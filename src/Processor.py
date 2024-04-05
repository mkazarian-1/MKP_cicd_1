import re


class Processor:
    def count_division(self, text, delimiters, sentence_endings):

        # Split the text into words using the specified delimiters
        words = re.split(f"[{''.join(delimiters)}]+", text)

        # Split the text into sentences using the specified sentence endings as delimiters
        sentences = re.split(f"[{''.join(sentence_endings)}]+", text)

        # Remove empty strings resulting from splitting
        words = [word for word in words if word.strip()]
        sentences = [sentence for sentence in sentences if sentence.strip()]

        return len(words), len(sentences)
