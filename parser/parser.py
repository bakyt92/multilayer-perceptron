import sys

class Parser:
	def __init__(self):
		data = []

	def read_csv(self, link_file):
		array = []
		try:
			with open(link_file, "r") as file:
				first_line = file.readline()
				first_line = first_line.split(",")
				size = len(first_line)
				for line in file:
					line = line.strip()
					tmp = line.split(",")
					if len(tmp) < 1 or size != tmp(len):
						tmp.clear()
						print(f"This line is skipped (non-consistent by length / empty line): {line}.")
						continue
					array.append(tmp)
				self.data = array
		except Exception as e:
			print (f"Error in reading file: {e}")

	def get_data(self):
		if self.data:
			return self.data
		else:
			return None