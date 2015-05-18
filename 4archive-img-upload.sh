#!/bin/bash

# BASC-4archive: 4archive-img-upload.py

# Uploads 4archive image archives via Internet Archive's S3
# keys. Make sure you have ~/.s3cfg set up.

# first argument is board
BOARD=$1
WORKDIR=$BOARD-zip/4archive

cd 4archive/

# if workdir doesn't exist, stop the script
if [ -f "$BOARD-zip/$BOARD-images-4archive.zip" ]; then
	echo "Please compress the images first, using './4archive-img-zip.sh' ."
	exit 0
fi

# zip up the folder
cd $BOARD-zip/

# upload to Internet Archive
s3cmd put $BOARD-images-4archive.zip s3://4archive/
cd ..

# move everything out of the folder before deletion
mv $WORKDIR/* .

# clean up the temp folder
#rm -rf $BOARD-zip