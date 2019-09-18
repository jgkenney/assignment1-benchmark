import threading
import time

def Benchmark():
    operations = 0
    while operations < 10000000000:
        operations+=1

def main():
    print("START")
    start = time.time()
    Benchmark()
    end = time.time()
    elapsed = (end-start)
    print(elapsed)
    print("END\n")


main()
#     int(iops = 0)
#     operations / time = iops
#     print(iops)
# single.start()
# end = time.time()
# print(end - start)
