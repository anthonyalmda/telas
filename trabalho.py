from threading import Event, Thread
from functions import target


class Worker(Thread):
    def __init__(self, target, queue, *, name='Worker'):
        super.__init__()
        self.name = name
        self.queue = queue
        self._target = target
        self.stoped = False
        print(self.name, 'Started')

    def run(self):
        event.wait()
        while not self.queue.empty():
            acao = self.queue.get()
            if acao == 'Kill':
                self.queue.put(acao)
                self.stoped = True
                break
            self._target(acao)

    def join(self):
        while not self._stoped:
            pass

