from threading import Thread

def my_function1():
    print("123")
    print("456")
    print("789")
    
def my_function2():
    print("abc")
    print("def")
    print("ghi")
    
def my_function3():
    print("ABC")
    print("DEF")
    print("GHI")
    
import threading

t1 = Thread(target=my_function1)
t2 = Thread(target=my_function2)
t3 = Thread(target=my_function3)

t1.start()
t2.start()
t3.start()
