def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line = "\n".join(line)
    return line

if __name__ == '__main__':
    result = split_and_join('this is a string')
    print(result)