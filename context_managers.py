
#------------ CONTEXT MANAGERS --------------
#? Context managers are a way to manage resources in Python. They allow you to set up a context for your code to run in, and then clean up after it when you're done. This is especially useful for managing resources like files, network connections, or locks.

#? The most common way to use a context manager is with the with statement. The with statement ensures that the context manager's __enter__() method is called before the block of code is executed, and the __exit__() method is called after the block of code is executed, even if an exception occurs.

#? The with statement is often used for file handling, as it ensures that the file is properly closed after its suite finishes, even if an exception is raised.

with open('example.txt', 'w') as file:
    file.write('Hello, World!')  # The file will be automatically closed after this block, even if an error occurs.
    
#* If we were to write the same code without using a context manager, we would need to manually close the file, which can lead to errors if we forget to do so or if an exception occurs before we get to the close() method.

file = open('example.txt', 'w')
try:
    file.write('Hello, World!')
finally:
    file.close()
    
    
    
#?Locks are used to prevent multiple threads from accessing a shared resource at the same time. A context manager can be used to acquire and release a lock automatically.

from threading import Lock
lock = Lock()
with lock:  # The lock will be automatically released after this block, even if an error occurs.
    # critical section of code that accesses shared resource
    pass

#prevents lock.aquire() and lock.release() from being called manually, which can lead to errors if we forget to release the lock or if an exception occurs before we get to the release() method.


#?CUSTOM CONTEXT MANAGERS

#? The with statement can also be used with custom context managers by defining a class that implements the __enter__() and __exit__() methods. This allows you to create your own context managers for managing resources specific to your application.

# class ManagedFile: #A custom context manager for managing a file resource. It ensures that the file is properly opened and closed, even if an error occurs.
#     def __init__(self, filename):
#         print('Initializing ManagedFile with filename:', filename)
#         self.filename = filename
        
#     def __enter__(self): #Enter method is called when the with statement is executed. It opens the file and returns the file object.
#         self.file = open(self.filename, 'w')
#         return self.file
    
#     def __exit__(self, exc_type, exc_val, exc_tb): #Exit method is called when the block of code inside the with statement is finished executing. It takes three arguments: exc_type, exc_val, and exc_tb, which are used to handle exceptions that may occur within the block of code. In this case, it simply closes the file.
#         self.file.close()
#         print('Exiting ManagedFile context, file closed.')
        
#         if exc_type is not None:  # If an exception occurred, it will be printed here.
#             print('Exception occurred:', exc_type, exc_val)
            
            
            
# # with ManagedFile('example.txt') as file:
# #     print('Doing something with the file...')
# #     file.write('Hello, World!')  # The file will be automatically closed after this block, even if an error occurs.
    

# #Try something that raises an exception to see how the context manager handles it.
# with ManagedFile('example.txt') as file:
#     print('Doing something with the file...')
#     file.write('Hello, World!')
#     raise ValueError('Something went wrong!')  # This will trigger the exception handling in the __exit__ method, and the file will still be closed properly.


#? Using contextlib.contextmanager decorator to create a context manager. Now we can use function open_managed_file as a context manager without needing to define a class with __enter__ and __exit__ methods. The code inside the function is executed when the context is entered, and the code after the yield statement is executed when the context is exited, even if an exception occurs.

# uses generator syntax to create a context manager. The code before the yield statement is executed when the context is entered, and the code after the yield statement is executed when the context is exited, even if an exception occurs. This allows for a more concise and readable way to create context managers without needing to define a class with __enter__ and __exit__ methods.

from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    print('Opening file:', filename)
    file = open(filename, 'w')
    try:
        yield file  
    finally:
        print('Closing file:', filename)
        file.close()
        

with open_managed_file('example.txt') as file:
    print('Doing something with the file...')
    file.write('Hello, World!')  # The file will be automatically closed after this block, even if an error occurs.