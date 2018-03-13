# How to handle data in a file?
#     Data from an opened file can be read using any of the methods: read, readline and readlines.
#     Data can be written to a file using either write or writelines method.
#     A file must be opened, before it is used for reading or writing.

fp = open('temp.txt','a')
#content = fp.read()
#print(content)
new_line = 'This is a new line'
fp.writelines(new_line)
#print(content)
fp.close()