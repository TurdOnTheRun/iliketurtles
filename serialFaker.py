from multiprocessing import Process
import time

class SerialFaker(Process):

    def __init__(self, queue):
        super().__init__()
        self.daemon = True
        self.queue = queue
        self.commands = [[0,0.4],[0,-0.2],[1,45],[1,-45],[1,0],[0,1],[0,0]]

    def run(self):

        while True:
            for co in self.commands:
                time.sleep(5)
                print('sending', co)
                self.queue.put(co)
    
