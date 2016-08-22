#!/usr/bin/env python
import os
import sys
import subprocess as sp
import threading
import time
from collections import deque
try:
    import Queue
except ImportError:
    import queue as Queue

#samtools sort kian84autosome.bam > kian84autosome.sorted.bam
#/psmc/utils/fq2psmcfa -q20 /psmc_files/kian84autosome.fq.gz > /psmc_files/kian84autosome.psmcfa
in_filename  = [i for i in os.listdir(os.getcwd()) if i.endswith("psmcfa")][0]
out_filename = "split_" + in_filename

with open(out_filename, "w+") as output_handle:
    command = ['/psmc/utils/splitfa', in_filename]
    sp.call(command, stdout=output_handle)

#/psmc/psmc -N25 -t15 -r5 -p "4+25*2+4+6" -o /psmc_files/split_kian84autosome.psmc /psmc_files/kian84autosome.psmcfa
commandList = []
for i in range(1, 101):
    commandList.append(['/psmc/psmc -N20 -t15 -r5 -b -p "4+25*2+4+6" -o round-{}.psmc {} | sh'.format(i, out_filename)])

#multicore threading
threadList=[]
for i in range(30): #NUMBER CPU
    threadList.append("Thread-{}".format(i+1))

queueLock = threading.Lock()
workQueue = Queue.Queue(len(commandList))
threads = []
threadID = 1

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        process_data(self.name, self.q)#,self.alpha)
        print("Exiting " + self.name)

def process_data(threadName, q):
    while not exitFlag:

        queueLock.acquire()

        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            status = True #NEED TO ADD ERROR CHECKING
            for item in data:
                status = sp.call(item, shell=True)
        else:
            queueLock.release()

# Create new threads
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# Fill the queue
queueLock.acquire()
for command in commandList:
    workQueue.put(command)
queueLock.release()


# Wait for queue to empty
while not workQueue.empty():
    time.sleep(1)

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("Exiting Main Thread")

exitFlag = 0
