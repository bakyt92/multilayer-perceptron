import sys
import argparse
from parser.parser import Parser
from split.ft_split import Split_Class
from train.ft_train import Train_class

def main():
	pars = argparse.ArgumentParser(description="Multilayer perceptron program")
	subparsers = pars.add_subparsers(dest="command", required=True)
	train_parser = subparsers.add_parser("train", help="Train model")
	predict_parser = subparsers.add_parser("predict", help="Predict result")
	split_parser = subparsers.add_parser("split", help="Split data to 2 datasets")
	train_parser.add_argument("training_file", help="input resource train file")
	train_parser.add_argument("validation_file", help="input resource validation file")
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
			data_training, training_labels = Trainer.process_data(data_training)
			X_train_norm = Trainer.data_normalization(data_training)
			means_training = Trainer.get_means()
			stds_training = Trainer.stds_training()
			data_validation, validation_labels = Trainer.process_data(data_validation)
			Y_train_norm = Trainer.validation_normalisation(data_validation)

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
