def sum(num1,num2,num3):
    result = num1+num2+num3
    return result

total = sum(99,11,5)
print(total)


def all_sum(*args):
    
    sum=0
    for num in args:
        sum+=num
    return sum
    

total = all_sum(45,46,89,11)
print(total)