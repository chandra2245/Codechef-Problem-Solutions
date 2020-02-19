t=int(input())
while t>0:
    s=input()
    flag=0
    dot=list()
    move=list()
    for i in range(len(s)):
        if s[i]==".":
            pass
        else:
            dot.append(i)
            move.append(int(s[i]))
    for i in range(len(move)-1):
        if dot[i+1]-dot[i]<=move[i]+move[i+1]:
            flag=1
            break
    if flag==1:
        print("unsafe")
    else:
        print("safe")
    t-=1
