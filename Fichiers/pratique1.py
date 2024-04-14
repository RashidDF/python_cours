from os import path
from pathlib import Path

print(path.abspath('.'))

print(Path('.').absolute())
print(Path.cwd())
