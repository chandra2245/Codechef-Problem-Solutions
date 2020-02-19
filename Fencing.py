t=int(input())
while t>0:
    t-=1
    m,n,k=list(map(int,input().split()))
    plant_loc=[]
    for i in range(k):
        el=list(map(int,input().split()))
        el="".join(el)
        plant_loc.append(el)
    print(plant_loc)
