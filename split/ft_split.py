import sys

class Split_Class:
    def __init__(self):
        self.input_data = []
        self.training_set = []
        self.validation_set = []
    

    def ft_split(self, data, ratio):
        try:
            self.input_data = data
            malignant = [row for row in data if row[1] == 'M']
            benign = [row for row in data if row[1] == 'B']
            split_index_b = int(ratio * len(benign))
            split_index_m = int(ratio * len(malignant))
            self.training_set = malignant[:split_index_m] + benign[:split_index_b]
            self.validation_set = malignant[split_index_m:] + benign[split_index_b:]
        except Exception as e:
            print(f"Error during split: {e}")
            sys.exit(1)
        return
    
    def get_data(self):
        if self.training_set and self.validation_set:
            return self.training_set, self.validation_set
        else:
            return None