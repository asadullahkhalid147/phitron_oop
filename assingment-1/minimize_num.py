import sys
mnt = sys.maxsize
num= int(input())
arr =[]

for _ in range(1):
    cnt =0
    numbers= list(map(int,input().split()))
    for i in numbers:
        arr.append(i) 
    

for k in arr:
    cnt =0
    while k!=0:
        if k%2==1:
            break
        k=k/2
        cnt+=1
    mnt = min(mnt,cnt)
print(mnt)

# import sys

# mnt = sys.maxsize
# n = int(input())
# values = []

# for _ in range(1):
#     k= list(map(int,input().split()))
#     for i in k:
#         values.append(i)

# for k in values:
#     cnt = 0
#     while k != 0:
#         if k % 2 == 1:
#             break
#         k //= 2
#         cnt += 1
#     mnt = min(mnt, cnt)

# print(mnt)


# import sys

# mnt = sys.maxsize
# n = int(input())

# for _ in range(n):
#     cnt = 0
#     k = int(input())
#     while k != 0:
#         if k % 2 == 1:
#             break
#         k //= 2
#         cnt += 1
#     mnt = min(mnt, cnt)

# print(mnt)



