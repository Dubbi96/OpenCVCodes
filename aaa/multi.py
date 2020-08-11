from multiprocessing import Process, Queue

def work1(id, start, end):
    print('hello')
    return

def work2(id, start, end):
    th1 = Process(target=work1, args=(1, start, end))
    for i in range(start, end):
        print(i)
        if i % 5 == 0:
            th1.start()
            th1.join()
    return

if __name__ == "__main__":
    work2(2, 0, 10000)