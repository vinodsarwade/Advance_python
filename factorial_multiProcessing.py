'''
example: Multiprocessing for CPU bound tasks
Scenario : Factorial calculation
factorial calculation especially for large numbers,
onvolves significant computation work, 
multiprocessing can be used to distibute 
the workload accross multiple CPU cores, improved performance.
'''
import multiprocessing
import time
import math
import sys

sys.set_int_max_str_digits(100000)

def computer_factorail(number):
    print(f"factorial of {number}")
    result = math.factorial(number)
    print(f"factorial of {number} is {result}")
    return result

if __name__=="__main__":
    numbers = [5000,6000,7000,8000]
    start_time = time.time()

##create a pool of worker processes 
    with multiprocessing.Pool() as pool:
        res = pool.map(computer_factorail,numbers)  
    end_time = time.time()

    print(f"results: {res}")
    print(f"final time: {end_time - start_time }seconds")
