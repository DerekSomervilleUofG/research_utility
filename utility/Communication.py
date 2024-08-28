import pymsteams
from utility.ReadWriteFile import ReadWriteFile
class Communication():

    read_write_file = ReadWriteFile()

    def __init__(self) -> None:
        key = self.read_write_file.get_file_as_string("ms_team.cfg", "resource/")
        self.connector = pymsteams.connectorcard(key)

    def sent_ms_team_message(self, message):
        self.connector.text(message)
        self.connector.send()

