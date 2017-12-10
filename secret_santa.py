import sys
import os
import zipfile
from random import shuffle


def create_assigment(items):
    """
    Creates a random cyclic assignment of the input items.

    :param items: items that should be assigned
    :return: assigment as dict
    """

    if not items:
        raise AssertionError("At least one argument is required.")

    shuffle(items)
    first = items.pop()
    current = first

    assignment = {}
    for item in items:
        assignment[current] = item
        current = item

    # close circle
    assignment[current] = first

    return assignment


def save_assigment(assigment, save_folder=""):
    """
    Saves the assignment in separate ZIP files. Each ZIP file contains
    a text file that contains the item that was assigned.

    :param assigment: the assigment
    :param save_folder: the folder where ZIP files are saved.
    :return:
    """

    save_folder = save_folder.strip()

    if "/" is not save_folder[-1]:
        save_folder = save_folder + "/"

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    for key, value in assigment.items():
        zip_filename = save_folder + key + ".zip"
        with zipfile.ZipFile(zip_filename, mode='w') as zip_file:
            zip_file.writestr(key + ".txt", value)


def main():
    save_location = "assignment"
    items = sys.argv[1:]
    print("Assigning items.")
    assigment = create_assigment(items)
    print("Saving assignments in: {}".format(save_location))
    save_assigment(assigment, save_location)
    print("Success created assigments and created ZIP files.")


if __name__ == "__main__":
    main()
