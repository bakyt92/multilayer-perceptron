import sys

class Train_class:
    def __init__(self, data_training, data_validation):
        self.training_set = data_training
        self.validation_set = data_validation
        self.X_train = []
        self.Y_train = []

    def process_data(self):
        try:
            X_train = []
            Y_train = []
            for row in self.training_set:
                row_float = [float(item) for item in row[2:]] 
                X_train.append(row_float)
                if row[1] == 'B':
                    Y_train.append(0)
                else:
                    Y_train.append(1)
            self.X_train = X_train
            self.Y_train = Y_train
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
    
    def ft_recalc(self, columns, means, std_devs):
        new_columns = []
        for column, mean, std_dev in zip(columns, means, std_devs):
            new_column = [(value - mean) / std_dev for value in column]
            new_columns.append(new_column)
        self.X_train = list(zip(*new_columns))
            

    def data_normalization(self):
        try:
            columns = list(zip(*self.X_train))
            means = [sum (column) / len(column) for column in columns]
            std_devs = self.ft_std(columns, means)
            array_new = self.ft_recalc(columns, means, std_devs)
        except Exception as e:
            print(f"Exception for processing data: {e}")
        return
            
        

