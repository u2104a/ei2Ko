#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <output_file> <URL>"
    exit 1
fi

# Assign arguments to variables for better readability
output_file=$1
URL=$2

# Generate the QR code
qrencode -m 2 --foreground=FFFFFF --background=000000 -o "$output_file" "$URL"

# Check if the QR code was generated successfully
if [ $? -eq 0 ]; then
    echo "QR code generated successfully: $output_file"
else
    echo "Failed to generate QR code."
    exit 1
fi

