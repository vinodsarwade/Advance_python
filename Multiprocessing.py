#multiprocessing
import multiprocessing 
import time
def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"cube: {i*i*i}")

if __name__=="__main__":
    ##create two process
    p1= multiprocessing.Process(target=square_numbers)
    p2= multiprocessing.Process(target=cube_numbers)

    t = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finished_time = time.time()- t
    print(finished_time)


##  Multiprocessing with ProcessPoolExecuter   ########

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(1)
    return f"Square: {number * number}"

number = [1,2,3,4,5,6,7,8,9]
if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=3) as executer:
        result= executer.map(square_number,number)
        # print(result)
    for i in result:
        print(i)