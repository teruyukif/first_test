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

truncate = maxlen

Z = X[:1]

original = [f[i] for i in range(maxlen)]
predicted = [none for i in range(maxlen)]

for i in range(length_of_sequence - maxlen +1):
    z_ = Z[-1:]
    y_ = model.predict(z_)
    sequence_ = np.concatenate(
        (z_.resharp(maxlen, n_in)[1:], y_),axis=0).reshape(1, maxlen, n_in)
    Z = np.append(Z, sequence_, axis=0)
    predicted.append(y_.reshape(-1)))


#import numpy as np

#def sin(x, T=100):
#  return np.sin(2.0 * np.pi * x / T)
