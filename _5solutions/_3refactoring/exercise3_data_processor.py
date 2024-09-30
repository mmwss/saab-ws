class DataProcessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.data = []
        self.processed_data = []

    def read_data(self):
        with open(self.input_file, 'r') as f:
            for line in f:
                fields = line.strip().split(',')
                self.data.append(fields)

    def process_data(self):
        for item in self.data:
            # Some complex processing
            processed_item = [field.upper() for field in item]
            self.processed_data.append(processed_item)

    def write_data(self):
        with open(self.output_file, 'w') as f:
            for item in self.processed_data:
                line = ','.join(item)
                f.write(line + '\n')

    def process(self):
        self.read_data()
        self.process_data()
        self.write_data()

# Example usage
if __name__ == "__main__":
    input_file = 'data/input.csv'
    output_file = 'data/output.csv'
    processor = DataProcessor(input_file, output_file)
    processor.process()
