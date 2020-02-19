t=int(input())
while t>0:
    n,k=map(int,input().split())
    for i in range(k):
        if str(n)[-1]=="9":
            n=n-9
        else:
            n+=1
    print(n)
    t-=1
