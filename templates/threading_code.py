'''Threading example...'''

#in-built py modules
import time 
import threading

class Makethreads:
    '''input seconds'''

    def __init__(self, seconds):
        self.seconds = seconds
    
    
    def do_something(self):
        '''generate a func'''
        
        print(f'Sleeping for {self.seconds} second..')
        time.sleep(self.seconds)
        print(f'Done sleeping for {self.seconds} sec(s)!')
    
    
    def populate_thread_list(self):
        '''Calling target func 10 times using threading and parsing Thread with 1.5 secs args'''
        threads = []

        for i in range(10):
            thread = threading.Thread(target=self.do_something) # pass second argument
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()

if __name__=="__main__":
    start = time.perf_counter()

    a = Makethreads(3)
    a.populate_thread_list()
    
    finish = time.perf_counter()
    
    print(f"Finished in {round(finish-start, 2)} second(s)")