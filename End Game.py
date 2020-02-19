t=int(input())
while t>0:
    t-=1
    dh=list(map(int,input().split()))
    
    dh.sort()
    
    d,h=dh
    count=0
    
    if h%2==0 and d%2==1:
        while d>0:
            x=d*2
            if x<=h:
                d=d*2
                count+=1
                print(d,h)
            elif d==h:
                count+=d
                d=0
                h=0
                break
            else:
                count=count+d-1
                h=h-d+1
                d=1
                
                print(d,h)
        else:
             pass
    print(count)
