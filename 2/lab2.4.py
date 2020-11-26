n=int(open('antiqs.in', 'r').readline())

arr = [0]*n
for i in range(n):
    arr[i] = i+1
for i in range(2,n):
    arr[i], arr[i//2] = arr[i//2], arr[i]

temp=open('antiqs.out','w')
print(*arr, file = temp)
temp.close()

