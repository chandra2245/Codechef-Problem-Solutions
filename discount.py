t=int(input())
while t>0:
    n=int(input())
    n=str(n)
    m=len(n)
    a=""
    b=""
    for i in range(m-1):
        if n[i]>n[i+1]:
            a=n[0:i]
            b=n[i+1:]
            break
    if a=="" and b=="":
        print(n[0:m-1])
    else:
        n=a+b
        print(int(n))
    t-=1
