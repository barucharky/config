# B"H

"""Auto config

A script that moves all your config files from your repo into their proper places

It relies mainly on the `pathlib` library and partly on the `os` library.

Documentation for `pathlib` can be found at https://docs.python.org/3/library/pathlib.html

**Why hard links?**

https://www.geeksforgeeks.org/difference-between-hard-link-and-soft-link/

If the original files are deleted, hard links will remain functional.
"""

import pathlib
import os

# Your config files must exist in your repo in the same file structure as they will appear in your home directory

# Set home_dir to your home directory where you want the links to be created
home_dir = pathlib.Path('/home/baruch')

# Set backup_dir to the location of your config files in your repo
backup_dir = home_dir / 'backup'
exceptions = backup_dir / '.links_ignore'

# Function to check if dir created successfully

def check_dir(
    dir: pathlib.PosixPath
) -> bool:

    if dir.is_dir():
        print(f'{dir} created successfully')
        return True
    else:
        return False

# Function to check if link created successfully

def check_file(
    filename: pathlib.PosixPath
) -> bool:

    if filename.is_file():
        print(f'{filename} created successfully')
    else:
        print("File not found :(")

"""# Now the script that will create all the directories and links

Added types for parameters

Check to see if the link already exists

https://www.geeksforgeeks.org/python-os-path-islink-method/
"""

def create_link(
    source: pathlib.PosixPath,
    destination: pathlib.PosixPath
) -> None:

    if str(source) not in exceptions.read_text():
        print("Creating link...")
        os.link(source, destination)
        check_file(destination)
    else:
        print(f"{source} is in exceptions list")

def make_all(
    source: pathlib.PosixPath, 
    destination: pathlib.PosixPath
) -> None:

  for path in sorted(source.glob('*')):

      if path.is_dir():
        if not str(destination / path.relative_to(backup_dir)) in exceptions.read_text():
            if not (destination / path.relative_to(backup_dir)).is_dir():
                print(f"making directory for {path}")
                (destination / path.relative_to(backup_dir)).mkdir()
                check_dir(destination / path.relative_to(backup_dir))
            make_all(path, destination)

      else:
          if (destination / path.relative_to(backup_dir)).is_file():
              if os.stat(destination / path.relative_to(backup_dir)).st_nlink == 1:
                  print(f"{path.relative_to(backup_dir)} exists, but is not linked. Overwrite? (y/n)")
                  answer = input()
                  if answer == "y" or answer == "Y":
                      path.relative_to(backup_dir).unlink()
                      create_link(path, (destination / path.relative_to(backup_dir)))
              else:
                  print("Link {path.relative_to(backup_dir)} already exists")
          else:
              create_link(path, (destination / path.relative_to(backup_dir)))

make_all(backup_dir, home_dir)