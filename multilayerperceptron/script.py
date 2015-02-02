import os
import pylearn2
#will setup paths and open files
path = os.path.join(pylearn2.__path__[0], 'scripts', 'tutorials', 'multilayer_perceptron', 'mlp_tutorial_part_2.yaml')
with open(path, 'r') as f:
    train = f.read()
hyper_params = {'train_stop' : 50000,
                'valid_stop' : 60000,
                'dim_h0' : 500,
                'max_epochs' : 10000,
                'save_path' : '.'}
#setup params for training
train = train % (hyper_params)
#print train


#the following trains our model
from pylearn2.config import yaml_parse
train = yaml_parse.load(train)
#train.main_loop()

#The following code adds another layer and changes it from Sigmoid to rectified linear
path = os.path.join(pylearn2.__path__[0], 'scripts', 'tutorials', 'multilayer_perceptron', 'mlp_tutorial_part_3.yaml')
with open(path, 'r') as f:
    train_2 = f.read()
hyper_params = {'train_stop' : 50000,
                'valid_stop' : 60000,
                'dim_h0' : 500,
                'dim_h1' : 1000,
                'sparse_init_h1' : 15,
                'max_epochs' : 10000,
                'save_path' : '.'}
train_2 = train_2 % (hyper_params)
print train_2
#trains it
from pylearn2.config import yaml_parse
train_2 = yaml_parse.load(train_2)
#train_2.main_loop()

#In here, we deal with the overfitting problem by using a baseyan inference approach
path = os.path.join(pylearn2.__path__[0], 'scripts', 'tutorials', 'multilayer_perceptron', 'mlp_tutorial_part_4.yaml')
with open(path, 'r') as f:
    train_3 = f.read()
hyper_params = {'train_stop' : 50000,
                'valid_stop' : 60000,
                'dim_h0' : 500,
                'dim_h1' : 1000,
                'sparse_init_h1' : 15,
                'max_epochs' : 10000,
                'save_path' : '.'}
train_3 = train_3 % (hyper_params)
print train_3
#trains
from pylearn2.config import yaml_parse
train_3 = yaml_parse.load(train_3)
train_3.main_loop()


