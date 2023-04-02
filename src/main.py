import os
import time
import subprocess

# set directory path relative to the script directory
directory = "/docx2pdf"

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
                # create PDF converter command
                cmd = ["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", directory, input_path]

                # convert docx to pdf using libreoffice
                print(f"Converting {input_path} to PDF...")
                subprocess.run(cmd)

                print(f"{input_path} converted to {output_path}")

    # wait for 10 seconds before looping again
    print("Waiting for 10 seconds...")
    time.sleep(10)