import csv

file = "./TestSet_EAGLES.goldS.OFFICIAL"
output = "out.csv"


# read the file
with open(file, 'r') as f:
    lines = f.readlines()

    # clear output file
    with open(output, 'w') as o:
        # write the header
        writer = csv.writer(o, delimiter='\t')
        writer.writerow(["word", "tag", "lem"])

        for l in lines:
            # write the list to a csv file
            with open(output, 'a') as o:
                writer.writerow(l.lower().split())

        
    
