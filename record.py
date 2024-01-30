import json
import sys
from typing import Any, Dict, Union


def create_record(
    filename: str, data: Dict[Any, Any] = {}
) -> None:
    try:
        with open(file=f"./db_files/{filename}.json", mode='r+') as file:
            parsed_file_records = {}
            try:
                parsed_file_records = json.load(fp=file)
            except json.JSONDecodeError:  # file contain wrong json
                with open(
                    file=f"./db_files/{filename}.json", mode='x+'
                ) as file:
                    json.dump(obj={}, fp=file, indent=4, sort_keys=True)
            idx = len(parsed_file_records) + 1
            file.seek(0)  # overwritten file from the first line
            parsed_file_records[idx] = data
            json.dump(
                obj=parsed_file_records, fp=file, indent=4, sort_keys=True
            )
            file.truncate()  # remove old_data that isn't overwritten
            # with `json.dump()`
    except FileNotFoundError:
        print(f"File {filename} doesn't exist.\n")


def update_record(
    idx: int, key: Union[str, int], value: Any, filename: str
) -> Dict:
    """Update a single record by its index"""
    record_to_be_updated = {}
    try:
        with open(file=f"./db_files/{filename}.json", mode="r+") as file:
            parsed_records = json.load(fp=file)
            try:
                record_to_be_updated = parsed_records[str(idx)]
                if record_to_be_updated.get(str(key), None):
                    record_to_be_updated[str(key)] = value
                else:
                    print(f"{key} doesn't exist in {record_to_be_updated}")
                    sys.exit()
            except KeyError:
                print(f"No record exists at index {idx}")
                sys.exit()
            file.seek(0)  # ensure file is overwritten from first line
            json.dump(obj=parsed_records, fp=file, indent=4, sort_keys=True)
            file.truncate()  # remove leftover records that weren't overwritten
    except FileNotFoundError:
        print("File {filename} not found.\n")

    return record_to_be_updated


def read_record(idx: int, filename: str) -> Dict:
    """Return a single record by it's index"""
    parsed_records = {}
    try:
        with open(file=f"./db_files/{filename}.json", mode='r') as file:
            parsed_records: Dict = json.load(fp=file)
    except FileNotFoundError:
        print("File {filename} not found.\n")

    return parsed_records.get(str(idx), None)


def delete_record(idx: int, filename: str) -> None:
    """Delete a single record"""
    try:
        with open(file=f"./db_files/{filename}.json", mode='r+') as file:
            parsed_records: Dict = json.load(fp=file)
            if parsed_records.get(str(idx), None):
                parsed_records.pop(str(idx))
            else:
                print("Index {idx} doesn't exist\n")
            file.seek(0)  # move file pointer to first line before overwriting
            json.dump(obj=parsed_records, fp=file, indent=4, sort_keys=True)
            file.truncate()  # remove leftover records
    except FileNotFoundError:
        print("File {filename} not found.\n")
