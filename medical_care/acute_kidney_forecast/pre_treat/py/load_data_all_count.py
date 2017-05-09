import pickle
import numpy as np
import matplotlib.pyplot as plt


train_matrix=[]
train_label=[]

with open('../label.txt') as label_file:
    for line in label_file.readlines():
        train_label.append(line.strip('\n'))

length=[]
with open('../train_all_-1000.data','rb') as train_data_file:
    train_matrix = pickle.loads(train_data_file.read())
    for one_id in train_matrix:
        length.append(len(one_id))

index = length.index(4123)
print(train_label[index])


print(length)
print("平均值:",np.mean(length))
print("最大值:",np.max(length))
print("最小值:",np.min(length))

plt.plot(range(0,len(length)),length,label='Frist line',linewidth=3,color='r',marker='o',markerfacecolor='blue',markersize=12)
plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()