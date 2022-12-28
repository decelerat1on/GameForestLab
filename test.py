import threading
import datetime
import time
def time_count():
    global sec,min
    while True:
        time_now = time.time()
        time_now = time.ctime(time_now).split(' ')[3].split(':')[1:]
        sec, min = int(time_now[1]), int(time_now[0])

def privet():
    while True:
        print('Hello!')
        time.sleep(3)
# thread1 = threading.Thread(target=time_count)
# thread2 = threading.Thread(target=privet)
# thread1.start()
# thread2.start()
# print('Конец')
time_now = time.time()
time_now = time.ctime(time_now).split(' ')[3].split(':')[1:]
sec,min = int(time_now[1]),int(time_now[0])


print(min,':',sec)