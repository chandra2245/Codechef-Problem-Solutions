from itertools import combinations
s=str(input())
s=list(s)
all_comb=[]
for i in range(2,len(s)+1):
    comb=list(combinations(s,i))
    all_comb=all_comb+comb
palin=[]
count=0
for j in range(len(all_comb)):
        x="".join(list(all_comb[j]))
        y=x[::-1]
        if x==y:
            count+=1
        else:
            pass
print(count)

    
