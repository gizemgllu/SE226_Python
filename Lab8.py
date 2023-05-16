from abc import ABC

#Question1

class AbstractClass(ABC):
    address=" "
    def __init__(self,address):
        self.address=address

    def calculateFreqs(self):
        pass

#Question2 and 3
class ListCount(AbstractClass):

    def calculateFreqs(self):
        frequencies={}
        with open(self.address, 'r') as f:
            content= f.read()
            for char in content:
                if char.isalpha():
                    char = char.lower()
                    if char in frequencies:
                        frequencies[char] += 1
                    else:
                        frequencies[char] = 1
        freq_list = [(char, count) for char, count in frequencies.items()]
        print(freq_list)


#Question2 and 4
class DictCount(AbstractClass):
    def calculateFreqs(self):
        frequencies = {}

        with open(self.address, 'r') as f:
            text = f.read()
            for char in text:
                if char.isalpha():
                    if char in frequencies:
                        frequencies[char] += 1
                    else:
                        frequencies[char] = 1

        for char, freq in frequencies.items():
            frequencies[char] = freq

        print("Updated Dict is: ", frequencies)



#Question5

x = ListCount("/Users/gizemgullu/Downloads/weirdWords.txt")
x.calculateFreqs()

y = DictCount("/Users/gizemgullu/Downloads/weirdWords.txt")
y.calculateFreqs()
