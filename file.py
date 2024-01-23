class File:
    ''''Klasa zawierająca informacje na temat plików. Założenia:
    Zawiera informacje:
                    odnośnie lokalizacji pliku
                    odnośnie typu pliku
                    lista Node'ów w których skład wchodzi plik
    Jakie informacje wyrazić w postaci data a jakie w postaci relacji node?
    TODO: dodać kolejne klasy dziedziczące posiadające określone dane
    TODO: określić relacje pomiędzy node a file
    TODO: Czy file może modyfikować node?
    '''
    def __init__(self, name, adress):
        '''node list zawiera liste node'ow w sklad ktorych wchodzi file, dane te sa w postaci par
        składających się z tytułu Node i Node'''
        self.name = name
        self.data = {'adress': adress}
        self.node_list = []

    def __repr__(self):
        return f'Name: {self.name}, Adress: {self.data.get("adress")}'


    def add_node(self, node):
        '''Funkcja przeznaczona do dodawaniu węzłów w skład których wchodzi data, jako argument przyjmuje node
        TODO: Test
        '''
        self.node_list.append((node.title, node))

    def get_node_list(self):
        '''TODO: Test'''
        return self.node_list
    def check_file_format(self):
        pass

    def check_metadata(self):
        pass

