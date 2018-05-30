import threading
import  time

def saygi(num):
    print("running on number:%s" %num)
    time.sleep(3)

if __name__ == '__main__':
    t1 = threading.Thread(target=saygi, args=(1,))
    t2 = threading.Thread(target=saygi, args=(2,))
    t1.start()
    t2.start()
    print(t1.getName())
    print(t2.getName())

class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        print("running on number of :%s" %self.num)
        time.sleep(3)

if __name__ == '__main__':
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()

#线程锁

def addNum():
    global  num
    print('___get num:',num)
    time.sleep(1)
    lock.acquire()  # 修改数据前加锁
    num -= 1  # 对此公共变量进行-1操作
    lock.release()  # 修改后释放

num = 100  # 设定一个共享变量
thread_list = []
lock = threading.Lock() # 生成全局锁
for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list:  # 等待所有线程执行完毕
    t.join()

print('final num:', num)