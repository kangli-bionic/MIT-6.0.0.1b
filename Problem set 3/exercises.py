'''
Return standard deviation of a list of lengths of strings
'''

import math

def stdDevOfLengths(L):
    string_lengths = [len(s) for s in L]
    mean = sum(string_lengths) / len(string_lengths)

    cumm = 0

    for s in string_lengths:
        cumm += (s - mean)**2

    variance = cumm / len(string_lengths)
    std_dev = math.sqrt(variance)

    return std_dev

print(stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples']))

