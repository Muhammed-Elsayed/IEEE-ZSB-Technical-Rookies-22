import tensorflow as tf 
# importing datasets which is an image of 28 * 28 
mnist = tf.keras.datasets.mnist  

# unpacking data into training and testing 
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# normalizing the model by making its value between 0 and 1
x_train = tf.keras.utils.normalize(x_train, axis = 1)
x_test = tf.keras.utils.normalize(x_test, axis = 1)
# making the model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten()) # making the model flat
# making the hidden layers which is only 2 because this problem isnot complicated
model.add(tf.keras.layers.Dense(128, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation = tf.nn.relu))
# making the output layer 
model.add(tf.keras.layers.Dense(10, activation = tf.nn.softmax))
#defining the training parameters of the model and reducing the loses
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

# training the test
model.fit(x_train, y_train, epochs = 3)

# save the model
model.save("cat.model")
# loading the model
new_model = tf.keras.models.load_model("cat.model")

predictions = new_model.predict([x_test])
# printing the first prediction
import numpy as np
print(np.argmax(predictions[0]))
