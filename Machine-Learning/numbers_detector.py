import tensorflow.keras as keras
import tensorflow as tf
import numpy as np

# Loading Data Section Start
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)
# Loading Data Section End

# Training section Start
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


model.fit(x_train, y_train, epochs=3)
val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss)
print(val_acc)
# Training section End


# Predictions Section Start
model.save('numbers_detector.model')
new_model = tf.keras.models.load_model('numbers_detector.model')
predictions = new_model.predict(x_test)
print(np.argmax(predictions[0]))
# Predictions Section End
