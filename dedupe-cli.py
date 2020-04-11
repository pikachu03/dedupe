import os
import hashlib
import operator

class DedupeObj:
    def __init__(self, path):
        self.path = path

    def dedupe(self):
        dedupe_helper(self.path)


def sha256(file):
    BLOCK_SIZE = 65536

    file_hash = hashlib.sha256()
    with open(file, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)

    return file_hash.hexdigest()


def sort_table(table, cols):
    for col in reversed(cols):
        table = sorted(table, key=operator.itemgetter(col))
    return table

def dedupe_helper(path):
    universe = []
    sub_a = []

    def read_files(p):
        print("Reading though files...\n")
        for file in os.listdir(p):
            if file[0] != '.':
                if os.path.isdir(p + "/" + file):
                    read_files(p + "/" + file)
                if os.path.isfile(p + "/" + file):
                    file_path = p + "/" + file
                    file_size = (os.path.getsize(file_path))
                    # print(file_path + "\n")
                    universe.append([file_size, file_path])
    read_files(path)

    universe = sort_table(universe, [0])

    def sort_files():
        print("\nSorting files by size...\n")
        for i in range(len(universe)):
            if i == 0:
                sub_a.append([universe[i]])
            if not i == 0:
                if universe[i][0] > universe[i-1][0]:              
                    sub_a.append([universe[i]])
                if universe[i][0] == universe[i-1][0]:
                    sub_a[len(sub_a)-1].append(universe[i])
    sort_files()

    def calculate_hashes():
        print("Calculating hashes...\n")
        temp = sub_a
        for i in range(len(sub_a)):                          
            for j in range(len(sub_a[i])):
                if not len(sub_a[i]) == 1:
                    temp_hash = sha256(sub_a[i][j][1])
                    print("Calculating hash for " + sub_a[i][j][1])
                    print("    " + str(temp_hash) + "\n")
                    temp[i][j].append(temp_hash)
        return temp

    sub_b = calculate_hashes()

    def give_results():
        seen_files = []
        dupes = []
        outputs = open(path + "/DUPLICATES.txt", "w")
        for i in range(len(sub_b)):
            for j in range(len(sub_b[i])):
                if len(sub_b[i]) > 1:
                    if not sub_b[i][j][2] in seen_files:
                        seen_files.append(sub_b[i][j][2])
                    else:
                        dupes.append(sub_b[i][j])
        if len(dupes) == 0:
            print("You have no duplicates in this folder!")
            outputs.write("You have no duplicates in this folder!")
        else:
            total_dupe_size = 0
            for l in range(len(dupes)):
                for m in range(len(dupes[l])):
                    outputs.write(" " + str(dupes[l][m]))
                    total_dupe_size += dupes[l][0]
                    # print(" " + str(dupes[l][m]))
                outputs.write("\n")

            print("\nYou have " + str(len(dupes)) + " duplicates for a total of " + str(total_dupe_size) + " bytes")
            print("Find a full list of duplicates at " + path + "/DUPLICATES.txt\n\n\n")
    give_results()


path = input("enter the full path of the direcory you want to dedupe surrounded by single quotes: ")
dedupeObj = DedupeObj(path)
dedupeObj.dedupe()