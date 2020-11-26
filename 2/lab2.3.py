def mergeSort(a):
    global ans

    if len(a)>1:
        mid = len(a)//2
        a1 = a[:mid]
        a2 = a[mid:]
        left = mergeSort(a1)
        right = mergeSort(a2)
        i, j, k = 0, 0, 0
      
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                a[k] = left[i]
                i += 1
            
            else:
                a[k] = right[j]
                j += 1
                ans += (len(left)-i)
            k += 1

        while i<len(left):
            a[k] = left[i]
            i += 1
            k += 1

        while j<len(right):
            a[k] = right[j]
            j += 1
            k += 1

    return a
    
f = open('inversions.in', 'r')
n = int(f.readline())
a = f.readline().split()
for i in range(n):
    a[i] = int(a[i])

ans = 0
mergeSort(a)


t = open('inversions.out','w')
print(ans, file = t)
t.close()


