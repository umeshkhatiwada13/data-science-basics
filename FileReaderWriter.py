# define imports
import pandas as pd


# define classname
class FileReaderWriter:

    @staticmethod
    def read_file():
        df = pd.read_csv(
            "https://raw.githubusercontent.com/umeshkhatiwada13/Datasets/main/healthcare-dataset-stroke-data_5k.csv")
        print("File read successful")
        return df
