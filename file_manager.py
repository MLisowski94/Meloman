from pathlib import Path


def path_maping(adres):
    if not Path.exists(adres):
        raise TypeError('This path is not existing')
    path_adres = Path(adres)


class Author:
    #Klasa opisująca autorów i zawierająca dane dotyczące ich dorobku
    #w relacji has-a do klasy Work (agregacja)
    pass

class Work:
    #klasa opisująca dzieło
    #własciwosci: tytul, autor, gatunek, album
    #TODO: okresic czy album powinien byc oddzielna klasa
    #TODO: określić rodzaje relacji
    pass

class File:
    def __init__(self, adres):

        #Adres podawać w formacie raw
        self.path = Path(adres)
        self.name = self.path.name

    def __repr__(self):
        return "FileObject(name: '{0}', format: '{1}')".format(self.name, self.path.suffix)

class AudioFile(File):
    #Określa pliki w formacie audio
    #TODO: stworzyć metode sprawdzajaca czy sciezka AudioFile jest adresem pliku o odpowiednim formacie
    #TODO: stworzyć metode generującą obiekty Author i Work
    #TODO: określić relacje między klasą AudioFile a Author i Work
    audio_format = ('.flac', '.mp3')
    def __init__(self, adres):
        super().__init__(adres)
    def __repr__(self):
        return "AudioFileObject(name: '{0}', format: '{1}')".format(self.name, self.path.suffix)


class Folder(File):

    def __init__(self, adres, dir_level=0):
        super().__init__(adres)
        if not self.path.is_dir():
            raise TypeError("This path is not a pointing to Directory")
        self._dir_level = dir_level
        self.file_map = None

    def __repr__(self):
        return "FolderObject(name: '{0}', dir_level: {1})".format(self.name, self._dir_level)

    def path_has_dirs(self):
        for file in self.path.iterdir():
            if file.is_dir():
                return True
            else:
                return False

    def set_file_map(self):
        # Tworzenie zbioru przeznaczonego do przechowywania plików zawartych w folderze
        self.file_map = self.__make_file_map()

    def __make_file_map(self):
        file_dict = {}
        file_cnt = 0

        folder_dict = {}
        folder_cnt = 0

        for file in self.path.iterdir():
            #Deklaracja słownika który zawierać będzie pliki zawarte w folderze i jego podfolderach
            basic_path_dict = {
                'Dictionary_base_file' : self,
            }

            #Iteracja po kolejnych folderach znajdujących sie w sciezce bazowej
            if file.is_dir():
                #rekurencyjny przebieg po podfolderach
                child_dir = Folder(file, self._dir_level + 1)
                folder_dict['Folder_' + str(folder_cnt)] = child_dir.__make_file_map()
                folder_cnt += 1
            else:
                #dodawanie plików nie będacych folderami
                if file.suffix in AudioFile.audio_format:
                    child_file = AudioFile(file)
                else:
                    child_file = File(file)
                file_dict['File_' + str(file_cnt)] = child_file
                file_cnt += 1

        basic_path_dict['Included_folders'] = folder_dict
        basic_path_dict['Included_files'] = file_dict
        return basic_path_dict

    def get_file_map(self):
    #TODO: Fromatowanie mapy
    #TODO: zwracanie mapy w formacie JSON
        if self.file_map == None:
            self.set_file_map()
        return(self.file_map)
    def get_audio_files_names(self):
        pass
    def print_map(self):
        map = self.get_file_map()
        print(map['Included_folders']['Folder_0'])





