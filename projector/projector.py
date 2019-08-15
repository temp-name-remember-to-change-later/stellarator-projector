# UNFINISHED

import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
import os
from tensorboard.plugins import projector

ds = ['data1.csv',
      'data2.csv',
      'data3.csv',
      'data4.csv',
      'data5.csv']

recdef = [tf.float64, tf.float64, tf.float64, tf.float64, tf.float64, tf.float64, tf.float64, tf.int32, tf.int32,
          tf.int32, tf.int32, tf.int32, tf.int32, tf.float64, tf.float64, tf.float64, tf.float64, tf.float64,
          tf.float64, tf.float64, tf.float64, tf.float64, tf.float64, tf.float64, tf.float64, tf.float64, tf.float64,
          tf.float64, tf.float64, tf.float64, tf.float64]

dataset = tf.data.experimental.CsvDataset(ds, recdef)

