from src import FileReader, FileWriter, Processor

READ_PATH = 'resources/read.txt'
WRITE_PATH = 'resources/write.txt'
WORD_DELIMITERS = [",", " ", ":", ";"]
SENTENCE_DELIMITERS = [".", "!", "?", "..."]

if __name__ == '__main__':
    fileReader = FileReader.FileReader()
    fileWriter = FileWriter.FileWriter()
    processor = Processor.Processor()

    words_amount,sentence_amount = processor.count_division(fileReader.read(READ_PATH), WORD_DELIMITERS,
                                                            SENTENCE_DELIMITERS)

    report = "Words amount:" + str(words_amount) + "\nSentence amount:" + str(sentence_amount)

    fileWriter.write(WRITE_PATH, report)
