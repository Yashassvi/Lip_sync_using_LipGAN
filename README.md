# Lip_sync_using_LipGAN
Prerequisites
-------------
- Python >= 3.5
- ffmpeg: `sudo apt-get install ffmpeg`
- Install necessary packages using `pip install -r requirements.txt`
- Install keras-contrib `pip install git+https://www.github.com/keras-team/keras-contrib.git`

Getting the weights
----------
Download checkpoints of the folowing models into the `logs/` folder

- CNN Face detection using dlib: [Link](http://dlib.net/files/mmod_human_face_detector.dat.bz2)
- LipGAN [Google Drive](https://drive.google.com/file/d/1DtXY5Ei_V6QjrLwfe7YDrmbSCDu6iru1/view?usp=sharing)

Generating talking face videos using pretrained models (Inference)
-------

Here, we are given an audio input and a video of an identity speaking something entirely different.
LipGAN can synthesize the correct lip motion for the given audio and overlay it on the given video of the speaking identity.
