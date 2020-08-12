from pathlib import Path

#  Absolute path
# c:\Program File\Wimdows
#/usr/local/bin/
# Relative path

path = Path("ecommerce")
print(path.exists())

#path = Path("skill")
# print(path.rmdir()) #mkdir

path = Path()
for file in path.glob('*.py'):
    print(file)