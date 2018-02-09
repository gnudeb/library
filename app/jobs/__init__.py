from threading import Thread
from ..app import app_instance


class Job:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def start(self, blocking=False):
        if blocking:
            with app_instance.app_context():
                self.func(*self.args, **self.kwargs)
        else:
            Thread(target=self.start, args=(True,)).start()
