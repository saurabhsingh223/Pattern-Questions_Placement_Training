n = int(input())
m = int(input())

for i in range(n):
    if n > 2:
        if i == 0 or i == (n-1):
            print('*'*n)
        else:
            print('*'+' '*(m-2)+'*')
    else:
        print('*'*m)