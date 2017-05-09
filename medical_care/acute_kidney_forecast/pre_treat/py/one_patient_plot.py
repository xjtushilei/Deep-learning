import pickle
import numpy as np
import matplotlib.pyplot as plt

temp_path = '201555.txt'

with open('../train.data', 'rb') as train_data_file:
    train_matrix = pickle.loads(train_data_file.read())

print(train_matrix[0])
print(train_matrix[1])

for i in  range(len(train_matrix)):
    mt = np.array(train_matrix[i])
    # mt = mt.reshape(mt.size(1), mt.size(0))

    y1 = mt[:, :1]

    print(y1.T[0])

    x1 = range(0, len(y1.T[0]))
    plt.plot(x1, y1, label='Frist line')

    plt.show()