import glob

# list all .txt files in the current directory
txt_files = glob.glob(
    r"*.txt")

# open the output file for writing
with open(r"output_normals.xyz", "w") as outfile:
    # loop over each input file
    for filename in txt_files:
        with open(filename, "r") as infile:
            # loop over each line in the input file
            for line in infile:
                # write the line to the output file
                outfile.write(line)
