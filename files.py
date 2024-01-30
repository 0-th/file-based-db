import json
import os
from typing import Dict
import sys


def create_file(filename: str, outer_dict_struct: Dict = {}) -> None:
    if os.path.isfile(path=f"./db_files/{filename}.json"):
        print(f"{filename} file already exists")

        recreate_file_response = input(
            f"Do you want to re-create {filename}? Enter [Y]es | [N]o: "
        ).lower()

        if recreate_file_response.startswith('y'):
            print(f"Re-creating {filename} file...")
            os.remove(path=f"./db_files/{filename}.json")
        elif recreate_file_response.startswith('n'):
            print("===Quitting===")
            sys.exit()
        else:
            print("Invalid Response")
            sys.exit()

    # create file
    with open(file=f"./db_files/{filename}.json", mode='x') as db_file:
        json.dump(obj=outer_dict_struct, fp=db_file)


def read_file(filename: str) -> Dict:
    with open(file=f"./db_files/{filename}.json", mode='r') as db_file:
        return json.load(fp=db_file)


def update_file(filename: str, new_filename: str) -> None:
    """Change file name"""
    try:
        os.rename(
            src=f"./db_files/{filename}.json",
            dst=f"./db_files/{new_filename}.json"
        )
    except FileNotFoundError:
        print(f"The file {filename} doesn't exist.\n")
        sys.exit()

def delete_file(filename: str):
    deleted_file_response = input(
        f"{filename} would be deleted? Enter [Y]es or [N]o: "
    ).lower()
    if deleted_file_response.startswith('y'):
        os.remove(f"./db_files/{filename}.json")
        print(f"{filename} deleted\n")
    elif deleted_file_response.startswith('n'):
        print(f"{filename} is preserved")
        sys.exit()
    else:
        print(f"{deleted_file_response} is an invalid response. Quitting")
        sys.exit()
