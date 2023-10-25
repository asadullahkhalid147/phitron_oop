j=int(input())
while(j!=0):

    x=input()
    
    sum=''


    y=len(x)

    for i in range(y,0,-1):
        sum+=x[i-1]+' '

    print(sum)
    j=j-1




    