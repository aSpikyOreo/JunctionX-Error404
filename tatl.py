# Recommend different strategies and steps to recovery

# Input: Given text response
# Data: words

# Set of items i.e: Feelings
# Set of users i.e: People

# Predicted feelings vs Actual feelings
# "How are you feeling?"
# predicted: guessing the user's feelings and thoughts based off texting styles
# actual: actions performed after querying the user & getting a response

# Learning Process: How does the chatbot predict and adjust to user's texting style?

# Classifiying and categorising text -> Phase One
# Deriving a mood from the categorised text -> Phase Two

# Separate from hard and soft categories:
	# Hard categories: Depression, Anxiety, Autism, PTSD, ADHD
	# Soft categories: Stress, Imposter Syndrome, Family, School,


# Moods:
# Happy
# Sad
# Anxious
# Depressed
# Excited
# Tired
# Angry
# Productive
# Bored
# Stressed
# Content

# if (HAPPY_LIST): +0.25 (good)
# if (SAD_LIST): -0.25 (sad)
# else: 0 (neutral)


# Per use: Classification
# Tracking, Learning and Optimisation: Sentiment Analysis




#################################T  A   T  L      .PY  ####################################################
import time
from multiprocessing import cpu_count
from typing import Union, NamedTuple
import torch
import torch.backends.cudnn
from torch import nn, optim
from torch.nn import functional as F
from torch.utils import data
from torch.optim.optimizer import Optimizer
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
import torchvision.datasets
from torchvision import transforms
from dataset import UrbanSound8KDataset
import numpy as np
import argparse
from pathlib import Path
import sklearn
from sklearn.metrics import confusion_matrix

from torchsummary import summary




### ~> Create the tensor datasets required alongside dataloaders


### ~> Shuffle data_aug_pad


### ~> Obtain a BATCH of training data


### ~> Define LSTM architecture


### ~> Define the Model class


### ~> TRAINING


### ~> TESTING & VALIDATION SET


### ~> a) Test Data
#
#
#
### ~> b) On user-generated data
#
#
### i.e: Tokenizing for pre-processing and predictions that illustrate output
###      after user review 
