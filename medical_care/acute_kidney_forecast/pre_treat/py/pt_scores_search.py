with open("M:\my_python\data\pt_scores_all\pt_scores_all.csv") as file:

    for line in file:
        words = file.readline().strip("\n").split(",")
        if words[0] == '274671':
            print(words)
