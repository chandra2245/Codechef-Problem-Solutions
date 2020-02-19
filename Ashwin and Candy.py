t=int(input())
while t>0:
    n=int(input())
    if n<4 or n%2>0:
        print(0)
    else:
        if n%4==0:
            print(n//4-1)
        else:
            print(n//4)
    t-=1
