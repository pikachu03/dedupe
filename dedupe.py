import os
import hashlib
import operator

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname) as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def sort_table(table, cols):
    for col in reversed(cols):
        table = sorted(table, key=operator.itemgetter(col))
    return table


def dedupe(p1, p2=''):
    universe = []
    sub_a = []
    path = p1

    def u(p):
        print("Reading though files...\n")
        for file in os.listdir(p):
            if not file[0] is '.':
                if os.path.isdir(p + "/" + file):
                    u(p + "/" + file)
                if os.path.isfile(p + "/" + file):
                    file_path = p + "/" + file
                    file_size = (os.path.getsize(file_path))
                    print(file_path + "\n")
                    universe.append([file_size, file_path])
    u(path)

    universe = sort_table(universe, [0])

    def a():
        print("\nSorting files by size...\n")
        for i in range(len(universe)):
            if i == 0:
                sub_a.append([universe[i]])
            if not i == 0:
                if universe[i][0] > universe[i-1][0]:              
                    sub_a.append([universe[i]])
                if universe[i][0] == universe[i-1][0]:
                    sub_a[len(sub_a)-1].append(universe[i])
    a()

    def b():
        print("Calculating hashes...\n")
        temp = sub_am
        for i in range(len(sub_a)):                          
            for j in range(len(sub_a[i])):
                if not len(sub_a[i]) == 1:
                    temp_hash = md5(sub_a[i][j][1])
                    print("Calculating hash for " + sub_a[i][j][1])
                    print("    " + temp_hash + "\n")
                    temp[i][j].append(temp_hash)
        return temp

    sub_b = b()

    def move_dupes():
        seen_files = []
        dupes = []
        outputs = open("Output.txt", "w")
        for i in range(len(sub_b)):
            for j in range(len(sub_b[i])):
                if len(sub_b[i]) > 1:
                    if not sub_b[i][j][2] in seen_files:
                        seen_files.append(sub_b[i][j][2])
                    else:
                        # UNCOMMENT THIS CODE IF YOU WANT DEDUPE TO MOVE DUPLICATE FILES TO p2
                        # IT WILL LEAVE ONE COPY OF THE FILE IN ITS ORIGINAL LOCATION
                        # new_name_components = sub_b[i][j][1].split("/")
                        # new_name = ''
                        # _, ext = os.path.splitext(sub_b[i][j][1])
                        # for k in range(len(new_name_components)):
                        #     if not k == (len(new_name_components)-1):
                        #         new_name += new_name_components[k] + ">"
                        #     else:
                        #         new_name += new_name_components[k]
                        dupes.append(sub_b[i][j])
                        # os.rename(sub_b[i][j][1], p2 + "/" + new_name + ext)
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

            print("\nYou have " + str(len(dupes)) +
                  " duplicates for a total of " +
                  str(total_dupe_size) + " bytes")
    move_dupes()


dedupe(input("Enter the path of the folder you want to dedupe."
             "Note, the file path must be surrounded by single of double quotes. \n")
       # UNCOMMENT THIS CODE IF YOU WANT DEDUPE TO MOVE DUPLICATE FILES TO p2
       # input("Enter the path of the folder you want duplicates to be moved to."
       )
