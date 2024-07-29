wd = input('Enter word ')
print("Original String:", wd)
size = len(wd)
print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", wd[i])
