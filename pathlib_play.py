# B''H

# pathlib practice
# documentation for pathlib can be found at:
# https://docs.python.org/3/library/pathlib.html

import os
import pathlib

print(pathlib.Path.cwd())

start_dir = pathlib.Path('/home/baruch/test')
path = pathlib.Path(start_dir / 'test001.txt')
path.write_text("it makes new files!!!")
print(path.read_text())

print("just path:")
print(path)
print("resolve():")
print(path.resolve())

print("---")

print(path.name)
print(path.parent)
print(path.stem)
print(path.suffix)
print(path.anchor)

pfile = (path.parent.parent / ('delete_me' + path.suffix))
pfile.write_text("it worked!")

# ----------

print("path:")
print(path)
print("relative_to:")
print(path.relative_to('/home/baruch'))
print("parts:")
print(path.relative_to('/home/baruch').parts)

# ----------

print("---")

print("Listing file names before replace():")

def lsfiles():
    the_files = sorted(path.parent.glob('*'))

    for file_name in the_files:
        print(file_name.name)


lsfiles()

# ----------

destination = start_dir / pfile.name

if not destination.exists():
    pfile.replace(destination)

path.replace(path.with_suffix('.md'))

print("Listing file names after replace()")

lsfiles()

print("---")

# ---------

def tree(directory):
    print(f'+ {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        print(f'{spacer}+ {path.name}')

tree(start_dir)

# ---------

print("---")

print("checking if file with os library\n")

print("check if file:")

print(f"is {destination} a file?")
print(os.path.isfile(destination))
print("is the directory a file?")
print(os.path.isfile(pathlib.Path.cwd()))

print("\nchecking if directory with pathlib library\n")

print(f"is {destination} a file?")
print(destination.is_file())
print("is the directory a file?")
print(pathlib.Path.cwd().is_file())

print("check if pplink is a link")
linkpath = start_dir / 'pplink'
print(linkpath.is_symlink())

# ---------

path.with_suffix('.md').unlink()
destination.unlink()

print("\n---\n")
print("make then delete new dir")

new_dir = start_dir / 'test_dir'
new_dir.mkdir()

lsfiles()

new_dir.rmdir()

print("after deleting dir")

lsfiles()