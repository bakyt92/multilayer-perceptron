import sys

class Parser:
	def __init__(self):
		headers = []
		data = []

	def read_csv(self, link_file):
		try:
			with open(link_file, "r") as file:
				
