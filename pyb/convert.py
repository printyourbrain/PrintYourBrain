""" Utils file for converting file types"""

def nii_to_mgz(inputfile, outputfile):
    from nipype.interfaces.freesurfer import MRIConvert
    
    mc = MRIConvert()   
    mc.inputs.in_file = inputfile
    mc.inputs.out_file = outputfile
    mc.inputs.out_type = 'mgz'
    mc.cmdline
    mc.run()