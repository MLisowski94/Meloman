
def deafult_function(x,y):
    return True
class Node:
    '''Klasa stanowiaca wezel. Załozenia:
    *dziecko moze mieć tylko jednego rodzica
    *rodzic może mieć dowolnie wiele dzieci
    *dziecko musi być dokładnie o jeden poziom wyżej niż rodzic
    *wyabstrahowanie z przechowywanych danych jedynie ich struktury
    *title zawiera informacje o tym jakie dane ma przedstawiać dany node
    TODO: stworzyć interfejs przekazujący do data informacje o tym że wchodzi w skład Node
    '''
    def __init__(self, data, title, level=0, parent=None):
        self.data = data
        self.title = title
        self.level = level
        self.parent = parent

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
        sprawdzając przy tym czy typy danych się zgadzają. Zapobiega to bałaganowi'''

        if type(child_data) is not type(self.data):
            raise TypeError("Child data - {0} is not the same as parent data {1}".format(type(child_data), type(self.data)))

        child = Node(child_data, self.title, self.level+1, parent=self)
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

