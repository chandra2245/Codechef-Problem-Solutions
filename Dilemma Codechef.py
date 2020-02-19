t=int(input())
while t>0:
    s=str(input())
    s=list(s)
    ct=s.count("1")
    if ct%2==0:
        print("LOSE")
    else:
        print("WIN")
    t-=1
    
