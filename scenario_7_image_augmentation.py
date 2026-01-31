import tensorflow as tf
from tensorflow.keras import layers
data_augmentation = tf.keras.Sequential([
    layers.RandomRotation(0.2),
    layers.RandomFlip("horizontal"),
    layers.RandomZoom(0.2)])
