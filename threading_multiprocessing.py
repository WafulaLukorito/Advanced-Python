# #? Process: An instance of a program (e.g a Python interpreter)

# *Takes advantage of multiple CPUs and Cores 
# * Separate memory space -> Memory is not shared between processes 
# * Great for CPU-bound processing 
# * New process is strated independently from other process 
# * Processes are interruptible/killable 
# * One GIL for each process -> avoids GIL limitation

# -Heavyweight
# -Starting a process is slower than starting a thread 
# -More memory 
# - IPC (inter-process communication) is more complicated

# #? THREADS
# Threads: An entity within a process that can be scheduled (also known as "lightweight process")
# A process can spawn multiple threads

# *All threads within a process share the same memory
# * lightweight
# * starting a thread is faster than starting a process 
# * great for I/O bound tasks 

# - Threading is limited by GIL: Only one thread at a time 
# - No effect on CPU-bound tasks 
# - Not interruptible/killable 
# - Careful with race conditions


# #? GIL: Global Interpreter Lock

# - A lock that allows only one thread at a time to execute in Python
# - Needed in CPython because memory management is not thread-safe 
#  - explain reference counting, etc 
 
 
# -Avoid the GIL:
#     - Use multiprocessing
#     - Use a different, free-threaded Python implentation (Jython, IronPython)
#     - Use Python as a wrapper for third-party libraries(C/C++  --> numpy, scipy)

# from multiprocessing import Process
# import os
# import time

# def square_numbers():
#     for i in range(100):
#         i * i
#         time.sleep(0.1)

# processes = []
# num_processes = os.cpu_count() #number of CPU cores
# print(f"num processes {num_processes}")

# #create processes
# for i in range(num_processes):
#     p = Process(target=square_numbers)
#     processes.append(p)
    
# #start
# for p in processes:
#     p.start()
    
# #join means that the main process will wait for all the processes to finish before it continues.
# for p in processes:
#     p.join()
    
# print ('end main')

#?in the task manager, we can see multiple processes running, each with its own memory usage. In contrast, with threads, we would see only one process with multiple threads sharing the same memory.

# from threading import Thread
# import time
# import os

# def square_numbers():
#     for i in range(100):
#         i * i
#         time.sleep(0.1)

# threads = []
# num_threads = 10

# for i in range(num_threads):
#     t = Thread(target=square_numbers)
#     threads.append(t)
    
# #start 
# for t in threads:
#     t.start()
# #join means that the main thread will wait for all the threads to finish before it continues. This is important because we want to make sure that all the threads have completed their tasks before we print 'end main'. If we didn't join the threads, we might see 'end main' printed before all the threads have finished their work.
# for t in threads:
#     t.join()
    
# print ('end main')

#? In the task manager, we can see only one process running with multiple threads sharing the same memory. The memory usage is also lower compared to the multiprocessing example.

#* Sharing data between threads is easy because they share the same memory. However, we need to be careful with race conditions, which can occur when multiple threads access shared data at the same time. We can use locks to prevent race conditions.

from threading import Thread
import time
import os


database_value = 0

def increase():
    global database_value
    local_copy = database_value
    local_copy += 1
    database_value = local_copy



# if __name__ == '__main__': #This is necessary to prevent the code from being executed when the module is imported. When we use multiprocessing, the child processes will import the main module, and if we don't have this guard, it will execute the code that creates new processes, leading to an infinite loop of process creation.
#     def increase():
#         global database_value
#         local_copy = database_value
#         local_copy += 1
#         time.sleep(0.1)
#         database_value = local_copy
        
#     thread1 = Thread(target=increase)
#     thread2 = Thread(target=increase)
    
#     thread1.start()
#     thread2.start()
    
#     thread1.join()
#     thread2.join()
    
#     print (database_value) # The output is not always 2 because of the race condition. Both threads read the same value of database_value, increment it, and then write it back, resulting in one of the increments being lost. This is a classic example of a race condition. To fix this, we can use a lock to ensure that only one thread can access the critical section of code that modifies database_value at a time.

# if __name__ == '__main__':
#     from threading import Lock
    
#     database_value = 0
#     lock = Lock()
    
#     def increase(lock): # We need to pass the lock as an argument to the increase function because we want to use the same lock for both threads. If we create a new lock inside the increase function, it will not be shared between the threads, and we won't be able to synchronize access to database_value properly.
#         global database_value
        
#         # lock.acquire() # This will block the thread until it can acquire the lock. Once the lock is acquired, the thread can safely access and modify database_value without worrying about other threads interfering.
#         # local_copy = database_value
#         # local_copy += 1
#         # time.sleep(0.1)
#         # database_value = local_copy
#         # lock.release() # This releases the lock so that other threads can acquire it.
#         #? aLTERNATIVELY, we can use a context manager to automatically acquire and release the lock, which is cleaner and less error-prone:
#         with lock:
#             local_copy = database_value
#             local_copy += 1
#             time.sleep(0.1)
#             database_value = local_copy
        
#     thread1 = Thread(target=increase, args=(lock,))
#     thread2 = Thread(target=increase, args=(lock,))
    
#     thread1.start()
#     thread2.start()
    
#     thread1.join()
#     thread2.join()
    
#     print (database_value) # The output will always be 2 because the lock prevents the race condition. Only one thread can access the critical section of code that modifies database_value at a time, ensuring that both increments are accounted for.

#? QUEUE: A thread-safe data structure that can be used to share data between threads. It provides methods for adding and removing items from the queue, and it handles the necessary locking to ensure that multiple threads can access the queue safely.

# from threading import Thread, Lock
# from queue import Queue
# import time
# from threading import current_thread


# if __name__ == '__main__':
#     #? Using a queue to share data between threads
#     q = Queue()
#     q.put(1)
#     q.put(2)
#     q.put(3)

#     # Returns 1
#     first = q.get()
#     print(first) # 1

#     # Returns True if the queue is empty, False otherwise
#     print(q.empty()) # False

#     # q.task_done() tells the queue that the task is done. This is important because the queue uses a counter to keep track of the number of tasks in the queue. When a thread finishes a task, it calls q.task_done() to decrement the counter. If the counter reaches zero, the queue knows that all tasks have been completed and can proceed accordingly.

#     # q.join() blocks until all items in the queue have been processed. This is useful when you want to wait for all tasks to be completed before continuing with the rest of your program.

#     #? Using a queue to share data between threads
#     def worker(q, lock):
#         while True:
#             value = q.get()
#             # Simulate some work
#             with lock:
#                 print(f'{value} is processed by {current_thread().name}')
#             q.task_done()

#     lock = Lock()
#     num_threads = 3
#     threads = []

#     for i in range(num_threads):
#         t = Thread(target=worker, args=(q, lock)) # We need to pass the lock as an argument to the worker function so that it can use the same lock for printing. This ensures that the print statements from different threads do not interleave and become unreadable.
#         t.daemon = True # Background thread that Dies when the main thread dies
#         t.start()
#         threads.append(t)

#     for i in range(1, 21):
#         q.put(i)
    
#     q.join()

#     print('end main')




# Multiprocessing and threading are both ways to achieve concurrency in Python, but they have different use cases and trade-offs. Multiprocessing is better for CPU-bound tasks that require heavy computation, while threading is better for I/O-bound tasks that involve waiting for external resources. It's important to choose the right approach based on the specific requirements of your application.

#?MULTPROCESSING 

#? Processes do not share memory, so they are more isolated and can run independently. This makes multiprocessing a good choice for CPU-bound tasks that require heavy computation, as it can take advantage of multiple CPU cores. However, starting a process is slower than starting a thread, and multiprocessing can consume more memory due to the need for separate memory spaces.


# from multiprocessing import Process, Value, Array, Lock
# import os
# import time

# #* Without lock

# def add_100 (number):
#     for i in range (100):
#         time.sleep(0.01)
#         number.value += 1

# if __name__ == '__main__':
#     shared_number = Value('i', 0)
#     print ('number at beginning is', shared_number.value)
    
#     p1 = Process(target=add_100, args=(shared_number,))
#     p2 = Process(target=add_100, args=(shared_number,))
    
#     p1.start()
#     p2.start()
    
#     p1.join()
#     p2.join()
    
#     print ('number at end is', shared_number.value) # The output is not always 200, because of a race condition. Both processes read the same value of shared_number, increment it, and then write it back, resulting in one of the increments being lost. To fix this, we can use a lock to ensure that only one process can access the critical section of code that modifies shared_number at a time.
    
#     print ('end main') 
    

# #? With lock

# def add_100(number, lock):
#     for i in range(100):
#         time.sleep(0.01)
#         with lock:
#             number.value += 1


# if __name__ == '__main__':
#     shared_number = Value('i', 0)
#     print ('number at beginning is', shared_number.value)
    
#     lock = Lock() 
#     # We need to pass the lock as an argument to the add_100 function because we want to use the same lock for both processes. If we create a new lock inside the add_100 function, it will not be shared between the processes, and we won't be able to synchronize access to shared_number properly.
    
   
    
#     p1 = Process(target=add_100, args=(shared_number, lock))
#     p2 = Process(target=add_100, args=(shared_number, lock))
    
#     p1.start()
#     p2.start()
    
#     p1.join()
#     p2.join()
    
#     print ('number at end is', shared_number.value) # The output will always be 200 because the lock prevents the race condition. Only one process can access the critical section of code that modifies shared_number at a time, ensuring that both increments are accounted for.
    
#     print ('end main')
    
# #? With shared array

# def add_100(arr, lock):
#     for i in range(100):
#         time.sleep(0.01)
#         with lock:
#             for j in range(len(arr)):
#                 arr[j] += 1
                
# if __name__ == '__main__':
#     shared_array = Array('i', [0, 0, 0])
#     print ('array at beginning is', shared_array[:])
    
#     lock = Lock()
    
#     p1 = Process(target=add_100, args=(shared_array, lock))
#     p2 = Process(target=add_100, args=(shared_array, lock))
    
#     p1.start()
#     p2.start()
    
#     p1.join()
#     p2.join()
    
#     print ('array at end is', shared_array[:]) # The output will always be [200, 200, 200] because the lock prevents the race condition. Only one process can access the critical section of code that modifies shared_array at a time, ensuring that all increments are accounted for.

#? Queue: A process-safe data structure that can be used to share data between processes. It provides methods for adding and removing items from the queue, and it handles the necessary locking to ensure that multiple processes can access the queue safely.


# if name__ == '__main__':
#     from multiprocessing import Queue, Process
#     import time

#     def worker(q):
#         while True:
#             value = q.get()
#             if value is None: # Sentinel value to signal the worker to exit
#                 break
#             print(f'{value} is processed by {os.getpid()}')
#             time.sleep(0.1)

#     q = Queue()
#     num_processes = 3
#     processes = []

#     for i in range(num_processes):
#         p = Process(target=worker, args=(q,))
#         p.start()
#         processes.append(p)

#     for i in range(1, 21):
#         q.put(i)

#     # Add sentinel values to signal the workers to exit
#     for _ in range(num_processes):
#         q.put(None)

#     for p in processes:
#         p.join()

#     print('end main')
    
    
# def square(numbers, queue):
#     for n in numbers:
#         queue.put(n*n)
        
# def make_negative(numbers, queue):
#     for n in numbers:
#         queue.put(-1*n)
        
# if __name__ == '__main__':
#     numbers = [-2, -1, 0, 1, 2]
#     queue = Queue()
    
#     p1 = Process(target=square, args=(numbers, queue))
#     p2 = Process(target=make_negative, args=(numbers, queue))
    
#     p1.start()
#     p2.start()  
    
#     p1.join()
#     p2.join()
    
#     while not queue.empty():
#         print(queue.get())


#?--------------------- ? Process Pool: A pool of worker processes that can be used to execute tasks in parallel. It provides a convenient way to manage a pool of processes and distribute tasks among them.

from multiprocessing import Pool
import os
import time

def cube (number):
    return number * number * number

if __name__ == '__main__':
    
    numbers = range(10)
    pool = Pool()
    
    #? map: A method that applies a function to every item in an iterable and returns a list of the results. It is a convenient way to parallelize the execution of a function across multiple input values.
    result = pool.map(cube, numbers)
    
    #map, apply, join and close are all methods of the Pool class that are used to manage the worker processes and distribute tasks among them.
    
    pool.close()
    pool.join()
    
    print (result)