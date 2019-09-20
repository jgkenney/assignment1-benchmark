import threading
import time
import datetime
from time import sleep as s

class Benchmark():
    a=[]
    for i in range(1000):
        a.append(i)
    #threadLock=threading.Lock()
    def getItem(self, tName):
        while 1:
            #self.threadLock.acquire()
            if (len(self.a)==0):
                break
            value=self.a[0]
            self.a.remove(value)
            print("Thread "+tName+", remove "+str(value))
            #self.threadLock.release()

    def run(self):
        thread1=threading.Thread(target=self.getItem,args=["1"])
        thread2=threading.Thread(target=self.getItem,args=["2"])
        thread3=threading.Thread(target=self.getItem,args=["3"])
        thread4=threading.Thread(target=self.getItem,args=["4"])
        thread5=threading.Thread(target=self.getItem,args=["5"])
        thread6=threading.Thread(target=self.getItem,args=["6"])
        thread7=threading.Thread(target=self.getItem,args=["7"])
        thread8=threading.Thread(target=self.getItem,args=["8"])
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread5.start()
        thread6.start()
        thread7.start()
        thread8.start()

def main():
    thread1=Benchmark()
    t1 = time.time()
    thread1.run()
    time.sleep(5)
    t2 = time.time()
    print(t1)
    print(t2)
    print(float(t2 - t1))

main()
