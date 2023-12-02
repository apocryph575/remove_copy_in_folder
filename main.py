import os


def find_and_print_result_file():
    files = os.listdir(".")
    for file_name in files:
        file_path = os.path.join(".", file_name)
        if "thumb" in file_path:
            os.remove(file_path)


if __name__ == "__main__":
    find_and_print_result_file()
