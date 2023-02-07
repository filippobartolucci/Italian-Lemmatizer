import csv

files =["./Evalita2011/TestSet_Deployment/DevSet_EAGLES.goldS", "./Evalita2011/TestSet_EAGLES.goldS.OFFICIAL"]
outputs = ["dev.csv", "test.csv"]
simplified_tags = True


def simplify_tag(tag):
    if tag.startswith("adj"):
        return "adj"
    elif tag.startswith("adv"):
        return "adv"
    elif tag.startswith("nn"):
        return "noun"
    elif tag.startswith("v_"):
        return "verb"

    return tag.split("_")[0]

for i in range(len(files)):
    # read the file
    with open(files[i], 'r') as f:
        lines = f.readlines()
    
        # clear output1 file
        with open(outputs[i], 'w') as o:
            # write the header
            writer = csv.writer(o, delimiter='\t')
            writer.writerow(["word", "tag", "lem"])


            for l in lines:
                with open(outputs[i], 'a') as o:
                    w, t, lem = l.lower().split()

                    if simplified_tags:
                        t = simplify_tag(t)

                    writer.writerow([w, t, lem])




        
