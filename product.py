from itertools import product

def func1(lst1 , lst2):
    print (list(product(lst1,lst2)))
if __name__ == '__main__':
    s1 = input('Nhap list 1 :')
    s2 = input('Nhap list 2: ')
    s1 = s1.split(" ")
    s2 = s2.split(" ")
    print(s1)
    print(s2)
    func1(s1,s2)