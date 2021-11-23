## This file is for installing and running all components for print your brain.

#### OS version : ubuntu 20.04

The softwares required and their installation process is mentioned below:


---

### Installing Freesurfer

FreeSurfer is a software package for the analysis and visualization of structural and functional neuroimaging data from cross-sectional or longitudinal studies.

#### Step 1 : Download freesurfer

```
wget https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/7.2.0/freesurfer-linux-ubuntu18_amd64-7.2.0.tar.gz
```
The url may change according to the version. There is currently no distribution for ***ubuntu 20*** but we can use the distribution for ubuntu18.

#### Step 2 : Unzip the downloaded file

```
tar -zxpf freesurfer-linux-ubuntu18_amd64-7.2.0.tar.gz
```

#### Step 3 :

Once unzipped, an additional freesurfer folder will be created. 
Post that we need to set up freesurfer executable path. 
Usually this steps need to be done everytime a terminal session is created. 
But we can add it into ***.bashrc*** to automate the process. 
In either case, either add this line into ***.bashrc*** or run it when you open a terminal 

```
export FREESURFER_HOME=<path to freesurfer>/freesurfer
source $FREESURFER_HOME/SetUpFreeSurfer.sh
```
Verify ***$FREESURFER_HOME*** points to the correct path.

#### Step 4 : Get license key

Go to [here](https://surfer.nmr.mgh.harvard.edu/registration.html) and register your details.
Post registration a ***license.txt*** would be sent to the given mail address, store it in the folder mentioned in ***$FREESURFER_HOME***. 
This can be found by ```echo $FREESURFER_HOME```.

We can check if freesurfer has been properly configured and running by using ```which freesurfer``` and ```which freeview```.

---

### MATLAB

#### Step 1: Download matlab zipped file

If your academic institution gives matlab full version download the zipped file for your respective OS.

#### Step 2: Unzip the downloaded file

Then unzip the file.

#### Step 3: Install matlab

Open terminal and go the the unzipped matlab folder. Then initiate install file.

```
./install
```
Follow the steps in the gui and install matlab.

#### Step 4: Start matlab

There are different ways of starting matlab.

First, while installing matlab we are given an option to create ***symlink*** , if you selected this option and was successful in installing and creating the link,
we can start matlab by simply typing ```matlab``` in the terminal.

Second, in case the symlink was not successful and/or we didnot select that option, then we can run matlab by ```./<path to matlab folder>/bin/matlab```.

Third, we can create a symlink by following command 

```
sudo ln -s <path to matlab installed folder>/bin/matlab <path to simlink folder>/<symlink name>
```
Post generating <it>symlink</it> we can open a terminal and type ***symlink name*** to start matlab.

---

### SPM12

It is a package for analysis of brain imaging data .

#### Step 1 : Download package

The zipped file can be downloaded :

```
wget https://www.fil.ion.ucl.ac.uk/spm/download/restricted/eldorado/spm12.zip

wget http://www.fil.ion.ucl.ac.uk/spm/download/spm12_updates/spm12_updates_rxxxx.zip
```
The updates version needs to be placed in place of ***_rxxxx.zip***.

#### Step 2 : Unzip the downloaded file

Open the terminal and go to the path where the ***spm12.zip*** has been downloaded.

```
unzip spm12.zip
unzip -o spm12_updates_rxxxx.zip -d spm12
```

#### Step 3 : Add spm12 in matlab path

Open matlab, on ***Environment*** tab of the workspace , click on ***Set Path*** , then click on ***Add Folder*** and then go to the spm12 folder and save this folder.
This will add the ***spm12*** folder into the matlab path for execution. 

#### Step 4 : Compilation

```
cd <path to spm12 folder>/src
make distclean
make && make install
make external-distclean
make external && make external-install
```
***Troubleshooting***

1. mex : Command not found 

Create symlink to ***mex*** in matlab folder.

```
sudo ln -s <path to matlab folder>/bin/mex <path to symlink folder>/mex
```
Then close and restart terminal and continue the compilation.

Full installation step and further troubleshooting can be found [here](https://en.wikibooks.org/wiki/SPM/Installation_on_64bit_Linux).

---

### Meshlab

MeshLab is an open source, portable, and extendible system for the processing and editing of unstructured 3D triangular meshes. 

#### Step 1 : Update apt-get

Update the ***apt-get*** command line tool. This is done to ensure that all linux packages and their metadata are updated.

```
sudo apt-get update -y
```
#### Step 2 : Installation

Install meshlab in ubuntu.
```
sudo apt-get install -y meshlab
```

#### Step 3: Run meshlab

Run the following command from the terminal (location does not matter). If it has been installed properly, meshlab gui would start.

```
meshlab
```

---

