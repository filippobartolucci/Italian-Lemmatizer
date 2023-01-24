import csv

files =["./TestSet_Deployment/DevSet_EAGLES.goldS", "./TestSet_EAGLES.goldS.OFFICIAL"]
outputs = ["dev.csv", "test.csv"]

for i in range(len(files)):
    # read the file
    with open(files[i], 'r') as f:
        lines = f.readlines()
    
        # clear output1 file
        with open(outputs[i], 'w') as o:
            # write the header
            writer = csv.writer(o, delimiter='\t')
            writer.writerow(["word", "tag", "lem"])

            sentence = []

            for l in lines:
                # write the list to a csv file
                with open(outputs[i], 'a') as o:
                    w, l, t = l.lower().split()
                    writer.writerow([w, l, t])

                    if w == ".":
                        # remove substring from namne
                        fname = "sentences_" + outputs[i].replace(".csv", ".txt")
                        with open((fname), 'a') as o2:
                            # append the sentence to a file
                            o2.write(" ".join(sentence))
                            o2.write("\n")
                            sentence = []

                    else:
                        sentence.append(w)



        
    
