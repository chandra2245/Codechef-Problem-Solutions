from itertools import combinations
test_case=int(input())
while test_case>0:
    n,k=map(int,input().split())
    sequence=list(map(int,input().split()))
    sequence.sort()
    sm=[]
    if k==1:
        print(sequence.count(min(sequence)))
    else:
        comb=list(combinations(sequence,k))
        for i in comb:
            pair_sum=sum(i)
            #print(pair_sum,i)
            sm.append(pair_sum)
        #print(comb)
        print(sm.count(min(sm)))
    test_case-=1
