#!/bin/bash

FILE="$1"
BUCKET="$2"
SEC="$3" #set equal to 604800 or shorter

# uploads a file to a private bucket

aws s3 cp "$FILE" "s3://$BUCKET/" 

# presigns a URL to that file with an expiration of 604800

aws s3 presign --expires-in "$SEC" "s3://$BUCKET/$FILE" 

