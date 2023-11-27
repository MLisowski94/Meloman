import pathlib
from pathlib import Path

"""
Założenia wstępne
"""


class File:
    ''''Klasa zawierająca informacje na temat plików. Założenia:
    Zawiera informacje:
                    odnośnie lokalizacji pliku
                    odnośnie typu pliku
                    lista Node'ów w których skład wchodzi plik
    Jakie informacje wyrazić w postaci data a jakie w postaci relacji node?
    '''
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress

    def __repr__(self):
        return f'Name: {self.name}, Adress: {self.adress}'
    def check_file_format(self):
        pass

    def check_metadata(self):
        pass

class Work(File):


    def __init__(self, name, adress, metadata):
        super(Work, self).__init__(name, adress)
        self.metadata = metadata


class Node:
    '''Klasa stanowiaca wezel. Załozenia:
    *dziecko moze mieć tylko jednego rodzica
    *rodzic może mieć dowolnie wiele dzieci
    *dziecko musi być dokładnie o jeden poziom wyżej niż rodzic
    *wyabstrahowanie z przechowywanych danych jedynie ich struktury
    TODO: Rozpisać strukture przy pomocy UML
    TODO: stworzyć interfejs przekazujący do data informacje o tym że wchodzi w skład Node
    '''
    def __init__(self, data, level=0, parent=None, condition_function=lambda x, y: True,):
        self.data = data
        self.level = level
        self.parent = parent
        ''' Condition_function to funkcja która musi zostać spełniona by stworzyć children node       
        Opisać warunki dla condition function'''

        self.condition = condition_function
        self.children = []

    def __repr__(self):
        return f'Node -- Level: {self.level}, Data:({self.data})'
    # def add_child(self, child_node):
    #     '''Do przemyślenia czy ta funkcja jest potrzebna, może wprowadzać tylko bałagan'''
    #     if child_node.get_level() != (self.get_level() + 1):
    #         raise ValueError("Child level must be exactly one bigger than parents")
    #     child_node.abandon_parent()
    #     self.children.append(child_node)

    def set_child(self, child_data):
        '''Metoda tworząca nowy węzeł-dziecko
        sprawdzając przy tym czy typy danych się zgadzają. Zapobiega to bałaganowi'''

        if type(child_data) is not type(self.data):
            raise TypeError("Child data - {0} is not the same as parent data {1}".format(type(child_data), type(self.data)))
        if self.condition:
            child = Node(child_data, self.level+1, parent=self)
            self.children.append(child)
            return child

    def get_level(self):
        return self.level

    def get_child_list(self):
        return self.children

    def get_data(self):
        return self.data

    def get_parent(self):
        return self.parent
    def abandon_parent(self):
        if self.parent is not None:
            self.parent.children.remove(self)
            self.parent = None

    def is_child(self, another_node):
        if type(another_node) is not Node:
            raise TypeError

        level_difference = self.get_level() - another_node.get_level()
        if level_difference < 1:
            return False

        local_parent = self.get_parent()
        while level_difference > 0:
            if local_parent == another_node:
                return True
            else:
                local_parent = local_parent.get_parent()
                level_difference -= 1
        else:
            return False




def map_path(path):
    '''rekurencyjna funckja zwracająca strukture węzłów reprezentujących wszelkie podfoldery i pliki
    znajdujące się w podanej ścieżce
    TODO: dopisać testy'''
    base_file = pathlib.Path(path)
    base_path_node = Node(File(base_file.name, base_file))
    __map_path_iter(base_path_node)
    return base_path_node
def __map_path_iter(node):
    "Część iteracyjna funkcji map_path"
    for file in node.data.adress.iterdir():
        sub_file = File(file.name, file)
        child_node = node.set_child(sub_file)
        if sub_file.adress.is_dir():
            __map_path_iter(child_node)



def map_save(Map, format):
    '''zapisanie mapy'''
    pass


def map_format_names(Map, Format_specifer, File_type):
    pass


def map_check_albums():
    '''Tworzenie listy albumów zawartych w mapie'''
    pass


def map_check_songs():
    '''Tworzenie listy plików w formacie mp3 zawartych w mapie i sprawdzanie czy
    są to piosenki'''
    pass
