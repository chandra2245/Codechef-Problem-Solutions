t=int(input())
while t>0:
    t-=1
    n=int(input())
    s,x=list(map(str,input().split()))
    length=len(s)
    total=(length*(length+1))//2
    count=0
    tot=0
    for i in range(length):
        if s[i]==x:
            tot=tot+((count*(count+1))//2)
            count=0
        else:
            count+=1
    tot=tot+((count*(count+1))//2)        
    if x not in s:
        print(0)
    else:
        print(total-tot)
