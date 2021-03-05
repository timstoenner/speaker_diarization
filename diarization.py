#pip install -q pyannote.audio==1.1
#pip install ffmpeg
#pip install --upgrade AudioConverter



from pyannote.core import Segment, notebook
from pyannote.audio.features import RawAudio
from pyannote.database.util import load_rttm
from IPython.display import Audio
import torch
import pandas as pd
import numpy as np
import re
import os
import sys
import time
import requests
import subprocess
import json

from glob import glob


#need to read mp4 and convert to wav
f = open("keys.json", "r")
keys = json.load(f)
ASSEMBLY_API = keys["API"]
f.close()

def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data


def convert_to_wav():
    
    os.system("audioconvert convert audio_in/ audio_out/ --output-format .wav")
    
    file = glob(os.path.join('./audio_out/', '*'))[0]

    URI = os.path.splitext(file)[0]   

    audio_file = {'uri': URI, 'audio': file}

    return audio_file

def diarize():
    
    audio_file = convert_to_wav()

    pipeline = torch.hub.load('pyannote/pyannote-audio', 'dia')

    diarization = pipeline(audio_file)
    diar_json = diarization.for_json()
    diar_df = pd.DataFrame.from_dict(diar_json['content'])

    diar_df['start'] = [diar_df['segment'][i]['start'] for i in range(len(diar_df['segment']))]
    diar_df['end'] = [diar_df['segment'][i]['end'] for i in range(len(diar_df['segment']))]
    diar_df = diar_df[['label', 'start', 'end']]

    d = {'label': 'first', 'start': 'min', 'end': 'max'}   # How to aggregate
    s = diar_df.label.ne(diar_df.label.shift(1)).cumsum().rename(None) # How to group

    diar_df = diar_df.groupby(s).agg(d)

    transcript_json = transcribe_file(audio_file['audio'], API_KEY = ASSEMBLY_API)

    confidence = transcript_json['confidence']
    text = transcript_json['text']
    highlights_list = [transcript_json['auto_highlights_result'].get('results')[i]['text'] for i in range(len(transcript_json['auto_highlights_result'].get('results')))]
    
    words_df = pd.DataFrame.from_dict(transcript_json['words'])
    words_df[['end', 'start']] = words_df[['end', 'start']] / 1000
    words_df = words_df[['text', 'start', 'end']]
    
    diar_df.reset_index(inplace=True)
    diar_df = diar_df[['label', 'start', 'end']]
    diar_df.columns = ['Speaker', 'sent_start', 'sent_end']

    df = pd.DataFrame()

    for i in range(len(diar_df)):
        if i == 0:
            series = (words_df.loc[np.where(words_df['start'] < diar_df.iloc[i+1,1])])['text']
            series = np.asarray(series)
            sentence= ' '.join(series)
            df2 = pd.Series(sentence)
            #df.append(df2)
            df = pd.concat([df,df2], axis=0)
            
        elif i == len(diar_df)-1:
            series = (words_df.loc[np.where(words_df['start'] >= diar_df.iloc[i,1])])['text']
            series = np.asarray(series)
            sentence= ' '.join(series)
            df2 = pd.Series(sentence)
            #df.append(df2)
            df = pd.concat([df,df2], axis=0)
            
        else:
            series = (words_df.loc[np.where((diar_df.iloc[i,1] <= words_df['start']) & (words_df['start'] < diar_df.iloc[i+1,1]))])['text']
            series = np.asarray(series)
            sentence= ' '.join(series)
            df2 = pd.Series(sentence)
            #df.append(df2)
            df = pd.concat([df,df2], axis=0)
    
    df.index = [diar_df.iloc[:,0]]
    
    df.reset_index(inplace=True)
    df[['Start', 'End']] = diar_df[['sent_start', 'sent_end']]
    
    diar_df['Talk_Time'] = diar_df['End'] - diar_df['Start']
    diar_df = diar_df.reindex(columns=['Speaker', 'Sentences', 'Start', 'End', 'Talk_Time'])


    keywords, summary, links, crosstab = feedback(df=diar_df)

    

    return diar_df, keywords, summary, links, crosstab, highlights_list, words_df, confidence, text



def transcribe_file(wav, API_KEY, **kwargs):
  
    data = read_file(wav)

    headers = {'authorization': API_KEY }
    response = requests.post('https://api.assemblyai.com/v2/upload',
                            headers=headers,
                            data=data)

    #this is needed for the next call below - 'audio url'
    url = response.json()['upload_url']


    endpoint = "https://api.assemblyai.com/v2/transcript"

    json = {
        "audio_url": f"{url}", 
        'auto_highlights': True,
        'speaker_labels': False, 
    }

    headers = {
        "authorization": API_KEY,
        "content-type": "application/json"
    }

    response = requests.post(endpoint, json=json, headers=headers)
    id = response.json()['id']

    endpoint = f"https://api.assemblyai.com/v2/transcript/{id}"

    headers = {
        "authorization": API_KEY,
        

    }

    response = requests.get(endpoint, headers=headers)
    status = response.json()['status']
    while status == 'queued' or status == 'processing':
        response = requests.get(endpoint, headers=headers)
        status = response.json()['status']

    transcript_json = response.json()


    return transcript_json

def transcribe_url(url, API_KEY, **kwargs):

    endpoint = "https://api.assemblyai.com/v2/transcript"

    json = {
        "audio_url": f"{url}", 
        'auto_highlights': True,
        'speaker_labels': False, 

    }

    headers = {
        "authorization": API_KEY,
        "content-type": "application/json"
    }

    response = requests.post(endpoint, json=json, headers=headers)
    id = response.json()['id']

    endpoint = f"https://api.assemblyai.com/v2/transcript/{id}"

    headers = {
        "authorization": API_KEY,   

    }

    response = requests.get(endpoint, headers=headers)
    status = response.json()['status']
    while status == 'queued' or status == 'processing':
        response = requests.get(endpoint, headers=headers)
        status = response.json()['status']

    transcript_json = response.json()


    return transcript_json