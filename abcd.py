import time

def foo(val):
    if val > 100:
        print("Sleep for 3 seconds")
        time.sleep(3)
    else:
        print("Sleep for 5 seconds")
        time.sleep(5)

def bar(arg):
    #foo(arg)
    print("exit")
