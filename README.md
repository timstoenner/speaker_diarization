<!--

-->
<div align = 'center'>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![Linkedin][linkedin-shield]][linkedin-url]

</div>




<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Speaker Diarization with Pyannote & Assembly AI</h3>
  <br/>
  <br/>
  
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <!-- <li><a href="#roadmap">Roadmap</a></li> -->
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <!-- <li><a href="#contact">Contact</a></li> -->
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project



> This repo is a basic pipeline for transcribing audio with Assemblyi AI API, and diarizing speech occurrences for multiple speakers.



### Built With

* [Assembly AI](https://www.assemblyai.com/)
* [Pyannote](https://github.com/pyannote/pyannote-audio/tree/master)




<!-- USAGE EXAMPLES -->
## Getting Started

### Prerequisites

Install pyannote audio via instructions at 
[Pyannote](https://github.com/pyannote/pyannote-audio/tree/master)

```bash
$ pip install -q pyannote.audio==1.1 
$ pip install ffmpeg 
$ pip install --upgrade AudioConverter 
```

## Usage

An audio file can be uploaded, transcribed and diarized. Output is a dataframe timestamped sentences, separated by speaker. See jupyter notebook example for more details.

<!-- ROADMAP -->

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Assembly AI API](https://www.assemblyai.com/)
* [Pyannote](https://github.com/pyannote/pyannote-audio/tree/master)

```bibtex
@inproceedings{Bredin2020,
  Title = {{pyannote.audio: neural building blocks for speaker diarization}},
  Author = {{Bredin}, Herv{\'e} and {Yin}, Ruiqing and {Coria}, Juan Manuel and {Gelly}, Gregory and {Korshunov}, Pavel and {Lavechin}, Marvin and {Fustes}, Diego and {Titeux}, Hadrien and {Bouaziz}, Wassim and {Gill}, Marie-Philippe},
  Booktitle = {ICASSP 2020, IEEE International Conference on Acoustics, Speech, and Signal Processing},
  Address = {Barcelona, Spain},
  Month = {May},
  Year = {2020},
}
```





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/timstoenner/speaker_diarization.svg?style=for-the-badge
[contributors-url]: https://github.com/timstoenner/speaker_diarization/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/timstoenner/speaker_diarization.svg?style=for-the-badge
[forks-url]: https://github.com/timstoenner/speaker_diarization/network/members
[stars-shield]: https://img.shields.io/github/stars/timstoenner/speaker_diarization.svg?style=for-the-badge
[stars-url]: https://github.com/timstoenner/speaker_diarization/stargazers
[issues-shield]: https://img.shields.io/github/issues/timstoenner/speaker_diarization.svg?style=for-the-badge
[issues-url]: https://github.com/timstoenner/speaker_diarization/issues
[license-shield]: https://img.shields.io/github/license/timstoenner/speaker_diarization.svg?style=for-the-badge
[license-url]: https://github.com/timstoenner/speaker_diarization/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/tim-stoenner
