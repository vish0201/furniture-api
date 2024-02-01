import os
import random
import time
n = 100
while n:
    n-=1
    file = open("./data.txt","a+")
    file.write("hello World")
    file.close()
    os.system("./upload-karo")
    time.sleep(10)