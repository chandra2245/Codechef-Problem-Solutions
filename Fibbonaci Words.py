t=int(input())
while t>0:
    t-=1
    a,b,x=list(map(str,input().split()))
    x=int(x)
    u=a
    v=b
    a="a"
    b="b"
    z=""
    ct=0
    while ct<=x:
        z=a+b
        a=b
        b=z
        ct=(list(z).count("a"))*len(u)+(list(z).count("b"))*len(v)
        x=x-ct
        
    a=len(u)
    b=len(v)
    na=list(z[0:len(z)-1]).count("a")
    nb=list(z[0:len(z)-1]).count("b")
    tot=(na*len(u))+(nb*len(v))
    tot=x-tot
    last=z[len(z)-1]
    if last=="a":
        print(u[tot-1])
    else:
        print(v[tot-1])
        
        
        


    
