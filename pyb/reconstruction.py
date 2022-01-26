""" Utils file for cortical surface reconstruction using freesurfer"""

from nipype.interfaces.freesurfer import ReconAll
from nipype.interfaces.ants.segmentation import BrainExtraction

from pyb.config import template

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

def autorecon1(subject, subject_directory, T1file):
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
    autorecon1.inputs.T1_files = T1file
    print(autorecon1.cmdline)
    autorecon1.run()
    

def recon_flow():
    """Overall recon pipeline"""
    autorecon1('exampleT1', 'data/exampleT1', 'data/exampleT1.nii')
    
def brain_extraction(T1file, template_name='NKI'):
    """Performs Atlas based brain extraction with ANTS tool.
    """
    brainextraction = BrainExtraction()
    brainextraction.inputs.dimension = 3
    brainextraction.inputs.anatomical_image = T1file
    brainextraction.inputs.brain_template = template[str(template_name)]['brain_template']
    brainextraction.inputs.brain_probability_mask = template[str(template_name)]['probablity_mask']
    # brainextraction.inputs.args.o = 'dssd'
    print(brainextraction.cmdline)
    brainextraction.run()

# antsBrainExtraction.sh -a T1.nii.gz -m ProbabilityMaskOfStudyTemplate.nii.gz
# -e study_template.nii.gz -d 3 -s nii.gz -o highres001_'

# SUBJECT_DIR=""
# T1_NAME="s9400-HR.nii"
# TEMPLATE_DIR="" # folder containing the downloaded templates

# BRAIN_TEMPLATE="T_template2.nii.gz" # anatomical template with skull
# PROBABILITY_MASK="T_template_BrainCerebellumProbabilityMask.nii.gz" # make sure to use the one with cerebellum
# OUTPUT_DIR=${SUBJECT_DIR}/output

# antsBrainExtraction.sh \
#   -a ${SUBJECT_DIR}/${T1_NAME} \
#   -e ${TEMPLATE_DIR}/${TEMPLATE_NAME}/${BRAIN_TEMPLATE} \
#   -m ${TEMPLATE_DIR}/${TEMPLATE_NAME}/${PROBABILITY_MASK} \
#   -d 3 \
#   -o ${OUTPUT_DIR}

brain_extraction('data/exampleT1.nii')
