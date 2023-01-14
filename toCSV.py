import csv

file = "./TestSet_Deployment/DevSet_EAGLES.goldS"

# Word Tag Lemma
output1 = "out.csv"

# Sentences
output2 = "out2.csv"

# read the file
with open(file, 'r') as f:
    lines = f.readlines()
   
    # clear output1 file
    with open(output1, 'w') as o:
        # write the header
        writer = csv.writer(o, delimiter='\t')
        writer.writerow(["word", "tag", "lem"])

        sentence = []

        for l in lines:
            # write the list to a csv file
            with open(output1, 'a') as o:
                w, l, t = l.lower().split()
                writer.writerow([w, l, t])

                if w == ".":
                    with open(output2, 'a') as o2:
                        writer2 = csv.writer(o2, delimiter='\t')
                        writer2.writerow(sentence)
                        sentence = []
                else:
                    sentence.append(w)



        
    
