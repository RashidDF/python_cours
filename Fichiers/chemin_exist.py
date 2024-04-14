from pathlib import Path

absolute_path = 'E:/Formation/Python/python_cours/Fichiers'
print(Path(absolute_path).exists())

relative_path = 'Fichiers/chemin_exist.py'
print(Path(relative_path).exists())

print(Path(absolute_path).is_file())
print(Path(absolute_path).is_dir())
print(Path(relative_path).is_file())

for f in Path('./Fichiers').iterdir():
    print(f)
