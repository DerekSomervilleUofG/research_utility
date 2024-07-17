import time

class Logging:
    __unique_instance = None
    start_time = None
    logging_on = True

    def __new__(cls):
        if Logging.__unique_instance is None:
            Logging.__unique_instance = object.__new__(cls)
        return Logging.__unique_instance

    def get_instance():
        return Logging.__unique_instance

    def set_logging_off(self):
        self.logging_on = False

    def set_logging_on(self):
        self.logging_on = True

    def get_start_time(self):
        if self.start_time is None:
            self.start_time = time.time()
        return self.start_time

    def get_duration(self):
        return time.time() - self.get_start_time()

    def message(self, class_name, method_name, message):
        if self.logging_on:
            print(self.get_duration(), class_name, method_name, message)
