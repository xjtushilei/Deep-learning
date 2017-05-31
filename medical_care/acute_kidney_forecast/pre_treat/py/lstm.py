# -*- coding: utf-8 -*-


from keras import layers
from keras.models import Sequential
from load_data_all_deal import *

from keras import backend as K
import tensorflow
K.clear_session()
print("设置显卡信息...")
# 设置tendorflow对显存使用按需增长
config = tensorflow.ConfigProto()
config.gpu_options.allow_growth = True
session = tensorflow.Session(config=config)



# 前90%是训练数据，后10%是测试数据
# Explicitly set apart 10% for validation data that we never train over.
split_at = len(x) - len(x) // 10
(x_train, x_val) = x[:split_at], x[split_at:]
(y_train, y_val) = y[:split_at], y[split_at:]
print(x_val)
print(y_val)

HIDDEN_SIZE = 128
BATCH_SIZE = 128

print('Build model...')
model = Sequential()
model.add(layers.Masking(mask_value=-1, input_shape=(90, 3)))
model.add(layers.normalization.BatchNormalization())
model.add(layers.LSTM(HIDDEN_SIZE))
model.add(layers.normalization.BatchNormalization())
model.add(layers.Dense(HIDDEN_SIZE))
model.add(layers.Dense(2))
model.add(layers.Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='Nadam',
              metrics=['binary_accuracy'])
model.summary()

model.fit(x_train, y_train,
          batch_size=BATCH_SIZE,
          # class_weight={1: 800, 0: 20},
          epochs=200,
          validation_data=(x_val, y_val))

model.save('model_lstm' + '.h5')
