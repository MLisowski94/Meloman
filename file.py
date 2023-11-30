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

