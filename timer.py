import threading
def mytimer():
   print("Python Program\n")
Thread1 = threading.Timer(15.0, mytimer)
Thread2 = threading.Timer(15.0, mytimer)
Thread3 = threading.Timer(15.0, mytimer)
Thread4 = threading.Timer(15.0, mytimer)
Thread1.start()
Thread2.start()
Thread3.start()
Thread4.start()

print("Bye\n")
