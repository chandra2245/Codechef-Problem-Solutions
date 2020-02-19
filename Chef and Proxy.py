t=int(input())
while t>0:
    d=int(input())
    s=str(input())
    s=list(s)
    check=.75*d
    no_p=s.count("P")
    need=0
    if no_p>=check:
        need=0
    else:
        if type(check)==float:
            need=(int(check)+1)-no_p
        else:
            need=check-no_p
    proxy_count=0
    for i in range(2,d-2):
        if s[i]=="A":
            if (s[i-1] or s[i-2]) and (s[i+1] or s[i+2])=="P":
                proxy_count+=1
            else:
                pass
        else:
            pass
    if no_p>=check:
        print(0)
    else:
        if need<=proxy_count:
            print(need)
        else:
            print(-1)
    t-=1
