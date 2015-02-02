import os
import pylearn2
dirname = os.path.abspath(os.path.dirname('softmax_regression.ipynb'))

#Right here, we load our dataset about to be used
with open(os.path.join(dirname, 'sr_dataset.yaml'), 'r') as f:
    dataset = f.read()
hyper_params = {'train_stop' : 50000}
dataset = dataset % (hyper_params)
#print dataset

#opens the model that gives info for the incoming training we will do
with open(os.path.join(dirname, 'sr_model.yaml'), 'r') as f:
    model = f.read()
#print model    

#opens our training algorithm and gives it a few parameters
with open(os.path.join(dirname, 'sr_algorithm.yaml'), 'r') as f:
    algorithm = f.read()
hyper_params = {'batch_size' : 10000,
                'valid_stop' : 60000}
algorithm = algorithm % (hyper_params)
#print algorithm

# now it runs training
with open(os.path.join(dirname, 'sr_train.yaml'), 'r') as f:
    train = f.read()
save_path = '.'
train = train %locals()
print train
#starts the actual training part
from pylearn2.config import yaml_parse
train = yaml_parse.load(train)
train.main_loop().


#to analyze it you have to go to where the following scripts are stores
#and run
# python print_monitor.py softmax_regression.pkl
#or
#!show_weights.py softmax_regression_best.pkl


