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
