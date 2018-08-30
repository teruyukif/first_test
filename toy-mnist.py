import keras
from keras.datasets import mnist
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import Adam
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

import matplotlib.pyplot as plt
#%matplotlib inline

#データの読み込みを行う
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#読み込んだデータを表示する
#fig = plt.figure(figsize=(9, 9))
#fig.subplots_adjust(left=0, right=1, bottom=0, top=0.5, hspace=0.05, wspace=0.05)
#for i in range(81):
#    ax = fig.add_subplot(9, 9, i + 1, xticks=[], yticks=[])
#    ax.imshow(x_train[i].reshape((28, 28)), cmap='gray')
#plt.show()

# 2次元データを数値に変換
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

# 型変換
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# 255で割ったものを新たに変数とする
x_train /= 255
x_test /= 255

# クラス数は10
num_classes = 10
y_train = y_train.astype('int32')
y_test = y_test.astype('int32')

#バイナリーのクラス行列に変換する
y_train = to_categorical(y_train, num_classes)
y_test =  to_categorical(y_test, num_classes)

# モデル作成
model = Sequential()
#全結合
model.add(Dense(512, activation='sigmoid', input_shape=(784,)))
#model.add(Dense(512, activation='elu', input_shape=(784,)))
#model.add(Dense(512, activation='selu', input_shape=(784,)))
#model.add(Dense(512, activation='softplus', input_shape=(784,)))
#model.add(Dense(512, activation='softsign', input_shape=(784,)))
#model.add(Dense(512, activation='relu', input_shape=(784,)))
#model.add(Dense(512, activation='tanh', input_shape=(784,)))
#model.add(Dense(512, activation='sigmoid', input_shape=(784,)))
#model.add(Dense(512, activation='hard_sigmoid', input_shape=(784,)))
#model.add(Dense(512, activation='linear', input_shape=(784,)))

#過学習を防ぐためにランダムに0を入れる
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(10, activation='softmax'))

#モデルの要約を出力します
model.summary()

# バッチサイズ、エポック数
batch_size = 128
epochs = 20

#学習の為の設定を行う
model.compile(loss='categorical_crossentropy',
              optimizer=Adam(),
              metrics=['accuracy'])

#固定回数（データセットの反復）の試行でモデルを学習させます．
history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(x_test, y_test))
#モデルの損失値と評価値を返します
score = model.evaluate(x_test, y_test, verbose=0)

print('Test loss:', score[0])
print('Test accuracy:', score[1])


#Accuracy
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()


#loss
#plt.plot(history.history['loss'])
#plt.plot(history.history['val_loss'])
#plt.title('model loss')
#plt.ylabel('loss')
#plt.xlabel('epoch')
#plt.legend(['train', 'test'], loc='upper left')
#plt.show()

#SVG(model_to_dot(model).create(prog='dot', format='svg'))
