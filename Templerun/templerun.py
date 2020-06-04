n=int(input())
l=list(map(int,input().split()))
m=int(input())
r=[]
for i in range(m):
    k=int(input())
    s=0
    for j in range(n):
        s=s+l[j]
        if s>=k:
            print(j+1)
            break
            
    else:
        print(-1)
            
