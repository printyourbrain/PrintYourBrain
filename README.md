## Print Your Brain!

### [Website](https://www.ewi-psy.fu-berlin.de/en/v/ccnb/news_events/2021_04_28_Print-your-Brain.html) (new website coming soon xD )

![Teaser image](images/print-your-brain_logo_jpeg.jpg)

*CAUTION*  This repo is a work in progress.

This repository contains:

* important thing 1.
* important thing 2.
* even more important thing 3 ;p.

# Setup

### For usage in a container

#### Pre-Requisites

* [Docker engine](https://docs.docker.com/engine/install/).
* [Neurodocker](https://www.repronim.org/neurodocker/user_guide/installation.html).

Make sure you have your neurodocker image listed in `docker images`.

Docker cheatcodes to copy files in and out of your container-

```
docker cp src/. container_id:/target
docker cp container_id:/src/. target
```

#### Getting Started

1. Build the PYB image from this [Dockerfile](https://raw.githubusercontent.com/printyourbrain/PrintYourBrain/main/pyb.Dockerfile).

```
docker build --tag pyb - < pyb.Dockerfile
```

2. Run an interative bash in your image.

```
docker run -it -v /path/to/PrintYourBrain:/PrintYourBrain pyb:latest
```

3. Make sure pip is installed.

```
python -m ensurepip --upgrade
```

4. Activate the pyb conda environemnt within the container.

```
conda activate pyb
```

You are all set up to process your brain scans now! 🧠🚀


### For usage in a conda environment

#### Pre-Requisites

* [Anaconda](https://www.anaconda.com/products/individual).
* [Fressurfer](https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall).
* [ANTs](https://picsl.upenn.edu/software/ants/).

Make sure to setup both your freesurfeer and ANTs environment variables are set.

# Processing Brain Scans

1. Clone the repository.

```
git clone https://github.com/printyourbrain/PrintYourBrain.git
```
*If using container, start your docker image at this point!*

2. Change directory.

```
cd PrintYourBrain
```

3. Build the pyb package.

```
python -m pip install --upgrade build/
python -m build
```


4. Run the pyb script!

```
python pyb.py -i <input NIfTI file> -o <output directory name> -s <subject_name>
```

Run `python pyb.py -h` for usage instructions!

