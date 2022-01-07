""" Utils file for cortical surface reconstruction using freesurfer"""

from nipype.interfaces.freesurfer import ReconAll
# >>> reconall = ReconAll()
# >>> reconall.inputs.subject_id = 'foo'
# >>> reconall.inputs.directive = 'all'
# >>> reconall.inputs.subjects_dir = '.'
# >>> reconall.inputs.T1_files = 'structural.nii'
# >>> reconall.cmdline
# 'recon-all -all -i structural.nii -subjid foo -sd .'

# recon-all -s s9400_MS -i s9400_MS.mgz -autorecon1
# recon-all -skullstrip -wsthresh 5 -clean-bm -subjid s9400_MS
# recon-all -skullstrip -clean-bm -gcut -subjid s9400_MS
# recon-all -s s9400_MS -autorecon2 -autorecon3

def autorecon1(subject, subject_directory, inputfile):
    """Performs the follwing operations-
        Motion Correction and Conform
        NU (Non-Uniform intensity normalization)
        Talairach transform computation
        Intensity Normalization 1
        Skull Strip
    """
    autorecon1 = ReconAll()
    autorecon1.inputs.subject_id = subject
    autorecon1.inputs.directive = 'autorecon1'
    autorecon1.inputs.subjects_dir = subject_directory
    autorecon1.inputs.T1_files = inputfile
    print(autorecon1.cmdline)
    autorecon1.run()
    

def recon_flow():
    """Overall recon pipeline"""
    autorecon1('exampleT1', 'data/exampleT1', 'data/exampleT1.nii')
    
# autorecon1()
recon_flow()