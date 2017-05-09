# 关于尿液的信息
result = ""
with open("与感染相关的icd9.txt", "r") as urine:
    for one_line in urine.readlines():
        print("1. "+one_line.split("\t")[1])

