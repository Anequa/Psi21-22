# Stwórz nowy moduł w projekcie o nazwie file_manager.
# Stwórz klasę FileManager z parametrem w konstruktorze file_name.
# Klasa będzie zawierać dwie metody: read_file oraz update_file.
# Funkcja update_file powinna zawierac parametr text_data, które w efekcie
# ma być dopisane na końcu pliku. Funkcja read_file powinna zwrócić zawartość pliku.
class FileManager:
    def __init__(self, file_name) -> None:
        self.file_name = file_name

    def read_file(self):
        """Funkcja read_file powinna zwrócić zawartość pliku."""
        try:
            with open(f"{self.file_name}", "r", encoding="utf-8") as file_reader:
                return file_reader.read()
        except IOError:
            print("Wystapił wyjątek IOError")

    def update_file(self, text_data):
        """Funkcja update_file powinna zawierac parametr text_data, które w efekcie ma być dopisane na końcu pliku."""
        try:
            uchwyt = open(f"{self.file_name}", "a", encoding="utf-8")
            uchwyt.write(text_data)
            uchwyt.close()

        except IOError:
            print("Wystapił wyjątek IOError")
