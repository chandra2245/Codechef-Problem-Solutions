t=int(input())
while t>0:
    t-=1
    n,k=list(map(int,input().split()))
    n=list(map(int,input().split()))
    n.sort()
    ans=0
    for i in range(len(n)-1):
        if n[i]<k:
            ans+=n[i]
        else:
            diff=n[i]-k
            n[i]=k
            n[i+1]-=diff
            ans+=n[i]
    ans+=n[-1]
    print(n,ans)
            
            
