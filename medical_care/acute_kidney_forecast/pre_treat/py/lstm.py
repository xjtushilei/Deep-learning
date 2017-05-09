# -*- coding: utf-8 -*-


from keras import layers
from keras.models import Sequential
from load_data_all_deal import *

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
# model.add(layers.Conv2D(80))
model.add(layers.LSTM(256))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(2))
model.add(layers.Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='SGD',
              metrics=['accuracy'])
model.summary()

model.fit(x_train, y_train,
          batch_size=BATCH_SIZE,
          class_weight={1: 800, 0: 20},
          epochs=200,
          validation_data=(x_val, y_val))

model.save('model_lstm' + '.h5')
