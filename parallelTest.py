import multiprocessing
from multiprocessing import Process
import threading



class ThreadRunner(threading.Thread):
    # this class represents the a single instance of a running thread
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        print(self.name, '\n')
		
		
		
		
		
		
class ProcessRunner:
    # this class represents a single instance of running procces
    def runp(self, pid, numThreads):
        mythreads = []
        for tid in range(numThreads):
            name = "Proc-"+str(pid)+"-Thread-"+str(tid)
            th = ThreadRunner(name)
            mythreads.append(th)
        for i in mythreads:
            i.start()
        for i in mythreads:
            i.join()
			
			
			
			
			
			
class ParallelExtractor:
    def runInParallel(self, numProcesses, numThreads):
        myprocs = []
        prunner = ProcessRunner()
        for pid in range(numProcesses):
            pr = Process(target=prunner.runp, args=(pid, numThreads))
            myprocs.append(pr)
            
        for i in myprocs:
            i.start()
            
        for i in myprocs:
            i.join()
			
			
