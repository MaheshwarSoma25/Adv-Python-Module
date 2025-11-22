import os

# print(os.name)
# print(os.getlogin())
# print(os.cpu_count())

# os.system("python --version")
# os.system("python tkinter-prac.py")
# os.system("mysql --version")
# print(os.getcwd())
# # os.chdir("/path")
# print(os.listdir("."))


from datetime import datetime

info = os.stat("tkinter-prac.py")
print(info.st_mtime)
print(datetime.fromtimestamp(info.st_mtime))

a = r"C:\Full Stack Python\BackEnd\Adv Python"
b = "New Folder"

print(os.path.join(a, b))