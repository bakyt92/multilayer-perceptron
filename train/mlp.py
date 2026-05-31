import sys

class MLP_Class:
    def __init__(self):
        self.weights = []
        self.biases = []
        self.layer_sizes = []
        self.learning_rate = 0
        self.epochs = 0
    
    def input(self, X_train_norm, training_labels, l_sizes, epochs=100, learning_rate=0.01):
        