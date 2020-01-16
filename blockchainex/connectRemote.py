import ast
import subprocess


class ConnectRemote:
    def runCommand(self, type, value):
        if type == "GET-BLOCK-BY-HASH":
            process = subprocess.getoutput(r"C:\Users\Paulius\Desktop\test.bat " + value + " 1")

            process = process.split('"', 2)[2]

            print(process)
            return process
