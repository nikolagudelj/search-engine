import sys
from os import path


class Config(object):
    @staticmethod
    def print_ranks(ranks):
        """
            Comment missing.
        """
        i = len(ranks) - 1
        rem = len(ranks)
        print("Number of pages in result set: " + str(rem))
        num_of_pages = 0
        while True:
            try:
                num_of_pages = int(input("Enter the number of pages you would like to display: "))
                break
            except Exception:
                print("Please enter an integer!")

        while num_of_pages > 0:
            if num_of_pages > rem:
                num_of_pages = rem
            if num_of_pages == 0:
                break
            print(str(num_of_pages) + " pages showing")
            for j in range(0, num_of_pages):
                print(ranks[i][0] + " " + str(ranks[i][1]))
                i -= 1
            rem -= num_of_pages
            print(str(rem) + " pages left")
            if rem > 0:
                while True:
                    try:
                        num_of_pages = int(input("Enter the number of pages you would like to display (0 for exit): "))
                        break
                    except Exception:
                        print("Please enter an integer!")
            else:
                break
        print("Finished displaying pages.")

    @staticmethod
    def inputPath():
        """
            Asks the user for a string-input path to the selected '.html' files directory.
            For every input, checks whether the specified folder exists. If not, it asks for input again.
            Returns a valid absolute path string.
        """
        while True:
            absolute_path = input("Enter the absolute path to your folder: ")
            sys.stdin.buffer.flush()
            if not path.exists(absolute_path):
                print("Path does not exist!")
            else:
                return absolute_path

    @staticmethod
    def removeTrailingOperators(query):
        """
            Prevents incorrect complex query input such as "! python && ||" by removing all the trailing operators
            after the last word token (works with infix form, so operators that are not between 2 words, are not valid)
            For input the above-mentioned input, returns "! python", incorrect operators are
        """
        last_word_index = -1
        for index in range(0, query.__len__()):
            if not Config.isOperator(query[index]):
                last_word_index = index
        if last_word_index == -1: return ""

        return query[:last_word_index+1]

    @staticmethod
    def isOperator(char):
        """ Checks whether a character is one of the following: ! & ! ( ) \\s  """
        return char in ['|', '&', '!', ' ']

    @staticmethod
    def isGreater(num, limit):
        """ Checks whether the first integer argument is greater than the second. Returns boolean value. """
        if num > limit: return True
        return False

    @staticmethod
    def removeNones(array):
        index = 0
        for i in array:
            if i is None:
                array.pop(index)
            index += 1
