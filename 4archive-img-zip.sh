#!/bin/bash

# BASC-4archive: 4archive-img-upload.py

# Uploads 4archive image archives via Internet Archive's S3
# keys. Make sure you have ~/.s3cfg set up.

# first argument is board
BOARD=$1
WORKDIR=$BOARD-zip/4archive

# if zip file exists, stop the script
if [ -f "$BOARD-zip/$BOARD-images-4archive.zip" ]; then
	echo "Images for $BOARD have already been compressed."
	exit 0
fi

cd 4archive/

# create a nested 4archive folder and move the desired board to it
mkdir -p $WORKDIR
mv $BOARD $WORKDIR/

# zip up the folder
cd $BOARD-zip/
zip -3 -r $BOARD-images-4archive.zip 4archive/