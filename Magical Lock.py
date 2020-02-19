t=int(input())
while t>0:
    t-=1
    n,m=map(int,input().split())
    count=0
    if m<n:
        print(n-m)
        
    else:
        while m>n:
            if m%2>0:
                m+=1
                count+=1
            m=m//2
            count+=1
        print(count+n-m)
    
