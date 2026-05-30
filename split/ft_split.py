import sys
import random

class Split_Class:
    def __init__(self):
        self.input_data = []
        self.training_set = []
        self.validation_set = []
    

    def ft_split(self, data, ratio, v_seed=4):
        try:
            self.input_data = data
            malignant = [row for row in data if row[1] == 'M']
            benign = [row for row in data if row[1] == 'B']
            random.seed(v_seed)
            random.shuffle(malignant)
            random.shuffle(benign)
            split_index_b = int(ratio * len(benign))
            split_index_m = int(ratio * len(malignant))
            self.training_set = malignant[:split_index_m] + benign[:split_index_b]
            self.validation_set = malignant[split_index_m:] + benign[split_index_b:]
            print(f"FT Split results:")
            print(f"Training set lines:{len(self.training_set)}")
            print(f"Validation set lines:{len(self.validation_set)}")
        except Exception as e:
            print(f"Error during split: {e}")
            sys.exit(1)
        return
    
    def export(self, Training_file="training.csv", Validation_file="validation.csv"):
        try:
            with open(Training_file, "w") as file1:
                for row in self.training_set:
                    file1.write(",".join(row) + "\n")
            with open(Validation_file, "w") as file1:
                for row in self.validation_set:
                    file1.write(",".join(row) + "\n")
        except Exception as e:
            print(f"Exception for writing file {e}")
            sys.exit(1)
        return


    def get_data(self):
        if self.training_set and self.validation_set:
            return self.training_set, self.validation_set
        else:
            return None