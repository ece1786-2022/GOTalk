text = ''
with open(textfile, 'rt') as file_in:
    for line in file_in:
        text = text + line