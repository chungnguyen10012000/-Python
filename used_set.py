#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def newList(value , ls):
	return [x for x in ls if x != value]
def sockMerchant(n, ar):
    return sum([ar.count(i)//2 for i in set(ar)]) #set tra ve tung thanh phan le khac nhau tron list

def main():
    n = 20
    ar = [4 ,5, 5 ,5, 6, 6 ,4, 1 ,4 ,4, 3, 6, 6 ,3 ,6 ,1 ,4 ,5 ,5 ,5]
    result = sockMerchant(n, ar)
    print(result)
if __name__ == '__main__':
	main()

   
