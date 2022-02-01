## Print Your Brain!

### [Website](https://www.ewi-psy.fu-berlin.de/en/v/ccnb/news_events/2021_04_28_Print-your-Brain.html) (new website coming soon xD )

![Teaser image](images/print-your-brain_logo_jpeg.jpg)

*CAUTION*  This repo is a work in progress.

This repository contains:

* important thing 1.
* important thing 2.
* even more important thing 3 ;p.

# Setup

1. Either [download](https://github.com/printyourbrain/PrintYourBrain/archive/refs/heads/main.zip) or clone the repository.

```
git clone https://github.com/printyourbrain/PrintYourBrain.git
```

2. Change directory.

```
cd PrintYourBrain
```

### For usage in a container

DISCLAIMER: You need ~4GB free storage space for this.

#### Pre-Requisites

* [Docker engine](https://docs.docker.com/engine/install/).
* [Neurodocker](https://www.repronim.org/neurodocker/user_guide/installation.html).

Make sure you have your neurodocker image listed in `docker images`.

#### Getting Started

1. Build the PYB image from [this](https://raw.githubusercontent.com/printyourbrain/PrintYourBrain/main/pyb.Dockerfile) Dockerfile.

```
docker build --tag pyb - < pyb.Dockerfile
```

2. Run an interative bash in your image, while mounting the PrintYourBrain folder and specifying your Freesurfer license file.

```
docker run -it -v /path/to/PrintYourBrain:/PrintYourBrain -v /path/to/your/freesurfer/license.txt:/opt/freesurfer-6.0.0-min/license.txt pyb:latest
```
You can get your license file from [here](https://surfer.nmr.mgh.harvard.edu/fswiki/License) incase you don't have one!


3. Make sure pip is installed.

```
python -m ensurepip --upgrade
```

4. Configure your shell and restart it.

```
conda init bash
exec bash
```

5. Activate the pyb conda environemnt within the container.

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

#### Getting Started

1. Creat a conda environment from [this](https://raw.githubusercontent.com/printyourbrain/PrintYourBrain/main/environment.yml) environment file.

```
conda env create --file environment.yml
```

2. Start your conda environment.


```
conda activate pyb
```

# Processing Brain Scans

Now that you are in your docker container or the conda environment, you are ready to start processing your T1w brain images!

1. Build the pyb package.

```
python -m pip install --upgrade build
python -m build
```

2. Configure your project and update paths in config.py.

3. Run the pyb script!

```
python pyb.py -i <input NIfTI file> -o <output directory name> -s <subject_name>
```

Run `python pyb.py -h` for usage instructions!

