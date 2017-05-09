# with open('../all_acute_kidney_hadm_id.txt') as file:
#     all_acute_kidney_hadm_id = [L.strip('\n') for L in file]

dic_icu_to_hadm = {}
with open('../icustay_id _to_hadm_id.txt') as file:
    for line in file.readlines()[1:]:
        two = line.strip("\n").split("\t")
        dic_icu_to_hadm[two[0]] = two[1]
print('键值对：', len(dic_icu_to_hadm))

with open('../all_acute_kidney_hadm_id.txt') as file:
    all_acute_kidney_hadm_id = [L.strip('\n') for L in file]
print('有病的hadm_id个数：', len(all_acute_kidney_hadm_id))

with open('../all_icu.txt') as file, open('../label.txt', 'w') as label_file:
    all_icu = [L.strip('\n') for L in file]
    print('icu个数：', len(all_icu))
    label_positive_count = 0
    for icu in all_icu[:]:
        if dic_icu_to_hadm.get(icu, False) in all_acute_kidney_hadm_id:
            label_file.write(icu + ',' + '1' + '\n')
            label_positive_count += 1
        else:
            label_file.write(icu + ',' + '0' + '\n')
    print("正例个数：", label_positive_count, '占比:', '%.2f' % (label_positive_count * 100 / len(all_icu)), '%')
