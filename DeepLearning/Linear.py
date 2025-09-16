import numpy as np
from keras.models import Sequential
import matplotlib.pyplot as plt
from keras.layers import Dense

X=np.linspace(0,10,100)
y=3*X+7+3*np.random.randn(100)

model=Sequential()
model.add(Dense(units=1,input_dim=1,activation='linear'))


model.compile(optimizer='sgd',loss='mean_squared_error')
plt.scatter(X,y)
plt.show()

print(X.shape)
#plt.scatter(x)




from keras.models import Sequential
print("hello")

#simple linear regression code

