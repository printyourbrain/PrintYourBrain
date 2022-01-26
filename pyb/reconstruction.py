""" Utils file for cortical surface reconstruction using freesurfer"""

from nipype.interfaces.freesurfer import ReconAll
from nipype.interfaces.ants.segmentation import BrainExtraction

from pyb.config import template


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
    autorecon1.inputs.directive = "autorecon1"
    autorecon1.inputs.subjects_dir = subject_directory
    autorecon1.inputs.T1_files = T1file
    print(autorecon1.cmdline)
    autorecon1.run()


def recon_flow():
    """Overall recon pipeline"""
    autorecon1("exampleT1", "data/exampleT1", "data/exampleT1.nii")


def brain_extraction(T1file, subject_directory, template_name="NKI"):
    """Performs Atlas based brain extraction with ANTS tool.
    """
    brainextraction = BrainExtraction()
    brainextraction.inputs.dimension = 3
    brainextraction.inputs.anatomical_image = T1file
    brainextraction.inputs.brain_template = template[str(template_name)][
        "brain_template"
    ]
    brainextraction.inputs.brain_probability_mask = template[str(template_name)][
        "probablity_mask"
    ]
    brainextraction.inputs.out_prefix = subject_directory
    print(brainextraction.cmdline)
    brainextraction.run()
