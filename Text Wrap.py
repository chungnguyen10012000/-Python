import textwrap

def wrap(string, max_width):
    _string = textwrap.wrap(string,max_width) #creare list
    _string = "\n".join(_string) # conver list to string
    return _string

if __name__ == '__main__':
    result = wrap("A B C D E F G H I K L M",3)
    print(result)