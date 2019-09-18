import threading
import time
from time import sleep as s

class Benchmark():
        #Global variable count
    a=[]
    for i in range(1000):
        a.append(i)
    #uncomment next line to make the code correct
    threadLock=threading.Lock()
    def getItem(self, tName):
        while 1:
            #uncomment next line to make the code correct
            self.threadLock.acquire()
            if (len(self.a)==0):
                break
            value=self.a[0]
            self.a.remove(value)
            print("Thread "+tName+", remove "+str(value))
            #uncomment next line to make the code correct
            self.threadLock.release()

    # Two threads are constantly removing elements from a shared array of numbers.
    def run(self):
        start = time.time()
        thread1=threading.Thread(target=self.getItem,args=["1"])
        thread2=threading.Thread(target=self.getItem,args=["2"])
        thread3=threading.Thread(target=self.getItem,args=["3"])
        thread4=threading.Thread(target=self.getItem,args=["4"])
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        end = time.time()
        elapsed = (end-start)
        print(elapsed)
    #
    # def stop(self):
    #     when a ==0:






def main():
    print("START")
    # n = int(input("Enter 1,2,4,8:"))

    thread1=Benchmark()
    thread1.run()
    # for i in range(1,n+1):
    #     threadTemp=Benchmark(i)
    #     threadTemp.start()

    s(10)
    print("END\n")


main()
#     int(iops = 0)
#     operations / time = iops
#     print(iops)
# single.start()
# end = time.time()
# print(end - start)
