from pathlib import Path

# Win
print(Path('E:/').joinpath('Users').joinpath('rashid'))
print(Path('E:/') / 'Users' / 'rashid')

# Mac and Unix
print(Path('usr').joinpath('local').joinpath('bin'))
print(Path('usr') / 'local' / 'bin')
