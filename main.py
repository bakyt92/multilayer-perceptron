import sys
import argparse
from parser.parser import Parser

def main():
	pars = argparse.ArgumentParser(description='Multilayer perceptron')
	pars.add_argument("filename", help="Enter name of file")
	args = pars.parse_args()
	try:
		if args.filename:
			Reader = Parser()
			Reader.read_csv(args.filename)
		else: 
			raise FileNotFoundError("File does not exist")
	except Exception as e:
		print(f"Exception in main: {e}")
		sys.exit(1)

if __name__ == '__main__':
	main()
