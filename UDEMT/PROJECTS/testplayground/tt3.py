print("i am tt3.py")
print("i am tt3.py")
print("i am tt3.py\n")
print("print('i am tt3.py')")

import subprocess

# result = subprocess.run(['lls', '-liud'], stdout=subprocess.PIPE)
# print(result.stdout.decode('utf-8'))

result = subprocess.run("ls -l",shell=True,stdout=subprocess.PIPE)
print(result.stdout.decode('utf-8'))

print("do u hear me?")