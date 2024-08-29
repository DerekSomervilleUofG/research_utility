import pymsteams
from utility.ReadWriteFile import ReadWriteFile
class Communication():

    read_write_file = ReadWriteFile()

    def __init__(self) -> None:
        self.connector = None
        if self.read_write_file.file_exists("ms_team.cfg", "resource/"):
            key = self.read_write_file.get_file_as_string("ms_team.cfg", "resource/")
            self.connector = pymsteams.connectorcard(key)

    def sent_ms_team_message(self, message):
        if self.connector is not None:
            self.connector.text(message)
            self.connector.send()

