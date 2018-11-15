#!/usr/bin/env python3

## TO TRY A LOT OF PARAMETERS COMBINATIONS

import argparse
from launch import launch_train_test
import time

################################################################################
### HYPERPARAMETERS
################################################################################

k_values = [5]
word_embedding_size = 300
word_embedding_window = 5
convolutional_filters_values = [400]
batch_size_values = [5,10]
negative_answer_count_training_values = [20, 50]
learning_rate_values = [0.01, 0.05, 0.1, 1.0]
loss_margin_values = [0.5, 0.2, 0.05, 0.01]
training_epochs_values = [25]

network_type = 'AP-CNN'
dataset_name = 'TrecQA'
model_type = 'GoogleRed'
use_cuda = True


################################################################################
### LAUNCH NETWORK TESTS
################################################################################

for k in k_values:
    for convolutional_filters in convolutional_filters_values:
        for batch_size in batch_size_values:
            for negative_answer_count_training in negative_answer_count_training_values:
                for learning_rate in learning_rate_values:
                    for loss_margin in loss_margin_values:
                        for training_epochs in training_epochs_values:
                            try:
                                starting_time = time.time()
                                res = launch_train_test(network_type,
                                    dataset_name,
                                    model_type,
                                    use_cuda,
                                    k,
                                    word_embedding_size,
                                    word_embedding_window,
                                    convolutional_filters,
                                    batch_size,
                                    negative_answer_count_training,
                                    learning_rate,
                                    loss_margin,
                                    training_epochs,
                                    silent_mode=True,
                                    validate=False)
                                print('Round - ( k:%d, batch_size: %d, learning_rate: %1.3f, loss_margin: %1.3f, training_epochs: %d ) -> ( MRR: %1.3f, MAP: %1.3f, time: %ds)' % (k, batch_size, learning_rate, loss_margin, training_epochs, *res, time.time()-starting_time))
                            except:

                                print('Round - ( k:%d, batch_size: %d, learning_rate: %1.3f, loss_margin: %1.3f, training_epochs: %d ) -> CUDA_ERROR' % (k, batch_size, learning_rate, loss_margin, training_epochs))
