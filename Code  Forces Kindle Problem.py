case=int(input())
while case>0:
    n,s,t=list(map(int,input().split()))
    print(n-min(s,t)+1)
    case-=1
