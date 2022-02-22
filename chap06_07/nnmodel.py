import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, InputLayer

CONTEXT_NEURON_NUM=2
HIDDEN_NEURON_NUM=4
sensor_data= [0.1,0.2,0.3,0.4,0.5,0.6,0.7]
#sensor_data= [0,0,0,0,0,0,0,]
context_val = np.zeros(CONTEXT_NEURON_NUM)
get_gene_length=60



nn_model = Sequential()
nn_model.add(InputLayer((7+CONTEXT_NEURON_NUM,)))
nn_model.add(Dense(HIDDEN_NEURON_NUM, activation='sigmoid'))
nn_model.add(Dense(2+CONTEXT_NEURON_NUM, activation='sigmoid'))






nn_input = np.r_[sensor_data, context_val]
nn_input = nn_input.reshape(1,9)
nn_output = nn_model.predict(nn_input)
action = np.array([nn_output[0][:2]])
context_val = nn_output[0][2:]







print(nn_input)
print(nn_output)
print(action)
print(context_val)
print(nn_model)






