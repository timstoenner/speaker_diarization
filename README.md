<!--

-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]




<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/studentstats/engagement-metrics">
    <img src="images/logo.png" alt="Logo" height="300" height="200">
  </a>

  <h3 align="center">StudentStats</h3>

  <p align="center">
    Engagement Metrics for Discussion-based Classrooms
    <br />
    <a href="https://github.com/studentstats/engagement-metrics"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!-- <a href="https://github.com/studentstats/engagement-metrics">View Demo (Coming Soon)</a> -->
    
  </p>
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

### **StudentStats**

> The quality of classroom relationships is one of the strongest predictors of students’ short-term and long-term academic success. As schools have moved online in the wake of COVID-19, 3.7 million teachers & 77 million US students are desperate for tools that will help them navigate this new environment. 

>Our system visualizes engagement metrics for discussion-based classrooms. We deliver a dashboard that tracks individual students and quantifies their engagement. Post-lesson, we provide descriptive statistics for each class period, along with automatic article and video recommendations related to the content of the given lesson.



### Built With

* [Assembly AI](https://www.assemblyai.com/)
* [Pyannote](https://github.com/pyannote/pyannote-audio)
* [Chord Pro](https://datacrayon.com/shop/product/chord-pro/)



<!-- USAGE EXAMPLES -->
## Process

<br />
<p align='left'>
  
  
  <h3 align="left"><strong>System Diagram</h3>    
  <img src="images/system_diagram.png" width='600' alt='System Diagram'>
     
  <br />  
</p>

## Documentation


[Technical Report](../blob/master/Technical_Report.pdf)

<img src="images/Doc_image.png" height='500' alt='System Diagram'>

## Usage

Step 1: Upload mp4 of class recording

<img src="images/upload page.png" height='350' alt='Upload Recording'>

Step 2: Get a cup of tea/coffee (and/or walk children/dog)

<img src="images/john-forson-WWzDPKot6nQ-unsplash.jpg" height='250' alt='coffee'>
<img src="images/chewy-OHV_IT371vI-unsplash.jpg" height='250' alt='dog'>

Step 3: Receive summary report of class in your email inbox 

<img src="images/mockup.png" height='350' alt='Chord Diagram'>


<!-- ROADMAP -->
## Roadmap
* This repository currently holds Version_1 of the StudentStats Engagement Metrics pipeline:
    * Upload mp4 of class recording, output email summary with features:
      * Discussion Tracker (via Chord diagram), displaying level of engagement between students in a classroom.
      * Sentence Classification:  delineate between questions and sentences
      * Summary of Discussion: 
        * Number of times each person spoke
        * Total words spoken per person
        * Highlighted/most important words from conversation
        * Summary sentence of the entire conversation

* Future versions will include:
    * Real-time Engagement Metrics dashboard
    * Speech Recognition/Diarization system trained on larger dataset with combined audio/video
    * Full integration with major video conferencing applications

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
## Contact
You can contact project creators @
[StudentStats](https://forms.gle/WDXMCcWLQrv9sYjU7)

Project Link: [https://github.com/studentstats/engagement-metrics](https://github.com/studentstats/engagement-metrics)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Assembly AI API](https://www.assemblyai.com/)
* [Lettergram: Sentence Classification](https://github.com/lettergram/sentence-classification)
* [Pyannote](https://github.com/pyannote/pyannote-audio)

@InProceedings{Bredin2020,
  Title = {{pyannote.audio: neural building blocks for speaker diarization}},
  Author = {{Bredin}, Herv{\'e} and {Yin}, Ruiqing and {Coria}, Juan Manuel and {Gelly}, Gregory and {Korshunov}, Pavel and {Lavechin}, Marvin and {Fustes}, Diego and {Titeux}, Hadrien and {Bouaziz}, Wassim and {Gill}, Marie-Philippe},
  Booktitle = {ICASSP 2020, IEEE International Conference on Acoustics, Speech, and Signal Processing},
  Address = {Barcelona, Spain},
  Month = {May},
  Year = {2020},
}






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/studentstats/engagement-metrics.svg?style=for-the-badge
[contributors-url]: https://github.com/studentstats/engagement-metrics/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/studentstats/engagement-metrics.svg?style=for-the-badge
[forks-url]: https://github.com/studentstats/engagement-metrics/network/members
[stars-shield]: https://img.shields.io/github/stars/studentstats/engagement-metrics.svg?style=for-the-badge
[stars-url]: https://github.com/studentstats/engagement-metrics/stargazers
[issues-shield]: https://img.shields.io/github/issues/studentstats/engagement-metrics.svg?style=for-the-badge
[issues-url]: https://github.com/studentstats/engagement-metrics/issues
[license-shield]: https://img.shields.io/github/license/studentstats/engagement-metrics.svg?style=for-the-badge
[license-url]: https://github.com/studentstats/engagement-metrics/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/studentstats
