""" Utils file for converting file types"""


def nii_to_mgz(inputfile, outputfile):
    """Converts .nii inputfile to .mgz outputfile

    Args:
        inputfile (.nii): NIfTI file path
        outputfile (.mgz): MGZ output path
    """
    from nipype.interfaces.freesurfer import MRIConvert

    mc = MRIConvert()
    mc.inputs.in_file = inputfile
    mc.inputs.out_file = outputfile
    mc.inputs.out_type = "mgz"
    print(mc.cmdline)
    mc.run()
