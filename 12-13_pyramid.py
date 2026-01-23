n = int(input())
def pyramid(n):
    for i in range(n):
        print(' '*(n-i)+'*'*(2*i+1))

def invertedPyramid(n):
    for i in range(n):
        print(' '*(i)+'*'*(2*n-2*i-1))
invertedPyramid(n)