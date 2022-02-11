""" Utils file for cortical surface reconstruction using freesurfer"""

from nipype.interfaces.freesurfer import ReconAll
from nipype.interfaces.ants.segmentation import BrainExtraction

from pyb.config import template


def autorecon1(subject, output_directory, T1file):
    """Performs the follwing operations-
        Motion Correction and Conform
        NU (Non-Uniform intensity normalization)
        Talairach transform computation
        Intensity Normalization 1
    """
    autorecon1 = ReconAll()
    autorecon1.inputs.subject_id = subject
    autorecon1.inputs.directive = "autorecon1"
    autorecon1.inputs.flags = "-noskullstrip"
    autorecon1.inputs.subjects_dir = output_directory
    autorecon1.inputs.T1_files = T1file
    print(autorecon1.cmdline)
    autorecon1.run()


def autorecon2_3(subject, output_directory):
    """Performs the following operations-
        EM Register (linear volumetric registration)
        CA Intensity Normalization
        CA Non-linear Volumetric Registration
        Remove Neck
        LTA with Skull
        CA Label (Volumetric Labeling, ie Aseg) and Statistics
        Intensity Normalization 2 (start here for control points)
        White matter segmentation
        Edit WM With ASeg
        Fill (start here for wm edits)
        Tessellation (begins per-hemisphere operations)
        Smooth1
        Inflate1
        QSphere
        Automatic Topology Fixer
        Final Surfs (start here for brain edits for pial surf)
        Smooth2
        Inflate2
        Spherical Mapping
        Spherical Registration
        Spherical Registration, Contralateral hemisphere
        Map average curvature to subject
        Cortical Parcellation - Desikan_Killiany and Christophe (Labeling)
        Cortical Parcellation Statistics
        Cortical Ribbon Mask
        Cortical Parcellation mapping to Aseg
    """
    autorecon2_3 = ReconAll()
    autorecon2_3.inputs.subject_id = subject
    autorecon2_3.inputs.directive = "autorecon2"
    autorecon2_3.inputs.args = "-autorecon3"
    autorecon2_3.inputs.subjects_dir = output_directory
    print(autorecon2_3.cmdline)
    autorecon2_3.run()


def brain_extraction(T1file, subject_directory, template_name="NKI"):
    """Performs Atlas based brain extraction with ANTS tool.
    """
    brainextraction = BrainExtraction()
    brainextraction.inputs.dimension = 3
    brainextraction.inputs.anatomical_image = T1file
    brainextraction.inputs.brain_template = template[template_name]["brain_template"]
    brainextraction.inputs.brain_probability_mask = template[template_name][
        "probablity_mask"
    ]
    brainextraction.inputs.out_prefix = subject_directory + "/"
    print(brainextraction.cmdline)
    brainextraction.run()
