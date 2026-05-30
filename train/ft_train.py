import sys

class Train_class:
    def __init__(self, data_training, data_validation):
        self.training_set = data_training
        self.validation_set = data_validation
        self.input_layer = []
        self.results = []

    def process_data(self):
        try:
            input_layer = []
            results = []
            for row in self.training_set:
                row_float = [float(item) for item in row[2:]] 
                input_layer.append(row_float)
                if row[1] == 'B':
                    results.append(0)
                else:
                    results.append(1)
            self.input_layer = input_layer
            self.results = results
        except Exception as e:
            print(f"Exception for processing data: {e}")
        return
    
    def ft_std(self, columns, means):
        variances = []
        for column, mean in zip(columns, means):
            diffs = [(value - mean) ** 2 for value in column]
            variance = sum(diffs) / len(column)
            variances.append(variance) 
        std_devs = [value ** 0.5 for value in variances]
        return std_devs
            

    def data_normalization(self):
        try:
            columns = list(zip(*self.input_layer))
            means = [sum (x for x in columns) / len(columns)]
            self.ft_std(columns, means)
        except Exception as e:
            print(f"Exception for processing data: {e}")
        return
            
        

