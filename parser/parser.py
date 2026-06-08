import sys

class Parser:
	def __init__(self):
		self.data = []

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
					if len(tmp) < 1 or size != len(tmp):
						tmp.clear()
						print(f"This line is skipped (non-consistent by length / empty line): {line}.")
						continue
					array.append(tmp)
				self.data = array
		except Exception as e:
			print (f"Error in reading file: {e}")


	def ft_data_shape(self):
		try:
			print(f"Overview of dataset.")
			print(f"Total rows: {len(self.data)}")
			print(f"Total columns: {len(self.data[0])}")
			malignant_q = sum(1 for row in self.data if row[1] == 'M')
			benign_q = sum(1 for row in self.data if row[1] == 'B')
			print(f"Lines with malignant result: {malignant_q}")
			print(f"Lines with benign result: {benign_q}")
		except Exception as e:
			print(f"Error while learning data shape: {e}")
			sys.exit(1)
		return

	def ft_clean_data(self):
		try:
			print(f"Before cleaning data:")
			self.ft_data_shape()
			clean_data = [row for row in self.data if row.count('0') < 2
				 and len(row) == len(self.data[0])]
			self.data = clean_data
			print(f"After cleaning data:")
			self.ft_data_shape()
		except Exception as e:
			print(f"Error while learning data shape: {e}")
			sys.exit(1)
		return

	def get_data(self):
		if self.data:
			return self.data
		else:
			return None
