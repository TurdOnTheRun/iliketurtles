import network
import json
from multiprocessing import Process


class Mediator(Process):


    def __init__(self, receiveQueue, sendQueue, ip=None):
        self.daemon = True
        super().__init__()
        self.receiver = receiveQueue
        self.sender = sendQueue
        if ip:
            network.call(sys.argv[1], whenHearCall=self.receive)
        else:
            network.wait(whenHearCall=self.receive)


    def receive(self, obj):
        try:
            data = json.loads(obj)
        except Exception:
            print('Failed to parse json')
        else:
            print('Received:', obj)
            self.receiver.put(data)
        

    def run(self):
        while network.isConnected():
            if not self.sender.empty():
                data = self.empty.get()
                print('Sending:', data)
                network.say(json.dumps(data))
            
        
