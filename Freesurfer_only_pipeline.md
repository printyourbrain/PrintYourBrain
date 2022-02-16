# Readme

Follow this instruction to convert a brain image in .nii or .mgz format into a .stl file for 3D printing. 

- **Note 1**: This is an old version of PYB pipeline that only needs freesurfer. To try the newest pipeline, follow the instructions in [this page](https://github.com/printyourbrain/PrintYourBrain).
- **Note 2**: This instruction is only for Mac. Windows user can follow [this tutorial](https://drive.google.com/drive/folders/1zd_3EC6rt_I1LIOu99jggR4t60GWY4Ez), and replace the SPM processing steps with the gcut step from this instruction.
- **Note 3**: After having the .stl files, you can download [MeshLab](https://www.meshlab.net/#download), view your 3D brain and smooth the imperfections there before printing.

## Pre-requisite:

1. Download FreeSurfer [here](https://surfer.nmr.mgh.harvard.edu/fswiki/rel7downloads), and install it
2. Get the FreeSurfer [license.txt](https://surfer.nmr.mgh.harvard.edu/registration.html), and place it under your freesurfer path
3. Prepare your to-be-processed brain. You can get it from an MRI experiment.

## Process your brain:

### 1. Setup FreeSurfer

**Note: You need to do this setup every time your open a new terminal!*

```bash
export FREESURFER_HOME=/path-to-your-freesurfer
source /path-to-your-freesurfer/SetUpFreeSurfer.sh
export SUBJECTS_DIR=/path-to-your-freesurfer/subjects
```

### 2. Run autorecon1

```bash
cd /path-to-your-freesurfer/subjects
recon-all -s subject_output_folder -i input_image_file -autorecon1
```

### 3. Run -gcut

```bash
recon-all -skullstrip -clean-bm -gcut -subjid subject_output_folder
```

### 4. Run autorecon2 and autorecon3

```bash
recon-all -s subject_output_folder -autorecon2 -autorecon3
```

### 5. Convert brain surfaces to .stl file

```bash
mris_convert /path_to_your_freesurfer/subjects/subject_output_folder/surf/lh.pial lh.stl
mris_convert /path_to_your_freesurfer/subjects/subject_output_folder/surf/rh.pial rh.stl
```

## Here is an example script on Mac:

```bash
#0. Get your brain image, e.g., example_T1.nii 

#1. Setup FreeSurfer
export FREESURFER_HOME=/Applications/freesurfer/7.2.0
source /Applications/freesurfer/7.2.0/SetUpFreeSurfer.sh
export SUBJECTS_DIR=/Applications/freesurfer/7.2.0/subjects

#2. Run autorecon1
cd /Applications/freesurfer/7.2.0/subjects
recon-all -s example_T1 -i example_T1.nii -autorecon1

#3. Run -gcut
recon-all -skullstrip -clean-bm -gcut -subjid example_T1

#4. Run autorecon2 and autorecon3
recon-all -s example_T1 -autorecon2 -autorecon3

#5. Convert brain surfaces to -stl files
mris_convert /Applications/freesurfer/7.2.0/subjects/example_T1/surf/lh.pial lh.stl
mris_convert /Applications/freesurfer/7.2.0/subjects/example_T1/surf/rh.pial rh.stl
```