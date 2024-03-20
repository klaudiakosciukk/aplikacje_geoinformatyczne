import czas
print("Hello World")
help(print)

from os import getcwd
current_path=getcwd()
print(current_path)
print(czas.aktualny_czas)

print(czas.aktualny_czas)
import time
time.sleep(20)

import importlib
import time

importlib.reload(time)
print(czas.aktualny_czas)