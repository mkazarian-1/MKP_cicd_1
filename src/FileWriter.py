class FileWriter:
    def write(self, filename, data):
        try:
            with open(filename, 'w') as file:
                file.write(data)
        except Exception as e:
            raise Exception("Can't open file" + str(e))
