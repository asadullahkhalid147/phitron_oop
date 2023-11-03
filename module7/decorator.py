import math
import time
def timer(func):
    def inner(*args,**kwargs):
        print('time started')
        start = time.time()
        # print(func)
        func(*args,**kwargs)
        print('time ended')
        end = time.time()
        print(f'total time taken {end - start}')
    return inner


# timer()()#calling the function that is returned by another function
@timer
def get_factorial(n):
    print('factorial starting')
    result = math.factorial(n)
    print(f'factorial of {n} is: {result}')

get_factorial(1200)
# timer(get_factorial)()