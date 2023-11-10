from pathlib import Path

"""
Założenia wstępne
"""


class File:
    '''Klasa sluzaca do przechowywania inforamcji na temat plików'''
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress

    def check_file_format(self):
        pass

    def check_metadata(self):
        pass

class Work(File):
    '''Klasa reprezentujaca pojedyncze prace takie jak pisoenki'''
    def __init__(self, name, adress, metadata):
        super(Work, self).__init__(name, adress)
        self.metadata = metadata


class Node:
    '''Klasa stanowiaca wezel'''
    def __init__(self, data, level=0, parent=None):
        self.data = data
        self.level = level
        self.parent = parent
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def set_child(self, child_data):
        child = Node(child_data, self.level+1, parent=self)
        self.add_child(child)
        return child

    def get_level(self):
        return self.level

    def get_child_list(self):
        return self.children

    def get_data(self):
        return self.data

    def get_parent(self):
        return self.parent

    def is_ancestor(self, another_node):
        if type(another_node) is not Node:
            raise TypeError

        level_difference = self.get_level() - another_node.get_level
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




def map_path(Path):
    '''rekurencyjna funckja zwracająca strukture węzłów reprezentujących wszelkie podfoldery i pliki
    znajdujące się w podanej ścieżce'''
    pass


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
