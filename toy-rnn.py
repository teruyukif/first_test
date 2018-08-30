from keras.layers.recurrent import SimpleRNN
from keras.models import Sequential

model = Sequential()
model.add(SimpleRNN(n_hidden,
                    kernel_initializer=weight_variable,
                    input_shape=(maxlen, n_in)))
model.add(Dense(n_out,kernel_initializer=weight_variable))
model.add(Activation('linear'))

optimizer = Adam(lr=0.001, beta_1=0.9, beta_2=0.999)
model.compile(loss='mean_squared_error', optimaizer=optimizer)

epochs = 500
batch_size = 10

model.fit(X_train, Y_train,
          batch_size=batch_size,
          epochs=epochs,
          validation_data=(X_validation,Y_validation),
          callbacks=[early_stopping])




#import numpy as np

#def sin(x, T=100):
#  return np.sin(2.0 * np.pi * x / T)
