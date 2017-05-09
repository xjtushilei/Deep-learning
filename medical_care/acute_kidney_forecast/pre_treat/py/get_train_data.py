import json
import pickle
import time

dic_pt_scores_all = {}

txt_split = '\t'
temp_path = '201555.txt'

csv_path_split = ','
pt_score_csv_path = "D:\my_python\data\pt_scores_all\pt_scores_all.csv"

# 测试时候使用，正常请注释掉
# pt_score_csv_path = temp_path
# csv_path_split = txt_split

print(time.ctime(), '\t', '开始数据库文件，内存中生成字典')
with open(pt_score_csv_path) as file:
    for line in file.readlines()[:]:
        words = line.strip("\n").split(csv_path_split)
        id = words[0]
        length = words[1]
        cat = words[2]
        index = words[3]
        score = words[4]

        if length == '1':
            id_dic = dic_pt_scores_all.get(id, {})

            index_three_dic = id_dic.get(index, {})
            index_three_dic[cat] = score

            id_dic[index] = index_three_dic
            dic_pt_scores_all[id] = id_dic


def get_beautiful_json(obj, indent=4):
    '''
    获得优美的json
    :param obj: 需要展示的元素
    :param indent:  输出的空格
    :return: 
    '''
    json_string = json.dumps(obj, indent=indent)
    return json_string


print(time.ctime(), '\t', '开始在字典中搜索，并生成训练数据！')
train_matrix = []
error_num = 0
with open('../label.txt') as label_file:
    for line in label_file.readlines()[:]:
        (icu_id, label) = line.strip('\n').split(",")
        icu_id_dic = dic_pt_scores_all.get(icu_id, {})
        # print(icu_id_dic)
        sort_list = sorted(icu_id_dic.items(), key=lambda d: int(d[0]))
        matrix_of_one_icu = []

        for i in sort_list:
            try:
                APACHEII = i[1].get('APACHEII', '-1000')
                if APACHEII == '':
                    APACHEII = '-1000'
                SOFA = i[1].get('SOFA', '-1000')
                if SOFA == '':
                    SOFA = '-1000'
                SAPSII = i[1].get('SAPSII', '-1000')
                if SAPSII == '':
                    SAPSII = '-1000'

                if APACHEII == '-1000': error_num += 1
                if SOFA == '-1000': error_num += 1
                if SAPSII == '-1000': error_num += 1

                matrix_of_one_icu.append([float(APACHEII),
                                          float(SOFA),
                                          float(SAPSII)])
            except Exception as e:
                print(e)
        train_matrix.append(matrix_of_one_icu)

print("不正常数据个数:", error_num)
# 文件太大，非常非常非常非常不建议输出
# print(get_beautiful_json(train_matrix,indent=None))
print(time.ctime(), '\t', '训练数据已经生成，开始序列化到本地磁盘中！')
with open('../train.data', 'wb') as train_data_file:
    pickle.dump(train_matrix, train_data_file)
    print(time.ctime(), '\t', '训练数据生成，位于： "../train.data" ')

