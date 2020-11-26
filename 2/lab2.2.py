def quicksort(masiv):
   if len(masiv) <= 1:
       return masiv
   else:
        q = masiv[len(masiv)//2]
        left = []
        mid = []
        right = []
        for k in masiv:
            if k<q:
                left.append(k)
            elif k>q:
                right.append(k)
            else:
                mid.append(k)
            
        return quicksort(left) + mid + quicksort(right)
   
f=open('race.in', 'r')
n=int(f.readline())
d=dict()
l=[]

for i in range(n):
    g = (f.readline().split())
    st , name = g[0] , g[1]
  
    if st in d:
        d[st].append(name)
    else:
        l.append(st)
        d[st] = [name]


ans = quicksort(l)

t = open('race.out', 'w')
for i in ans:
    print('===', i, '===', file = t)
    
    for j in d[i]:
        print(j, file = t)


t.close()


