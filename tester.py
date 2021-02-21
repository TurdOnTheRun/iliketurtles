from executer import Executer
from serialFaker import SerialFaker
from multiprocessing import Queue


queue = Queue()
seri = SerialFaker(queue)
exi = Executer(queue)

seri.start()
exi.run()
