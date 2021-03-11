def find_second(lst):
    ls = [x for x in set(lst)]
    _max = max(ls)
    ls.remove(_max)
    new_lst = ls
    _result = max(new_lst)
    return _result
def main():
    ar = [2,2,6,6,5]
    n = 5
    kq = find_second(ar)
    print(kq)
if __name__ == '__main__':
    main()
