import sys
import random
import math
class MLP_Class:
	def __init__(self):
		self.weights = []
		self.biases = []
		self.layer_sizes = []
		self.learning_rate = 0
		self.epochs = 0
		self.z_layers_data = []
		self.a_layers_data = []

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

	def ft_calculation(self, a_prev):
		self.z_layers_data = []
		self.a_layers_data = []
		for layer_index, layer in enumerate(self.weights):
			z_layer = []
			a_layer = []
			for i, row in enumerate(layer):
				sum_tmp = 0
				for index, elem in enumerate(row):
					sum_tmp += elem * a_prev[index]
				z_layer.append(sum_tmp + self.biases[layer_index][i])
			if layer_index == len(self.weights) - 1:
				exp_z = [math.exp(z_k) for z_k in z_layer]
				sum_exp = sum(exp_z)
				a_layer = [e_k / sum_exp for e_k in exp_z]
			else:
				a_layer = [x if x > 0 else 0 for x in z_layer]
			a_prev = a_layer
			self.z_layers_data.append(z_layer)
			self.a_layers_data.append(a_layer)
		return a_layer

	def ft_loss_func(self, a_layer, labels):
		l = 0
		l = - (labels[0] * math.log(a_layer[0] + 1e-15) + labels[1] * math.log(a_layer[1] + 1e-15))
		return l

	def ft_backprop(self, x, y, delta_out):
		num_layers = len(self.weights)
		deltas = [None] * num_layers
		deltas[-1] = delta_out
		layer_index = num_layers - 2
		while (layer_index >= 0):
			W_next = self.weights[layer_index + 1]
			delta_next = deltas[layer_index + 1]
			deltas[layer_index] = []
			z_layer = self.z_layers_data[layer_index]
			j_index = 0
			while j_index < len(W_next[0]):
				sum_j = 0
				k_index = 0
				while k_index < len(W_next):
					s_j = (W_next[k_index][j_index] * delta_next[k_index])
					sum_j += s_j
					k_index += 1
				if z_layer[j_index] > 0:
					delta_j = sum_j
				else:
					delta_j = 0
				deltas[layer_index].append(delta_j)
				j_index += 1
			layer_index -= 1
		for layer_index in range(num_layers):
			delta_l = deltas[layer_index]
			if layer_index == 0:
				a_prev = x
			else:
				a_prev = self.a_layers_data[layer_index - 1]
			for j in range(len(self.weights[layer_index])):
				for i in range(len(self.weights[layer_index][0])):
					dW_j_i = delta_l[j] * a_prev[i]
					self.weights[layer_index][j][i] -= self.learning_rate * dW_j_i
				db_j = delta_l[j]
				self.biases[layer_index][j] -= self.learning_rate * db_j

	def ft_save_to_file(self, train_means, train_stds):
		model_data = {
			"layer_sizes" : self.layer_sizes,
			"weights": self.weights,
			"biases": self.biases,
			"means": train_means,
			"stds": train_stds
		}
		with open ("save_data.json", "w") as file:
			file.write(model_data)
		print(f"File save_data.json is saved")
