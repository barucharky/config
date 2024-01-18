# B"H

# config-file-link-creator

import pathlib
import os
import filecmp

from pydantic import BaseSettings, BaseModel
from typing import List, Optional

class Settings(BaseSettings):
    HOME_DIR: pathlib.PosixPath
    HOME_CONFIG: pathlib.PosixPath
    BACKUP_DIR: pathlib.PosixPath
    CONFIG_DIR: pathlib.PosixPath
    IGNORE: pathlib.PosixPath

    class Config:
        env_file = '.env'

settings = Settings()

# Test functions

# Check if directory was created
def check_dir(
    dir: pathlib.PosixPath
):

  if dir.is_dir():
      print(f'{dir} created successfully')

  else:
      raise Exception(f'{dir} not created :)')

# Check if file was created
def check_file(filename):

    if filename.is_file():
        print(f'{filename} created successfully')

    else:
        raise Exception(f'{filename} not created :(')

"""### Functions for checking file contents"""

def line_by_line(filename):

    file = open(filename, 'r')
    Lines = file.readlines()

    for line in Lines:
        print(line.strip())

def check_files(dir):

    for file in sorted(dir.glob('*')):

      if file.is_file():
          print(f'{file}: {file.read_text()}')

# Bring contents of path_ignore_file into a list of PosixPaths
class Paths(BaseModel):
    paths: List[pathlib.PosixPath] = None

with open(settings.IGNORE) as file:
    path_ignore_list = Paths(
        paths = [line.rstrip() for line in file]
        )

# Check the path and create the link or directory as appropriate

def create_path(
    source_path: pathlib.PosixPath,
    destination_path: pathlib.PosixPath,
    path_ignore_list: List[pathlib.PosixPath]
) -> bool:

    if source_path not in path_ignore_list:

        if source_path.is_dir():

            if not destination_path.is_dir():

                print(f"Creating {destination_path}...")
                destination_path.mkdir()
                check_dir(destination_path)

            return True

        elif destination_path.is_file():

            if filecmp.cmp(source_path, destination_path, shallow=False):

                destination_path.unlink()
                os.link(source_path, destination_path)
                check_file(destination_path)

                return False

            else:

                overwrite = input(f"{destination_path} exists with different contents from {source_path}. Overwrite?")

                if overwrite in ["y", "Y"]:

                     destination_path.unlink()
                     os.link(source_path, destination_path)
                     check_file(destination_path)

                return False

        else:

            os.link(source_path, destination_path)
            check_file(destination_path)

    else:
        print(f"{source_path} is in 'ignore' list")
        return False

# Create all the paths recursively
def create_all_paths(
    source_path: pathlib.PosixPath,
    destination_path: pathlib.PosixPath,
    path_ignore_list: pathlib.PosixPath
) -> None:

    for path in sorted(source_path.glob('*')):

        working_path = (destination_path / path.relative_to(settings.BACKUP_DIR))

        if create_path(path, working_path, path_ignore_list):
            create_all_paths(path, destination_path, path_ignore_list)

create_all_paths(settings.BACKUP_DIR, settings.HOME_DIR, path_ignore_list.paths)