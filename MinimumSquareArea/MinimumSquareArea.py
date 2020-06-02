for _ in range(int(input())):
    n=int(input())
    x=[]
    y=[]
    for i in range(n):
        l=list(map(int,input().split()))
        x.append(l[0])
        y.append(l[1])
        
    j=abs(min(x)-max(x))
    k=abs(min(y)-max(y))
    
    print(max(j,k)**2)
