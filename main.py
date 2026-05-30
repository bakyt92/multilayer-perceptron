import sys
import argparse
from parser.parser import Parser

def main():
	pars = argparse.ArgumentParser(description="Multilayer perceptron program")
	subparsers = pars.add_subparsers(dest="command", required=True)
	train_parser = subparsers.add_parser("train", help="Train model")
	predict_parser = subparsers.add_parser("predict", help="Predict result")
	split_parser = subparsers.add_parser("split", help="Split data to 2 datasets")
	train_parser.add_argument("data_file", help="input resource file", required=True)
	split_parser.add_argument("data_file", help="input resource file", required=True)
	split_parser.add_argument("training_file", help="output file for training", required=True)
	split_parser.add_argument("validation_file", help="output file for validation", required=True)
	predict_parser.add_argument("training_file", help="input file for training", required=True)
	predict_parser.add_argument("validation_file", help="input file for validation", required=True)
	args = pars.parse_args()
	try:
		if args.command == "train":
			Reader = Parser()
			Reader.read_csv(args.data_file)
			data = Reader.get_data()
		elif args.command == "split":
			Reader = Parser()
			Reader.read_csv(args.data_file)
			data = Reader.get_data()
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
