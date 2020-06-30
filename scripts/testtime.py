import concurrent.futures
import multiprocessing
import threading
import time

start = time.perf_counter()


def do_something1():
    for i in range(5):
        print(f'from do_something1: Sleeping {i} second...')
        time.sleep(1)
    print( f'Done Sleeping1...')

def do_something2():
    for i in range(10):
        print(f'from do_something2: Sleeping {i} second...')
        time.sleep(1)
    print( f'Done Sleeping2...')

p1 = threading.Thread(target=do_something1)
p2 = threading.Thread(target=do_something2)

p1.start()
p2.start()

p1.join()
p2.join()
# with concurrent.futures.ProcessPoolExecutor() as executor:
#     secs = [5, 4, 3, 2, 1]
#     results = executor.map(do_something, secs)

    # for result in results:
    #     print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
