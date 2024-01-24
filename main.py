import file_managerv2 as fm
from pathlib import Path
import file

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # x = fm.map_path(r"C:\Users\malis\Desktop\Doktorat")
    # print(x.data.get_node_list())
    # lista = x.get_ascendant_list()
    # for y in lista:
    #     print("{0}\n".format(y))
    y = Path.cwd()/"test.txt"
    # y.mkdir()

    y.touch()
    filex = file.File('x', y)
    filex.change_file_adress(Path.cwd()/"test")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
