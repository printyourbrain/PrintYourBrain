"""Print Your Brain (PYB)."""

#!/usr/bin/python

import sys, getopt
import os

import pyb.config as config
from pyb.convert import nii_to_mgz

# setup subjects directory for freesurfer
os.environ['SUBJECTS_DIR'] = config.subjects_dir

def sub_process(process_name):
   print('-'*100)
   print(process_name, '...')
   print('-'*100)
   
def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, _ = getopt.getopt(argv,"hi:o:s:",["ifile=","ofile=","subj="])
   except getopt.GetoptError:
      print('pyb.py -i <input NIfTI file> -o <output directory name> -s <subject_name>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('pyb.py -i <input NIfTI file> -o <output directory name> -s <subject_name>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         assert arg.endswith('.nii') # supports only NIfTI files
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputdir = arg
      elif opt in ("-s", "--subj"):
         subject = arg
   print('Input NIfTI file is', inputfile)
   print('Output directory is', outputdir)
   
   return inputfile, outputdir, subject

if __name__ == "__main__":
   inputfile, outputdir, subject = main(sys.argv[1:])
   print('Running PYB for subject %s'%subject)
   
   # create subject dir to store all outputs
   subj_directory = os.path.join(outputdir, subject)
   if not os.path.exists(subj_directory):
        os.makedirs(subj_directory)

   sub_process('Converting NIfTI file to MGZ')
   outputfile = os.path.join(subj_directory, subject+'.mgz')
   nii_to_mgz(inputfile, outputfile)