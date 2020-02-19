#Codechef
#https://www.codechef.com/ICL2019/problems/ICL1901
t=int(input())
while t>0:
    k,n=list(map(int,input().split()))
    k=str(k)
    k=set(k)
    if len(k)==3:
        print(27)
    elif len(k)==2:
        print(8)
    else:
        print(1)
    t-=1    
