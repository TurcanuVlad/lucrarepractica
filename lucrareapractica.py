with open('C:/Users/Admin/Desktop/Lista_clasei_11D.txt', 'r') as f:
    a=list(f)
b=0
m=0
for i in a:
    g=i.split()
    b=int(g[2])
    m=b+1
    if g[3]=='1':
        z=open('Engleza1.txt', 'a')
        z.write(i)
        z.close()
    else:
        z=open('Engleza2.txt', 'a')
        z.write(i)
        z.close()
jopa=m/float(b)
j=open('Media.txt', 'w')
j.write(str(jopa))
j.close()
#Iubesc listele