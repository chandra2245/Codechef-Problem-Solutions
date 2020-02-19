t=int(input())
while t>0:
    t-=1
    a,b,c,d=list(map(int,input().split()))
    team=0
    if a==0 or b==0 or d==0:
        pass
    else:
        tot=sum([a,b,c,d])//4
        team=min(tot,a,b,d)
    print(team)
        
