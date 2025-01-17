#!/usr/bin/env python3


import argparse
from launch import launch_train_test

################################################################################
### PARSE COMMAND LINE ARGUMENTS
################################################################################

parser = argparse.ArgumentParser(description='Create an AP network for Question Answering')

parser.add_argument("-n", help="type of the network, either CNN or biLSTM", type=str, default='AP-CNN', dest='network_type', choices=['AP-CNN','AP-biLSTM','CNN','biLSTM'])
parser.add_argument("-d", help="dataset to use, either TrecQA or WikiQA", type=str, default='TrecQA', dest='dataset_name', choices=['TrecQA','WikiQA'])
parser.add_argument("-m", help="specify which embedding model should be used", type=str, default='LearnPyTorch', dest='model_type', choices=['Google', 'GoogleRed', 'LearnGensim', 'LearnPyTorch', 'Glove', 'Wiki'])
parser.add_argument("-p", help="use powerful cuda nvidia gpu", dest='use_gpu', action='store_true')
args = parser.parse_args()

network_type = args.network_type
dataset_name = args.dataset_name
model_type = args.model_type
use_cuda = args.use_gpu


################################################################################
### HYPERPARAMETERS - CHANGE THIS PART
################################################################################

#'''
# Best for CNN

k = 3
word_embedding_size = 300
word_embedding_window = 5
convolutional_filters = 3600
batch_size = 20
negative_answer_count_training = 50
learning_rate = 1.1
loss_margin = 0.5
training_epochs = 25
#'''


'''
# Best for biLSTM

k = 1
word_embedding_size = 300
word_embedding_window = 3
convolutional_filters = 282
batch_size = 20
negative_answer_count_training = 40
learning_rate = 1.1
loss_margin = 0.1
training_epochs = 25
#'''


'''
# Best for AP-CNN

k = 4
word_embedding_size = 300
word_embedding_window = 5
convolutional_filters = 400
batch_size = 20
negative_answer_count_training = 50
learning_rate = 1.1
loss_margin = 0.5
training_epochs = 25
'''


'''
# Best for AP-biLSTM

k = 1
word_embedding_size = 300
word_embedding_window = 3
convolutional_filters = 400
batch_size = 15
negative_answer_count_training = 50
learning_rate = 1.1
loss_margin = 0.2
training_epochs = 25
'''


################################################################################
### LAUNCH NETWORK
################################################################################

launch_train_test(network_type, dataset_name, model_type, use_cuda, k, word_embedding_size, word_embedding_window, convolutional_filters, batch_size, negative_answer_count_training, learning_rate, loss_margin, training_epochs, silent_mode=False, validate=True)
