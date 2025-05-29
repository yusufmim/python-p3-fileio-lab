#def write_file(file_name, file_content):
 #   pass

#def append_file(file_name, append_content):
   # pass

#def read_file(file_name):
    #pass


# lib/file_io.py

def write_file(file_name, file_content):
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content + "\n")


def append_file(file_name, append_content):
    with open(f"{file_name}.txt", "a") as file:
        file.write(append_content + "\n")


def read_file(file_name):
    with open(f"{file_name}.txt", "r") as file:
        return file.read().strip()  # strip() removes trailing newline for cleaner output
