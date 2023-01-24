import csv

file = "./altri_dataset/morph-it_048_utf8.txt"
output = "out.csv"

# read the file
with open(file, 'r') as f:
    lines = f.readlines()

    # create a set
    tags = set()

    # clear output file
    with open(output, 'w') as o:
        # write the header
        writer = csv.writer(o, delimiter='\t')
        writer.writerow(["word", "tag", "lem"])

        for l in lines:
            # write the list to a csv file
            with open(output, 'a') as o:
                w, l, t = l.lower().split()
                writer.writerow([w, t, l])
