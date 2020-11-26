
 
f=open('check.in', 'r')
t=open('check.out','w')
n=int(f.readline())
if n:
    d=[0]*n
    mas=[[0,0,0] for i in range(n)]
    for i in range(n):
        d=f.readline().split()
        a,left,right=int(d[0]),int(d[1]),int(d[2])
        left-=1
        right-=1
        mas[i][0]=a
        mas[i][1]=left
        mas[i][2]=right
    fl = 1
    dl=[[0,10000000000,-10000000000]]
    while dl and fl:
        pars=dl.pop()
        num=pars[0]
        ap=pars[1]
        al=pars[2]
        a,left,right = mas[num][0],mas[num][1],mas[num][2]
        if a>=ap or a<=al:
            fl=0
            break
        if left!=-1:
            if mas[left][0] >= mas[num][0]:
                fl=0
                break
            dl.append([left,a,al])
        if right!=-1: 
            if mas[right][0] <= mas[num][0]:
                fl=0
                break
            dl.append([right,ap,a])
              
    if fl:
        print('YES',file = t)
    else:
        print('NO',file = t)
else:
    print('YES',file = t)
t.close()
