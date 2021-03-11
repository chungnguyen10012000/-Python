def count_(s,lst):
    kq = 0
    for x in lst:
        for i in range(x+1,len(s)+1):
            kq = kq + sum(1 for j in range(len(s))  if s.startswith(s[x:i], j))
    return kq

def minion_game(string):
    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print ("Kevin", kevsc)
    elif kevsc < stusc:
        print ("Stuart", stusc)
    else:
        print ("Draw")

if __name__ == '__main__':
    s = 'BAANANAS'
    minion_game(s)