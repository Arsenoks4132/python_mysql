from sys import argv
s = "No arguments (By python)"
if len(argv) > 1:
    s = argv[1]
print(s)