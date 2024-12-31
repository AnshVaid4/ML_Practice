import time
import multiprocessing

def table2():
    print('Printing table of',2)
    for i in range(1,11):
        time.sleep(1)
        print(2,'x',i,'=',2*i,sep='')

def table3():
    print('Printing table of',3)
    for i in range(1,11):
        time.sleep(1)
        print(3,'x',i,'=',3*i,sep='')

def table4():
    print('Printing table of',4)
    for i in range(1,11):
        time.sleep(1)
        print(4,'x',i,'=',4*i,sep='')


if __name__=="__main__":

    p1=multiprocessing.Process(target=table2)
    p2=multiprocessing.Process(target=table3)
    p3=multiprocessing.Process(target=table4)

    time_start=time.time()
    print('Started at:',time_start)
    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    time_finish=time.time()-time_start
    print('Time taken',time_finish)