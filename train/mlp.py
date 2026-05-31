import sys
import random

class MLP_Class:
    def __init__(self):
        self.weights = []
        self.biases = []
        self.layer_sizes = []
        self.learning_rate = 0
        self.epochs = 0
    
    def create_layer(self, n_in, n_out):
        if n_in < 1 or n_out < 1:
            return None
        W = []
        for row in range(n_out):
            row = []
            for elem in range(n_in):
                row.append(random.random() - 0.5)
            W.append(row)
        print(f"New Layer is created")
        print(f"rows: {len(W)}, columns: {len(W[0])}")
        return W

    def input(self, X_train_norm, training_labels, l_sizes, epochs, learning_rate):
        self.learning_rate = learning_rate
        self.epochs = epochs
        output_size = 2
        input_size = len(X_train_norm[0])
        self.layer_sizes = [input_size] + l_sizes + [output_size]
        for index, size in enumerate(self.layer_sizes[1:], start=1):
            self.weights.append(self.create_layer(self.layer_sizes[index - 1], size))
            self.biases.append(size * [0])
        return 
    
    def ft_activation(self):
        

    def ft_calculation(self, a_prev):
        z = []
        for layer in self.weights:
            for row in layer:
                for index, elem in enumerate(row):
                    z = elem * a_prev[index]
