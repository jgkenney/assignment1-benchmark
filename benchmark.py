import threading
# from time import sleep as s
import time

def Start():
    print("START\n")
    global start
    start = time.time()

def End():
    print("END\n")
    global end
    end = time.time()
    elapsed = (end-start)
    print(elapsed)

def Benchmark():
    global operations
    operations = 0
    while operations < 10:
        operations+=1


def main():
    Start()
    Benchmark()
    End()

#     int(iops = 0)
#     operations / time = iops
#     print(iops)
# single.start()
# end = time.time()
# print(end - start)
