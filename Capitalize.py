def solve1(s):
    s = s.split(" ")
    lst = []
    for x in s:
        lst.append(x.capitalize())
    string = " ".join(lst)
    return string

def solve2(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s
if __name__ == '__main__':

    s = 'chung nguyen'

    result = solve2(s)
    print(s[:])

    print(result)

