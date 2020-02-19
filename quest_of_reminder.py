t=int(input())
while t>0:
    n=int(input())
    new=n/2
    if new==n//2:
        print(int(new))
    else:
        print((n//2)+1)
    t-=1
