import sys
import argparse
from parser.parser import Parser
from split.ft_split import Split_Class
from train.ft_train import Train_class
from train.mlp import MLP_Class

def main():
	pars = argparse.ArgumentParser(description="Multilayer perceptron program")
	subparsers = pars.add_subparsers(dest="command", required=True)
	train_parser = subparsers.add_parser("train", help="Train model")
	predict_parser = subparsers.add_parser("predict", help="Predict result")
	split_parser = subparsers.add_parser("split", help="Split data to 2 datasets")
	train_parser.add_argument("training_file", help="input resource train file")
	train_parser.add_argument("validation_file", help="input resource validation file")
	train_parser.add_argument("--epochs", type=int, default=100, help="Number of epochs")
	train_parser.add_argument("--learning_rate", type=float, default=0.01,
						   help="Learning rate float value, e.g. --learning_rate 0.01")
	train_parser.add_argument("--hidden_layers", type=int, default=[24, 24], nargs='+',
						   help="Hidden layer sizes, e.g. --hidden_layers 24 24")
	train_parser.add_argument("--batch_size", type=int, default=50,
						   help="Batch sizes for each epoch, e.g. --batch_size 50")
	split_parser.add_argument("data_file", help="input resource file")
	split_parser.add_argument("training_file", help="output file for training")
	split_parser.add_argument("validation_file", help="output file for validation")
	split_parser.add_argument("--ratio", type=float, default=0.8,
                              help="Train ratio, e.g. 0.8 means 80% train and 20% validation")
	split_parser.add_argument("--seed", type=int, default=2, choices=range(0, 1000),
                              help="Random seed for reproducibility (0-999)")
	predict_parser.add_argument("training_file", help="input file for training")
	predict_parser.add_argument("validation_file", help="input file for validation")
	args = pars.parse_args()
	try:
		if args.command == "train":
			Reader = Parser()
			Reader.read_csv(args.training_file)
			data_training = Reader.get_data()
			Reader.read_csv(args.validation_file)
			data_validation = Reader.get_data()
			Trainer = Train_class()
			X_train_raw, training_labels = Trainer.process_data(data_training)
			X_train_norm = Trainer.data_normalization(X_train_raw)
			# means_training = Trainer.get_means()
			# stds_training = Trainer.stds_training()
			Y_train_raw, validation_labels = Trainer.process_data(data_validation)
			Y_train_norm = Trainer.validation_normalisation(Y_train_raw)
			MLP = MLP_Class()
			MLP.input(X_train_norm, training_labels, args.hidden_layers, args.epochs, args.learning_rate)
			sum_loss = 0
			for i, rows in enumerate(X_train_norm):
				p = MLP.ft_calculation(rows)
				loss = MLP.ft_loss_func(p, training_labels[i])
				sum_loss += loss
				delta_out = [p[0] - training_labels[i][0], p[1] - training_labels[i][1]]
				MLP.ft_backprop(p, training_labels[i], delta_out)
			average_loss = sum_loss / i
			# data_validation, validation_labels = Trainer.process_data(data_validation)
			# data_validation = Trainer.data_normalization(data_validation)
		elif args.command == "split":
			Reader = Parser()
			Reader.read_csv(args.data_file)
			Reader.ft_clean_data()
			data = Reader.get_data()
			Splitter = Split_Class()
			Splitter.export(args.training_file, args.validation_file)
			if args.ratio < 0 or args.ratio > 1:
				raise ValueError("Args Ratio is not in range from 0 to 1")
			Splitter.ft_split(data, args.ratio)
		elif args.command == "predict":
			Reader = Parser()
			Reader.read_csv(args.training_file)
			data_training = Reader.get_data()
			Reader.read_csv(args.validation_file)
			data_validation = Reader.get_data()
	except Exception as e:
		print(f"Exception in main: {e}")
		sys.exit(1)

if __name__ == '__main__':
	main()
