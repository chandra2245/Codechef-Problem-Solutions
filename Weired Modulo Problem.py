t=int(input())
while t>0:
    n=int(input())
    arr=list(map(int,input().split()))
    arr=list(set(arr))
    arr.sort()
    res=arr[-2]%arr[-1]
    print(res)
    t-=1
    
