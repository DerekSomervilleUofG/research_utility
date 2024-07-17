from utility.Logging import Logging

class ClassThatLogs:

    logging_filter = []
    logging_on = False

    def __init__(self):
        self.logging = Logging()

    def log_message(self, method, message, filter):
        if filter in self.logging_filter or self.logging_on:
            if self.logging is None:
                self.logging = Logging()
            if isinstance(message, str):
                self.logging.message(self.get_class_name(), method, message)
            else:
                self.logging.message(self.get_class_name(), method, str(message))

    def get_class_name(self):
        class_name = str(self.__class__).split("'")[1]
        position = class_name.rfind(".") + 1
        if position > 0:
            class_name = class_name[position:]
        return class_name

    def to_string(self):
        return self.get_class_name()
