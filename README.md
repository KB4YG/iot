<div align="center">

  <img src="https://raw.githubusercontent.com/KB4YG/kb4yg.github.io/main/assets/icon-white.png" alt="logo" width="200" height="auto" />
  <h1>KB4YG</h1>
  
  <p>
   Oak Creek Valley is a very popular destination for hiking and recreation for the city of Corvallis. Accessible forests in the Oak Creek Valley include the McDonald Forest, Cardwell Hill, Fitton Green, Bald Hill Farm, and others. These natural areas are enjoyed by many for hiking, mountain biking, and more. Our project, Know Before You Go, is an Internet of Things platform with a mobile app to help park visitors determine how busy a recreation site is before they arrive. By providing park visitors with this insight, we alleviate traffic congestion at trailheads, saving park visitors time and preventing overuse of natural areas.
  </p>
  
  <!-- Badges -->
<p>
  <a href="https://github.com/KB4YG/iot/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/KB4YG/iot" alt="contributors" />
  </a>
  <a href="https://github.com/KB4YG/iot/commits">
    <img src="https://img.shields.io/github/last-commit/KB4YG/iot" alt="last update" />
  </a>
  <a href="https://github.com/KB4YG/iot/stargazers">
    <img src="https://img.shields.io/github/stars/KB4YG/iot" alt="stars" />
  </a>
  <a href="https://github.com/KB4YG/iot/issues/">
    <img src="https://img.shields.io/github/issues/KB4YG/iot" alt="open issues" />
  </a>
</p>
   
<h4>    
    <a href="https://kb4yg.github.io">Demo</a>
  <span> · </span>
    <a href="https://github.com/KB4YG/frontend">Frontend</a>
  <span> · </span>
    <a href="https://github.com/KB4YG/iml">ML</a>
  <span> · </span>
    <a href="https://github.com/KB4YG/iot">IoT</a>
  </h4>
</div>

<br />

<!-- Table of Contents -->
# :notebook_with_decorative_cover: Table of Contents

- [Project Overview](#star2-about-the-project)
  * [Screenshots](#camera-screenshots)
  * [Tech Stack](#space_invader-tech-stack)
- [Getting Started](#toolbox-getting-started)
  * [Prerequisites](#bangbang-prerequisites)
- [Usage](#eyes-usage)
- [FAQ](#grey_question-faq)
- [License](#warning-license)
- [Contact](#handshake-contact)
- [Acknowledgements](#gem-acknowledgements)


<!-- About the Project -->
## :star2: About the Project
This repo contains all the code and setup instructions for running our running software on our Raspberry pi nodes. You'll find the code for the main script in in `src/main.py`.

<!-- Screenshots -->
### :camera: Screenshots

<div align="center"> 
  <img src="https://i.imgur.com/DoOP0bl.jpg" alt="screenshot" width="600px"/>
</div>

<!-- TechStack -->
### :space_invader: Tech Stack

#### Software
<li><a href="https://github.com/sixfab/sixfab-power-python-api">Sixfab Power Python API</a></li>
<li><a href="https://roboflow.com">Python 3</a></li>
#### Hardware
<li><a href="https://opencv.org">Raspberry Pi 4 B 2GB</a></li>
<li><a href="https://opencv.org">SixFab IoT Raspberry Pi Hat</a></li>
<li><a href="https://opencv.org">Solar Panel B</a></li>
<li><a href="https://opencv.org">RBattert etc B</a></li>


<!-- Getting Started -->
## 	:toolbox: Getting Started

<!-- Prerequisites -->
### :bangbang: Prerequisites

In /src/setup/installscript on your Pi run this Python file to install necessary Python and Linux packages.

```bash
  python setupscript.py 
```

<!-- Usage -->
## :eyes: Usage
In src/ run main.py. This script will auto turn off the Pi when complete and turn on when there is an interval.
```bash
  python main.py
```

<!-- License -->
## :warning: License

Distributed under the GPL-3.0 license. See [LICENSE.txt](https://github.com/KB4YG/iot/blob/main/LICENSE) for more information.


<!-- Contact -->
## :handshake: Contact

<!-- Acknowledgments -->
## :gem: Acknowledgements

 - [Shields.io](https://shields.io/)
 - [Readme Template](https://github.com/Louis3797/awesome-readme-template)
 - [TF-Lite Tutorial](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/examples/python/label_image.py)
 - [TF on RPi Tutorial](https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi)
