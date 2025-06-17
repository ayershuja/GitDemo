


# if we dont want to use file.close everytime so whe use below with, it automatically open and close the file
with open('test.txt', 'r') as reader:
    content=reader.readlines()
    reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)