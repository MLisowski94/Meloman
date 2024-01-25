from pathlib import Path
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
        '''
        Adres musi być podany jako obiekt klasy Path
        node list zawiera liste node'ow w sklad ktorych wchodzi file, dane te sa w postaci par
        składających się z tytułu Node i Node'''
        if not isinstance(adress, Path):
            raise TypeError("adress musi być obiektem klasy Path")
        if not adress.exists():
            raise ValueError("pod podanym adresem nie istnieje plik")
        self.name = name
        self.data = {'adress': adress}
        self.node_list = []

    def __repr__(self):
        return f'Name: {self.name}, Adress: {self.data.get("adress")}'

    def change_file_adress(self, new_adress):
        '''TODO: Dopisać test
        Należy podać adres ścieżki na której ma znaleźć się plik, komenda ta nie zmienia nazwy pliku
        jedynie jego lokalizajce'''
        print(new_adress)
        print(new_adress.is_dir())
        if not isinstance(new_adress, Path):
            raise TypeError("adress musi być obiektem klasy Path")
        if not new_adress.is_dir():
            print('exist')
            print(new_adress)
            new_adress.mkdir()
        updated_location = new_adress/self.data['adress'].name
        self.data['adress'].replace(updated_location)

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

