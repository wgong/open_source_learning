# TensorFlow Tutorial #01 Simple Linear Model
# by Magnus Erik Hvass Pedersen http://www.hvass-labs.org/

# imports
###############################
# %matplotlib inline
# import matplotlib.pyplot as plt

import tensorflow as tf
import numpy as np
from sklearn.metrics import confusion_matrix

# load data
###############################

from tensorflow.examples.tutorials.mnist import input_data
data = input_data.read_data_sets("data/MNIST/", one_hot=True)

print("Size of:")
print("- Training-set:\t\t{}".format(len(data.train.labels)))
print("- Test-set:\t\t{}".format(len(data.test.labels)))
print("- Validation-set:\t{}".format(len(data.validation.labels)))

data.test.cls = np.array([label.argmax() for label in data.test.labels])

# Data dimensions
###############################

# We know that MNIST images are 28 pixels in each dimension.
img_size = 28

# Images are stored in one-dimensional arrays of this length.
img_size_flat = img_size * img_size

# Tuple with height and width of images used to reshape arrays.
img_shape = (img_size, img_size)

# Number of classes, one class for each of 10 digits.
num_classes = 10

# Hyperparameters
###############################
# step size of Gradient Descent Optimizer
learning_rate = \
	0.05
	#0.5
	
batch_size = \
	300
	#100

# build model graph
###############################
x = tf.placeholder(tf.float32, [None, img_size_flat])
y_true = tf.placeholder(tf.float32, [None, num_classes])
y_true_cls = tf.placeholder(tf.int64, [None])

weights = tf.Variable(tf.zeros([img_size_flat, num_classes]))
biases = tf.Variable(tf.zeros([num_classes]))
logits = tf.matmul(x, weights) + biases

y_pred = tf.nn.softmax(logits)
y_pred_cls = tf.argmax(y_pred, dimension=1)

cross_entropy = \
	tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels=y_true)
#tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits,labels=y_true)														
cost = tf.reduce_mean(cross_entropy)

optimizer = \
	tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)
	#tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)
	#tf.train.AdagradOptimizer(learning_rate=learning_rate).minimize(cost)

correct_prediction = tf.equal(y_pred_cls, y_true_cls)

accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


# Create TensorFlow session
###############################
session = tf.Session()
session.run(tf.global_variables_initializer())

feed_dict_test = {x: data.test.images,
                  y_true: data.test.labels,
                  y_true_cls: data.test.cls}

def optimize(num_iterations):
    for i in range(num_iterations):
        # Get a batch of training examples.
        # x_batch now holds a batch of images and
        # y_true_batch are the true labels for those images.
        x_batch, y_true_batch = data.train.next_batch(batch_size)
        
        # Put the batch into a dict with the proper names
        # for placeholder variables in the TensorFlow graph.
        # Note that the placeholder for y_true_cls is not set
        # because it is not used during training.
        feed_dict_train = {x: x_batch,
                           y_true: y_true_batch}

        # Run the optimizer using this batch of training data.
        # TensorFlow assigns the variables in feed_dict_train
        # to the placeholder variables and then runs the optimizer.
        session.run(optimizer, feed_dict=feed_dict_train)
		 
def print_accuracy():
    # Use TensorFlow to compute the accuracy.
    acc = session.run(accuracy, feed_dict=feed_dict_test)
    
    # Print the accuracy.
    print("Accuracy on test-set: {0:.1%}".format(acc))

def print_confusion_matrix():
    # Get the true classifications for the test-set.
    cls_true = data.test.cls
    
    # Get the predicted classifications for the test-set.
    cls_pred = session.run(y_pred_cls, feed_dict=feed_dict_test)

    # Get the confusion matrix using sklearn.
    cm = confusion_matrix(y_true=cls_true,
                          y_pred=cls_pred)

    # Print the confusion matrix as text.
    print(cm)


# run tests	
###############################
				  
# Performance after 1 optimization iteration
optimize(num_iterations=1)
print_accuracy()
#print_confusion_matrix()

# Performance after 10 optimization iteration
optimize(num_iterations=9)
print_accuracy()
print_confusion_matrix()

# Performance after 1000 optimization iterations
optimize(num_iterations=990)
print_accuracy()
print_confusion_matrix()

# 
session.close()
