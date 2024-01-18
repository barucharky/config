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
class Settings(BaseSettings):
    HOME_DIR: pathlib.PosixPath
    HOME_CONFIG: pathlib.PosixPath
    BACKUP_DIR: pathlib.PosixPath
    CONFIG_DIR: pathlib.PosixPath
    IGNORE: pathlib.PosixPath

    class Config:
        env_file = '.env'

settings = Settings()

# Function to check if dir created successfully

def check_dir(
    dir: pathlib.PosixPath
) -> bool:

  if dir.is_dir():
      print(f'{dir} created successfully')
      return True
  else:
      print(f'{dir} not created :)')
      return False

# Function to check if link created successfully

def check_file(
    filename: pathlib.PosixPath
) -> bool:

    if filename.is_file():
        print(f'{filename} created successfully')
        return True
    else:
        print(f'{filename} not created :(')
        return False

"""# Now the script that will create all the directories and links

Added types for parameters

Check to see if the link already exists

https://www.geeksforgeeks.org/python-os-path-islink-method/
"""

def create_link(
    source: pathlib.PosixPath,
    destination: pathlib.PosixPath
) -> None:

    if str(source) not in ignore.read_text():
        print("path_ignore_file link...")
        os.link(source, destination)
        check_file(destination)
    else:
        print(f"{source} is in path ignore list")

def make_all(
    source: pathlib.PosixPath,
    destination: pathlib.PosixPath
) -> None:

  for path in sorted(source.glob('*')):

      working_path = (destination / path.relative_to(settings.BACKUP_DIR))

      if path.is_dir():
          if not str(working_path) in settings.IGNORE.read_text():
              if not (working_path).is_dir():
                  print(f"making directory for {path}")
                  (working_path).mkdir()
                  check_dir(working_path)

              make_all(path, destination)
          
          else:
              print(f'{working_path} is in path ignore list')

      else:
          if path.relative_to(settings.BACKUP_DIR).is_file():
              if os.stat(path.relative_to(settings.BACKUP_DIR)).st_nlink == 1:
                  print(f"{path.relative_to(settings.BACKUP_DIR)} exists, but is not linked. Overwrite? (y/n)")
                  answer = input()
                  if answer == "y" or answer == "Y":
                      path.relative_to(settings.BACKUP_DIR).unlink()
                      create_link(path, (working_path))
              else:
                  print("Link {path.relative_to(settings.BACKUP_DIR)} already exists")
          else:
              create_link(path, (working_path))

make_all(settings.BACKUP_DIR, settings.HOME_DIR)