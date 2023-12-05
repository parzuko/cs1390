
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import pickle

def NB_XGivenY(XTrain, yTrain, a=0.001, b=0.9):
    """
    Compute the probability of P(X|Y).

    :param
        XTrain: numpy array of size [num_samples, feat_dim]
          where num_samples is the number of samples
          and feat_dim is the dimension of features
        yTrain: numpy array of size [num_samples, 1]
        a: default to 0.001
        b: default to 0.9

    :return: 
        D: numpy array of size [2, vocab_size] where
          vocab_size is the size of vocabulary
    """
    raise NotImplementedError
    return D


def NB_YPrior(yTrain):
    """
    Compute the probability of P(Y).

    :param
        yTrain: numpy array of size [num_samples, 1]

    :return: 
        p: a scalar for the probability of P(Y = 1)
    """
    raise NotImplementedError
    return p


def NB_Classify(D, p, X):
    """
    Predict the labels of X.

    :param
        D: the probability P(X|Y)
        p: the probability P(Y)
        X: numpy array of size [num_samples, feat_dim]
          where num_samples is the number of samples
          and feat_dim is the dimension of features

    :return: 
        y: numpy array of size [num_samples, 1] where
            num_samples is the number of samples
    """
    raise NotImplementedError
    return y


def NB_ClassificationAccuracy(yHat, yTruth):
    """
    Compute the accuracy of predictions.

    :param
        yHat: numpy array of size [num_samples, 1]
        yTruth: numpy array of size [num_samples, 1]
    
    :return:
        acc: a scalar for the accuracy
    """
    raise NotImplementedError
    return acc
