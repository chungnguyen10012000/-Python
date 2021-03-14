import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    len_string = len(s)
    len_a = s.count('a')
    step = int(n/len_string)
    total = len_string * step
    result = len_a*step
    for x in range(0,n-total):
        if s[x] == 'a':
            result += 1
    return result



if __name__ == '__main__':
    s = 'aba'

    n = 10

    result = repeatedString(s, n)

    print(result)
