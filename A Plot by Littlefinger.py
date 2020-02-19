t=int(input())
while t>0:
    n,k=map(int,input().split())
    r=[]
    c=[]
    for i in range(k):
        a,b=map(int,input().split())
        r.append(a)
        c.append(b)
    r=len(set(r))
    c=len(set(c))
    r=n-r
    c=n-c
    occupied=r*c
    if r==0 or c==0:
        print('Impossible')
    else:
       import math
       gcd=math.gcd(occupied,n*n)
       p=occupied/gcd
       q=(n*n)/gcd
       print(int(p),int(q))
       t-=1
    
