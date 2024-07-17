from threading import Thread, Event

class MultiThreadProcess():

    def multi_process(method, time_out):
        bridge = Event()
        mvn_thread = Thread(target=method)
        mvn_thread.start()
        mvn_thread.join(timeout=time_out)
        bridge.set()
