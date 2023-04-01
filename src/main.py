import os
import docx2pdf
import time

# set directory path
directory = "~/docx2pdf"

while True:
    # loop through each file in directory
    for filename in os.listdir(directory):
        if filename.endswith(".docx"):
            # create input and output file paths
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, f"{os.path.splitext(filename)[0]}.pdf")

            # check if PDF already exists
            if os.path.isfile(output_path):
                print(f"{output_path} already exists. Skipping conversion.")
            else:
                # convert docx to pdf
                docx2pdf.convert(input_path, output_path)
                print(f"{input_path} converted to {output_path}")

    # wait for 10 seconds before looping again
    time.sleep(10)
