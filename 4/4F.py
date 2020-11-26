f = open("garland.in", "r")
fout = open("garland.out", "w")
fin = f.readline().split()
n = int(fin[0])
A = float(fin[1])
left = 0
right = A
height = [0]*n
height[0] = A

while right-left > 0.0000000001:
    height[1] = (left+right)/2
    under = True
    for i in range(2,n):
        height[i] = 2*height[i-1]-height[i-2] + 2
        if height[i] < 0:
            under = False
            break
    if under:
        right = height[1]
    else:
        left = height[1]

print("%.2f" % height[-1], file = fout)
