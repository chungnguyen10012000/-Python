def count_substring1(string, sub_string):
    _size_string = len(string)
    _size_sub_string = len(sub_string)
    _count = 0
    for x in range(0,_size_string):
        if string[x:x+_size_sub_string] == sub_string :
          	_count = _count + 1
    return _count

def count_substring2(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string): # dung de tim kiem tu vi tri i den cuoi xem co chuoi bat dau bang sub_string hay khong
            count += 1
    return count

if __name__ == '__main__':
    string = 'ThIsisCoNfUsInG'
    sub_string = 'is'   
    count = count_substring2(string, sub_string)
    print(count)