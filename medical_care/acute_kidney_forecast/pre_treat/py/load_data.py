import pickle

train_matrix=[]
train_label=[]
with open('../train.data','rb') as train_data_file:
    train_matrix = pickle.loads(train_data_file.read())
with open('../label.txt') as label_file:
    for line in label_file.readlines():
        train_label.append(line.strip('\n').split(',')[1])

print(train_matrix)
print(train_label)