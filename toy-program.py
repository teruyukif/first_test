# coding: UTF-8
import numpy as np
#from keras.models import Sequential
#from keras.layers import Dense, Activation
#from keras.optimizers import SGD
#import tensorflow as tf

#import keras
#print(keras.__version__)

#ランダムで２０行４列の配列を作成している
data = np.random.randn(10, 4)
print ("data:" , data)

#それぞれを2乗している
squared = data**2
print ("squared:" , squared)

#配列の和をとって１次配列にする
squared_sum = np.sum(squared, axis=1)
print ("squared_sum:" , squared_sum)

#平方根をとる
dist = np.sqrt(squared_sum)
print ("dist:" ,dist)

#平均を算出する。
print (np.mean(dist))


#print (u"こんにちは、PYTHON!!")
