
import sys

def get_filename():
    filename = sys.argv[-1]

    if filename.split('.')[-1] != 'txt':
        raise ValueError("Input must be a text file")
    else:
        return filename

def split_elf_loads(filename):
    file = open(filename,'r')

    input_text = file.read()

    split_text = input_text.split('\n\n')

    elf_loads = []
    for load in split_text:
        this_load = []
        for item in load.split('\n'):
            try:
                 this_load.append(int(item))
            except:
                continue
        elf_loads.append(this_load)

    return elf_loads

def find_largest_load(elf_loads):

    largest_load = -1

    for load in elf_loads:
        if sum(load) > largest_load:
            largest_load = sum(load)

    return largest_load

def main():

    filename = get_filename()

    elf_loads = split_elf_loads(filename)

    largest_load = find_largest_load(elf_loads)

    print(largest_load)

if __name__ == "__main__":
    main()
