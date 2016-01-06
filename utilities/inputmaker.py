import random
import sys

def create_array(size):
    result = []
    while size > 0:
        element = random.randrange(size * 5)
        result.append(element)

        size -= 1
    return result

def save(data, filename):
    separator = ''
    with open(filename, 'w') as outputfile:
        for i in data:
            outputfile.write(separator + str(i))
            if separator == '':
                separator = ' '

def load(filename):
    with open(filename, 'r') as inputfile:
        result = inputfile.read().split(' ')
    print(result)
