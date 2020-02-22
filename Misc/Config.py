import sys
from msvcrt import kbhit, getch
from os import path


class Config(object):
    @staticmethod
    def print_ranks(ranks):
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
        while True:
            absolute_path = input("Enter the absolute path to your folder: ")
            sys.stdin.buffer.flush()
            if not path.exists(absolute_path):
                print("Path does not exist!")
            else:
                return absolute_path

    @staticmethod
    def removeTrailingOperators(query):
        last_word_index = -1
        for index in range(0, query.__len__()):
            if not Config.isOperator(query[index]):
                last_word_index = index
        if last_word_index == -1: return ""

        return query[:last_word_index+1]

    @staticmethod
    def isOperator(char):
        return char in ['|', '&', '!', '(', ')', ' ']

    @staticmethod
    def isGreater(num, limit):
        if num > limit: return True
        return False
