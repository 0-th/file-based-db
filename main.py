from typing import Union
from files import create_file, delete_file, read_file, update_file
from record import create_record, delete_record, read_record, update_record
import sys

# create_file(filename='test')
# create_record(filename='test', data={"name": 1, "gpa": 2})
# print(read_file(filename='test'))
# update_file(filename='test', new_filename='new_test')
# update_record(filename='new_test', idx=1, key='name', value='new_name')
# print(read_record(filename='new_test', idx=1))
# delete_record(idx=1, filename='new_test')
# print(read_file(filename='new_test'))


def crud_file_or_specific_record(operation: str) -> Union[str, None]:
    file_or_record_response = input(
        f"{operation} whole file or specific record?\n"
        "Enter (f)ile or (r)ecord: "
    ).lower()
    if not file_or_record_response.startswith(('f', 'r',)):
        print(f"{file_or_record_response} is an invalid response."
              "Try again.\n")
        return None
    return file_or_record_response


def main():
    while True:
        # data objects(file or records), crud operations are parsed by the
        # first character in the response
        file_operation_response = input(
            "\nWhat database operations would you want to perform?\n"
            "Enter (C)reate, (R)ead, (U)pdate, (D)elete, (Q)uit: "
        ).lower()

        # quit immediately
        if file_operation_response.startswith('q'):
            print("Quitting...\n")
            sys.exit()

        filename_response = input("What is your file's name: ")

        # create operation
        if file_operation_response.startswith('c'):
            if create_file_or_record_response := crud_file_or_specific_record(
                operation='Creation'
            ):
                if create_file_or_record_response.startswith('f'):
                    create_file(filename=filename_response)
                    print(f"{filename_response} created...\n")
                    continue
                elif create_file_or_record_response.startswith('r'):
                    record_fields = input(
                        "Input data fields of your records.\n"
                        "Separate multiple field names by space: "
                    ).split(sep=' ')
                    record = {}

                    # collect input and create record
                    for field in record_fields:
                        field_value = input(
                            f"Enter value of field '{field}': "
                        )
                        record[field] = field_value
                    create_record(filename_response, data=record)
                    print("Record created...\n")
                    continue
            else:
                # invalid response start loop all over
                continue

        # read operation
        elif file_operation_response.startswith('r'):
            read_file_or_record_response = crud_file_or_specific_record(
                'Read'
            )
            # if response isn't invalid
            if read_file_or_record_response:
                if read_file_or_record_response.startswith('f'):
                    print(f"{read_file(filename_response)}\n")
                    continue
                elif read_file_or_record_response.startswith('r'):
                    read_record_id = input(
                        "Enter id of record: "
                    )
                    record_to_be_displayed = read_record(
                        idx=int(read_record_id),
                        filename=filename_response
                    )
                    if record_to_be_displayed:
                        print(f"{record_to_be_displayed}\n")
                        continue
                    else:
                        print(
                            f"No record found with the id {read_record_id}\n"
                        )
                        continue
            # on invalid response start all over
            else:
                continue

        elif file_operation_response.startswith('u'):
            update_file_or_record_response = crud_file_or_specific_record(
                'Update'
            )

            if update_file_or_record_response:
                if update_file_or_record_response.startswith('f'):
                    new_filename_response = input(
                        "Enter new name for file: "
                    )
                    update_file(
                        filename_response, new_filename=new_filename_response
                    )
                    print(f"File name updated from {filename_response} "
                          f"to {new_filename_response}")
                    continue
                elif update_file_or_record_response.startswith('r'):
                    update_record_id = input(
                        "Enter id of record to be updated: "
                    )
                    update_record_key = input("Enter field to be updated: ")
                    update_record_value = input(
                        f"Enter value of field '{update_record_key}': "
                    )
                    update_record(
                        filename=filename_response,
                        idx=int(update_record_id),
                        key=update_record_key,
                        value=update_record_value
                    )
                    continue
            else:
                continue

        elif file_operation_response.startswith('d'):
            delete_file_or_record_response = crud_file_or_specific_record(
                'Delete'
            )

            if delete_file_or_record_response:
                if delete_file_or_record_response.startswith('f'):
                    delete_file(filename=filename_response)
                    continue
                elif delete_file_or_record_response.startswith('r'):
                    delete_record_id = input(
                        f"Enter the id of the record you want to delete from "
                        f"the {filename_response} file: "
                    )
                    delete_record(
                        filename=filename_response,
                        idx=int(delete_record_id)
                    )
                    print("Record deleted...\n")
                    continue
            else:
                continue
        else:
            print(f"{file_operation_response} is an invalid db operation."
                  "Try again.\n")
            continue


if __name__ == "__main__":
    print("Welcome to File-based DB")
    main()
