import sys

class Parser:
	def __init__(self):
		headers = []
		data = []

	def read_csv(self, link_file):
		array = []
		try:
			with open(link_file, "r") as file:
				for line in file:
					line = line.strip()
					tmp = line.split()
					array.append(line)
		except Exception as e:
			print (f"Error in reading file: {e}")