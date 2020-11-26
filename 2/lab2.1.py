import random
def quicksort(massiv):
   if len(massiv) <= 1:
       return massiv

  
   else:
        left = []
        right = []
        mid = []
       
        q = random.choice(massiv) 
        for i in range(len(massiv)):
            if massiv[i] < q:
                left.append(massiv[i])
            elif massiv[i] > q:
                right.append(massiv[i])
            else:
                mid.append(massiv[i])
       
        return quicksort(left) + mid + quicksort(right)

f = open('sort.in', 'r')

n = int(f.readline())
l = (f.readline().split())
for i in range(n):
    l[i] = int(l[i])
    
    
    
answer = quicksort(l)

t = open('sort.out','w')

print(*answer, file = t)

t.close()

