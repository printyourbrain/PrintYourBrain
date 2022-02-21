source "./config.sh"

echo "****************************************************************************************************
Autorecon 1
****************************************************************************************************"

# autorecon1 (~ 20min)
cd $SUBJECTS_DIR
recon-all -s $OUTPUT_DIR -i $T1_NAME -autorecon1 -noskullstrip

echo "****************************************************************************************************
ANTs Brain Extraction
****************************************************************************************************"

# ANTs skullstripping
antsBrainExtraction.sh \
  -a ${SUBJECTS_DIR}/${T1_NAME} \
  -e ${TEMPLATE_DIR}/${BRAIN_TEMPLATE} \
  -m ${TEMPLATE_DIR}/${PROBABILITY_MASK} \
  -d 3 \
  -o ${SUBJECTS_DIR}/

mri_convert BrainExtractionBrain.nii.gz ./$OUTPUT_DIR/mri/brainmask.mgz

echo "****************************************************************************************************
Autorecon 2-3
****************************************************************************************************"

# autorecon2-3
recon-all -s $OUTPUT_DIR -autorecon2 -autorecon3

# # freeview - artifact checking
# cd $SUBJECTS_DIR/$OUTPUT_DIR

# freeview -v \
# mri/T1.mgz \
# mri/wm.mgz \
# mri/brainmask.mgz \
# mri/aseg.mgz:colormap=lut:opacity=0.2 \
# -f \
# surf/lh.white:edgecolor=blue \
# surf/lh.pial:edgecolor=red \
# surf/rh.white:edgecolor=blue \
# surf/rh.pial:edgecolor=red 

# cerebellum - 7,8,46,47
cd $SUBJECTS_DIR/$OUTPUT_DIR/mri

areas=(7 8 46 47)

for area in $areas
do
	subcortical_area="subcortical$area"
	mri_convert aseg.mgz "$subcortical_area.nii"
	mri_binarize --i "$subcortical_area.nii" --match $area --o bin.nii
	fslmaths subcortical47.nii -mul bin.nii "$subcortical_area-c.nii" 
	fslmaths "$subcortical_area-c.nii"  -bin "$subcortical_area-bin.nii"
	mri_tessellate "$subcortical_area-bin.nii.gz" 1 "$subcortical_area"
	mris_convert $subcortical_area $subcortical_area.stl
done

echo "****************************************************************************************************
Cerebellum Processed
****************************************************************************************************"

# convert rh/lh.pial to .stl files
mris_convert ./../surf/rh.pial ./rh.stl
mris_convert ./../surf/lh.pial ./lh.stl
