from os import close


class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        f=open(self.file_name,"r")
        print(f.read())
        f.close()


    def update_file(self,text_data):
        f=open(self.file_name,"a")
        f.write(text_data)
        f.close()

file=FileManager("text.txt")
file.read_file()
file.update_file("lubie pieski ")
file.read_file()