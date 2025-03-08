try:
    with open('sample.txt', 'r') as file:
        contents = file.read()
        print("Contents of the file:")
        print(contents)
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")

with open('newfile.txt', 'w') as file:
    file.write("This is a new file, like New Year New Me XD.\n")
    print("\nNew file created with content:")

with open('newfile.txt', 'r') as file:
    newfile_contents = file.read()
    print(newfile_contents)