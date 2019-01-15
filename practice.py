import csv
import numpy


f = open("C:/python/Projects/numpy/nyc_taxis.csv",'r')
data_read = csv.reader(f)
data = list(data_read)

print(data)




class Dataset:
    def __init__(self,lst):
        f = open(lst,'r')
        data_read = csv.reader(f)
        rows = list(data_read)
        self.data = rows[1:]

    def convert_float(self):
        converted_data = []
        for row in self.data:
            for item in row:
                converted_data.append(float(item))
        return converted_data        




data = Dataset("C:/python/Projects/numpy/nyc_taxis.csv")

print(data.convert_float())

tax
