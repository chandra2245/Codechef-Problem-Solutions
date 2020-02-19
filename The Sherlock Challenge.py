no_inst=int(input())
string=str(input())
string=list(string)

st=[]
for i in string:
    if i=="1":
        st.append("a")
    elif i=="2":
        st.append("b")
        st.append("b")
    elif i=="3":
        st.append("a")
        st.append("b")
    else:
        for j in range(len(st)):
            if st[j]=="a":
                st[j]="b"
            else:
                st[j]="a"
x="".join(st)
print(x)
            
        
        
