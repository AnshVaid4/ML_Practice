import time
from concurrent.futures import ProcessPoolExecutor

def tables(n):
    print('Printing table of',n)
    for i in range(1,11):
        time.sleep(1)
        print(n,'x',i,'=',n*i,sep='')



if __name__=="__main__":
    
    time_start=time.time()

    with ProcessPoolExecutor(max_workers=3) as multiprocess:
        multiprocess.map(tables,[2,3,4])

    print('Started at:',time_start)

    time_finish=time.time()-time_start
    print('Time taken',time_finish)