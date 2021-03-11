def main():
    lst = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    students = []
    second_high = sorted(set([i[1] for i in lst]))[1]
    print("\n".join(sorted([i[0] for i in lst if i[1] == second_high])))
    
if __name__ == '__main__':
    main()