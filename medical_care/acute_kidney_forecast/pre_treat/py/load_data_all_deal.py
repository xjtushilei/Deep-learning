import pickle
import numpy as np
from keras.utils import np_utils
from keras.utils.np_utils import to_categorical

train_matrix = []
train_label = []

with open('../label.txt') as label_file:
    for line in label_file.readlines():
        train_label.append(int(line.strip('\n').split(',')[1]))

length = []
with open('../train_all_-1000.data', 'rb') as train_data_file:
    train_matrix = pickle.loads(train_data_file.read())
    for i in range(len(train_matrix[:])):
        if len(train_matrix[i]) > 90:
            train_matrix[i] = train_matrix[i][:90]
            if len(train_matrix[i]) > 90:
                print('出错了！')

        if len(train_matrix[i]) < 90:
            for j in range(len(train_matrix[i]), 90):
                train_matrix[i].append([-1, -1, -1])
        for j in range(len(train_matrix[i])):
            if -1000 in train_matrix[i][j]:
                for k in (0, 1, 2):
                    if train_matrix[i][j][k] == -1000:
                        if j - 1 < 0 and j + 1 < len(train_matrix[i]):
                            train_matrix[i][j][k] = train_matrix[i][j + 1][k]
                        elif j - 1 >= 0 and j + 1 < len(train_matrix[i]):
                            train_matrix[i][j][k] = (train_matrix[i][j - 1][k] + train_matrix[i][j + 1][k]) / 2
                        elif j - 1 >= 0 and j + 1 >= len(train_matrix[i]):
                            train_matrix[i][j][k] = train_matrix[i][j - 1][k]
                        else:
                            train_matrix[i][j][k] = 0
        length.append(len(train_matrix[i]))
print("平均值:", np.mean(length))
print("最大值:", np.max(length))
print("最小值:", np.min(length))

x = np.array(train_matrix)
y = np.array(train_label)
y = np_utils.to_categorical(y)
# 打乱顺序
indices = np.arange(len(y))
np.random.shuffle(indices)
x = x[indices]
y = y[indices]

print(x.shape)
