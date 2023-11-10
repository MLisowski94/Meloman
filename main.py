import file_manager as fm
from pathlib import Path

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # adres = r'C:\Users\malis\Desktop\HP_1120'
    # print(adres)
    plik = fm.Folder(r'C:\Users\malis\Desktop\Muzyka\Elektroniczna')
    plik.print_map()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
