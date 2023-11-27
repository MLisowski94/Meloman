import file_managerv2 as fm
from pathlib import Path

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = fm.map_path(r"C:\Users\malis\Desktop\Doktorat")
    print(x.get_child_list())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
