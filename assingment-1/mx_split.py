stirng = input()
l=0
r=0
cnt=0
col=0
row=0
value = [['' for _ in range(1000)] for _ in range(1000)]

for i in range(len(stirng)):
    if(stirng[i]=='R'):
        value[row][col]='R'
        r+=1
    else:
        value[row][col]='L'
        l+=1
    col+=1

    if r==l and l>0:
        col=0
        row+=1
        cnt+=1
        r=0
        l=0
    
print(cnt)

for i in range(1000):
    if(value[i][0] not in ('R','L') ):
        continue
    print(''.join(value[i]))