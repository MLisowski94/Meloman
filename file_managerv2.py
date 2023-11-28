import pathlib
from pathlib import Path

"""
Założenia wstępne
TODO: określić dokładnie api File i Node
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
        self.node_list = []

    def __repr__(self):
        return f'Name: {self.name}, Adress: {self.adress}'


    def add_node(self, node):
        '''Funkcja przeznaczona do dodawaniu węzłów w skład których wchodzi data, jako argument przyjmuje
        pare składająca się z tytułu Node i Node
        TODO: Test'''
        self.node_list.append((node.title, node))

    def get_node_list(self):
        '''TODO: Test'''
        return self.node_list
    def check_file_format(self):
        pass

    def check_metadata(self):
        pass


class Node:
    '''Klasa stanowiaca wezel. Załozenia:
    *dziecko moze mieć tylko jednego rodzica
    *rodzic może mieć dowolnie wiele dzieci
    *dziecko musi być dokładnie o jeden poziom wyżej niż rodzic
    *wyabstrahowanie z przechowywanych danych jedynie ich struktury
    TODO: Rozpisać strukture przy pomocy UML
    TODO: stworzyć interfejs przekazujący do data informacje o tym że wchodzi w skład Node
    TODO: Zastanowić się czy condition function jest potrzebny
    '''
    def __init__(self, data, title, level=0, parent=None, condition_function=lambda x, y: True,):
        self.data = data
        self.title = title
        self.level = level
        self.parent = parent
        ''' Condition_function to funkcja która musi zostać spełniona by stworzyć children node       
        Opisać warunki dla condition function'''

        self.condition = condition_function
        self.children_list = []

    def __repr__(self):
        return f'Node {self.title}-- Level: {self.level}, Data:({self.data})'


    # def add_child(self, child_node):
    #     '''Do przemyślenia czy ta funkcja jest potrzebna, może wprowadzać tylko bałagan'''
    #     if child_node.get_level() != (self.get_level() + 1):
    #         raise ValueError("Child level must be exactly one bigger than parents")
    #     child_node.abandon_parent()
    #     self.children.append(child_node)

    def set_child(self, child_data):
        '''Metoda tworząca nowy węzeł-dziecko
        sprawdzając przy tym czy typy danych się zgadzają. Zapobiega to bałaganowi
        TODO: dopisać test sprawdzajaca zgodność tytułów'''

        if type(child_data) is not type(self.data):
            raise TypeError("Child data - {0} is not the same as parent data {1}".format(type(child_data), type(self.data)))
        if self.condition:
            child = Node(child_data, self.title, self.level+1, parent=self, condition_function=self.condition)
            self.children_list.append(child)
            return child

    def get_level(self):
        return self.level

    def get_child_list(self):
        return self.children_list

    def get_ascendant_list(self):
        '''Funkcja zwracająca liste wszystkich potomków, nie tylko dzieci
        TODO: test'''
        ascendant_list = []
        for sub_node in self.children_list:
            ascendant_list.append(sub_node)
            if len(sub_node.children_list) > 0:
                ascendant_list = ascendant_list + sub_node.get_ascendant_list()
        return ascendant_list

    def get_data(self):
        return self.data

    def get_parent(self):
        return self.parent
    def abandon_parent(self):
        if self.parent is not None:
            self.parent.children_list.remove(self)
            self.parent = None

    def is_child_of(self, another_node):
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

    def does_data_belong_node(self, data):
        '''Funkcja zwracająca wartość True lub False w zależności od tego czy
        argument należy do Node
        TODO: Dopisać testy'''
        if data == self.data:
            return True
        else:
            return False



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
