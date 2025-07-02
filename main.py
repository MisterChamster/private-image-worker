from packages import ask_path, mainloop
from os import chdir


print("")
dir_main = ask_path()
chdir(dir_main)
print("")
mainloop()
