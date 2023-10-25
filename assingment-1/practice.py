n = int(input())
mp = {
    
}

for i in range(n):
    c = list(map(int, input().split()))  # Convert the input list to a tuple
    if c in mp.keys():
        mp[c] += 1
    else:
        mp[c] = 1

sum = 0
for key, value in mp.items():
    if value < key[0]:
        sum += value
    elif value > key[0]:
        sum += value - key[0]

print(sum)
