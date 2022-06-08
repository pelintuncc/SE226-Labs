from abc import ABC


class Count(ABC):
    def __init__(self, address):
        self.address = address

    def calculateFreqs(self, address):
        pass


class ListCount(Count):
    def __init__(self, address):
        Count.__init__(self, address)

    def calculateFreqs(self, address):
        file = open(address)
        x = file.readline().split()
        my_list = []
        for i in x:
            if i not in my_list:
                my_list.append(i)
        for i in range(0, len(my_list)):
            print("Frequency of ", my_list[i], "is :", x.count(my_list[i]))


class DictCount(Count):
    def __init__(self, address):
        Count.__init__(self, address)

    def calculateFreqs(self, address):
        file = open(address)
        x = file.readline()
        my_dictionary = {}
        for word in x.split():
            my_dictionary[word] = my_dictionary.get(word, 0) + 1
        for key in my_dictionary:
            print("{} : {}".format(key, my_dictionary[key]))


address1 = "/Users/pelintunc/Desktop/strange.txt"

file1 = ListCount(address1)
file1.calculateFreqs(address1)

file2 = DictCount(address1)
file2.calculateFreqs(address1)
