from functools import reduce
def solution(x,y,z,n):
    return [[i,j,k] for i in range (0,x+1) for j in range (0,y+1) for k in range (0,z+1) if (i+j+k)!=n]
def solution1(x,y,z,n):
    return reduce(lambda x ,y : [x + y] , [])
def main():
    print(solution(1,1,2,3))
if __name__ == '__main__':
    main()

