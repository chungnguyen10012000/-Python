def mutate_string(string, position, character):
    lst = list(string)
    lst[position] = character
    lst = "".join(lst)
    return lst
def mutate_string2(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

if __name__ == '__main__':
    s_new = mutate_string2('abracadabra', int(5), 'k')
    print(s_new)