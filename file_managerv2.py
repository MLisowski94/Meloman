import pathlib
from pathlib import Path
from file import File
from node import Node
"""
Założenia wstępne
TODO: określić dokładnie api File i Node
"""





def map_path(path):
    '''rekurencyjna funckja zwracająca strukture węzłów reprezentujących wszelkie podfoldery i pliki
    znajdujące się w podanej ścieżce, funkcja ta stnaowi kompozcyje Node i Data,
    title powinno być krótką nazwą opisującą rodzaj struktury
    TODO: dopisać testy
    TODO: Upewnić się że powiązania mięzy strukturą Node i Data nie są ścisłe'''
    base_file_path = pathlib.Path(path)
    base_file = File(base_file_path.name, base_file_path)
    base_node = Node(base_file, 'SCIEZKA')
    base_file.add_node(base_node)
    __map_path_iter(base_node)
    return base_node
def __map_path_iter(node):
    ''' Funkcja pomocnicza funkcji map path
    TODO: Dopisać test'''
    for file in node.data.adress.iterdir():
        sub_file = File(file.name, file)
        child_node = node.set_child(sub_file)
        sub_file.add_node(child_node)
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
