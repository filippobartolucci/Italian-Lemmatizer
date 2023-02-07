import csv

files =["./Evalita2011/TestSet_Deployment/DevSet_EAGLES.goldS", "./Evalita2011/TestSet_EAGLES.goldS.OFFICIAL"]
outputs = ["dev.csv", "test.csv"]
simplified_tags = False



def simplify_tag(tag):
    if tag.startswith("adj"):
        return "adj_"
    elif tag.startswith("adv"):
        return "adv"
    elif tag.startswith("nn"):
        return "nn"
    elif tag.startswith("v_"):
        return "v_"

    return tag

for i in range(len(files)):
    tag_counter = {}
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

                    if t not in tag_counter:
                        tag_counter[t] = 0
                    tag_counter[t] += 1

                    writer.writerow([w, t, lem])


    print("\n\n", outputs[i], "tags count:")
    open_class = ["nn", "nn_p", "v_gvrb", "v_essere", "v_avere", "v_pp", "v_mod", "v_clit", "adv", "adj_ind", "adj_num", "adj", "adj_pos", "adj_dim", "adj_ies"]
    open_class_count = 0
    for k, v in tag_counter.items():
        if k in open_class:
            open_class_count += v
    print("open class count", open_class_count)

        
