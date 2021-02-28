from mediator import Mediator
from multiprocessing import Queue

receive = Queue()
send = Queue()
medi = Mediator(receive, send)
medi.start()

while True:
    phrase = input()
    send.put({'text':phrase})
    
