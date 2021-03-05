
@app.post('/upload')
async def transcription_model(request: Request, file: UploadFile = File(...), email: str = Form(...)):
    file_location = f"audio_in/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    diar_df, highlights_list, words_df, confidence, text = diarization.diarize()
    shutil.os.remove('audio_in/' + file.filename)
    delete_file = glob('audio_out/*.wav')[0]
    shutil.os.remove(delete_file)
    questions = ''
    return templates.TemplateResponse('output.html',
           context={'request':request, 'keywords':keywords, 'summary':summary,
                    'questions':questions, 'highlights':highlights_list})