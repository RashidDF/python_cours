from pathlib import Path

# print(type(Path))

cwd = Path('.')
cwd2 = Path('E:/') / 'Formation' / 'Python' / 'python_cours' / 'Examples'
# print(cwd)
# print(isinstance(cwd, Path))
# print(type(cwd))
# print(Path.__subclasses__())
# print(dir(cwd))
# print(cwd.absolute())

print(cwd2.exists())

if not cwd2.exists():
    cwd2.mkdir()

print(cwd2.exists())

if cwd2.exists():
    cwd2.rmdir()

print(cwd2.exists())
