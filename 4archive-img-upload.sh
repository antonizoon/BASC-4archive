#!/bin/bash

# BASC-4archive: 4archive-img-upload.py

# Uploads 4archive image archives via Internet Archive's S3
# keys. Make sure you have ~/.s3cfg set up.

# first argument is board
BOARD=$1
WORKDIR=$BOARD-zip/4archive

cd 4archive/

# create a nested 4archive folder and move the desired board to it
mkdir -p $WORKDIR
mv $BOARD 4archive/

# zip up the folder
zip -3 -r $BOARD-images-4archive.zip $WORKDIR

# move the board out of the folder
mv $WORKDIR/$BOARD .

# upload to Internet Archive
s3cmd put $BOARD-images-4archive.zip s3://4archive/