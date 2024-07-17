from utility.ClassThatLogs import ClassThatLogs

class ListItem(ClassThatLogs):



    def __init__(self, name):
        super().__init__()
        self.name = name

    def log_message(self, method, message):
        super().log_message(method, message, self.get_name())

    def __str__(self):
        self.to_string()

    def get_name(self):
        return self.name

    def get_full_name(self):
        return self.get_class_name() + " " + self.name

    def to_string(self, spacer="\n", display_class_name=False):
        display = ""
        if display_class_name:
            display += super().to_string() + " "
        return display + self.get_name()
