from FileReaderWriter import FileReaderWriter


class PreProcessing:
    def __init__(self):
        self.data = FileReaderWriter.read_file()

    def define_dataset(self):
        print("First 5 rows ", self.data.head(5))
