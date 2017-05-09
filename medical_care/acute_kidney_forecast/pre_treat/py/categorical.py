from keras.utils.np_utils import to_categorical


train_label = []

with open('../label.txt') as label_file:
    for line in label_file.readlines():
        train_label.append(int(line.strip('\n').split(',')[1]))
print(train_label)
y_binary = to_categorical(train_label)
print(y_binary)