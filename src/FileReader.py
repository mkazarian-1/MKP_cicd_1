class FileReader:
    def read(self, filename):
        try:
            with open(filename, 'r') as file:
                data = file.read()
            return data
        except Exception as e:
            raise Exception("Can't open file" + str(e))
