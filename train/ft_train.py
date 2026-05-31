import sys

class Train_class:
    def __init__(self):
        self.means_training = []
        self.stds_training = []

    def process_data(self, data):
        try:
            dataset = []
            labels = []
            for row in data:
                row_float = [float(item) for item in row[2:]] 
                dataset.append(row_float)
                if row[1] == 'B':
                    labels.append([1, 0])
                else:
                    labels.append([0, 1])
        except Exception as e:
            print(f"Exception for processing data: {e}")
        return dataset, labels
    
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
        return list(zip(*new_columns))
    
    def validation_normalisation(self, data):
        try:
            columns = list(zip(*data))
            means = self.means_training
            std_devs = self.stds_training
            array_new = self.ft_recalc(columns, means, std_devs)
        except Exception as e:
            print(f"Exception for processing data: {e}")
        self.means_training = means
        self.stds_training = std_devs
        return array_new

    def data_normalization(self, data):
        try:
            columns = list(zip(*data))
            means = [sum (column) / len(column) for column in columns]
            std_devs = self.ft_std(columns, means)
            array_new = self.ft_recalc(columns, means, std_devs)
        except Exception as e:
            print(f"Exception for processing data: {e}")
        self.means_training = means
        self.stds_training = std_devs
        return array_new
    
    def get_means(self):
        return self.means_training
    
    def get_std(self):
        return self.stds_training
            
        

