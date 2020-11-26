f=open('height.in', 'r')
t=open('height.out','w')

n=int(f.readline())
x = [1 for i in range(n)]
ans = 1
if n:
    for i in range(n-1):
        d=f.readline().split()
        a,l,r=int(d[0]),int(d[1]),int(d[2])
        if l!=0:
            l-=1
            x[l]=x[i]+1
            ans = max(ans, x[l])
        if r!=0:
            r-=1
            x[r]=x[i]+1
            ans = max(ans, x[r])
    print(ans, file = t)
else:
    print(0, file = t)
t.close()
