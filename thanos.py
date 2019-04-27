from sys import platform
import os
if platform == "win32":
    print("This System Technology detected as Windows")
    cd =os.chdir("C:/Users/")
    path = os.getcwd()
    print("Iron man founded Thanos on "+path)
    for i in range(1,100000):
        os.mkdir("Thanos" + str(i))
    print("Killed Thanos Successfully")
elif platform == "linux":
    print("This system is Linux")
    cd =os.chdir("/Desktop/")
    path = os.getcwd()
    print("Iron man founded Thanos on "+path)
    for i in range(1,100000):
        os.mkdir("Thanos" + str(i))
    print("Killed Thanos Successfully")
