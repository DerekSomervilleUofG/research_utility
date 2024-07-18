import os
import socket
from base64 import decodebytes
from utility.ReadWriteFile import ReadWriteFile

class AccessToken:

    __uniqueInstance = None
    ip_file_name = "ip.cfg"
    file_name = "token.cfg"
    read_write_file = ReadWriteFile()
    user_name = "auto.marker"
    ip_address = None
    access_token = decodebytes(b"Z2xwYXQteXpVNjI5eDYtM1JVWnh6MXlfeUU=\n").decode("utf-8").strip()

    def __new__(cls):
        if AccessToken.__uniqueInstance is None:
            AccessToken.__uniqueInstance = object.__new__(cls)
        return AccessToken.__uniqueInstance

    def get_user_name(self):
        user_name = None
        counter = 0
        while user_name is None or ("@" in user_name and counter < 3):
            user_name = input("Please provide the user name?")
            counter += 1
        return user_name

    def get_ip_address(self):
        if self.ip_address is None:
            host_name = socket.gethostname()
            self.ip_address = socket.gethostbyname(host_name).replace(".", "")
            if self.read_write_file.file_exists(self.ip_file_name, os.getcwd() + "/resource/"):
                stored_ip_address = self.read_write_file.get_file_as_string(self.ip_file_name, os.getcwd() + "/resource/").strip()
                if stored_ip_address != self.ip_address:
                    self.read_write_file.delete_file(self.file_name, os.getcwd() + "/resource/")
                    self.read_write_file.write_file(self.ip_file_name, self.ip_address,os.getcwd() + "/resource/")
        return self.ip_address

    def get_access_token(self):
        if self.access_token is None:
            self.read_write_file.fix_working_directory()
            ip_address = self.get_ip_address()
            if self.read_write_file.file_exists(self.file_name, os.getcwd() + "/resource/"):
                raw_token = self.read_write_file.get_file_as_csv(self.file_name)
                self.user_name = raw_token[0][0]
                self.access_token = self.encrypt(raw_token[0][1], ip_address, -1)
            else:
                self.user_name = self.get_user_name()
                self.access_token = input("Please provide your personal access token: ")
                raw_data = []
                raw_data.append([self.user_name,self.encrypt(self.access_token, ip_address)])
                self.read_write_file.write_csv(self.file_name,raw_data)
        return self.user_name, self.access_token

    def encrypt(self, word, ip_address, direction=1):
        encrypted_word = ""
        for counter, letter in enumerate(word):
            counter = counter % len(ip_address)
            encrypted_word += chr(ord(letter) + (direction * int(ip_address[counter]) ))
        return encrypted_word
    
def main():
    access_token = AccessToken()
    user_name, actual_access_token = access_token.get_access_token()
    ip_address = access_token.get_ip_address()
    print(user_name, actual_access_token)
    print("encrypt", access_token.encrypt("Test123#", ip_address))
    print("De-encrypt", access_token.encrypt(access_token.encrypt("Test123#", ip_address), ip_address, -1))

if __name__ == "__main__":
    main()


