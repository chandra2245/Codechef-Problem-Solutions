test_case=int(input())
while test_case>0:
    n=int(input())
    scene=list(map(str,input().split()))
    roll_scene=[scene[-1][::-1]]
    rev=-2
    if n%2==0:
        for i in range(n//2-1):
            roll_scene.append(scene[i])
            roll_scene.append(scene[rev])
            rev-=1
    else:
        for i in range(n//2):
            roll_scene.append(scene[i])
            roll_scene.append(scene[rev])
            rev-=1
    if n%2==0:
        roll_scene.append(scene[n//2-1])
    for i in roll_scene:
        print(i,end=" ")
    test_case-=1
    
