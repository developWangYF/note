import threading
import time


def foo1():
    for i in range(1, 3):
        print('foo1 函数第{}执行'.format(i))
        time.sleep(2)


def foo2():
    for i in range(1, 6):
        print('foo2 函数第{}执行'.format(i))
        time.sleep(1)


if __name__ == '__main__':
    start_time = time.time()
    t1 = threading.Thread(target=foo1)
    t2 = threading.Thread(target=foo2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = start_time - time.time()

    print('主线程结束执行时间{}'.format(end_time))