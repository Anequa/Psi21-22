# Zaimportuj klasę FileManager w innym pliku, a następnie zademonstruj działanie klasy.
from file_manager.FileManager import FileManager as fm

manager = fm("lab2/test.txt")
print(manager.read_file())

manager.update_file("\nmmabbvewaxx")
print(manager.read_file())
