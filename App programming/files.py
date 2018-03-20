# How to handle data in a file?
#     Data from an opened file can be read using any of the methods: read, readline and readlines.
#     Data can be written to a file using either write or writelines method.
#     A file must be opened, before it is used for reading or writing.

#     A file mus be closed after performing all operations needed on it
#
fp = open('temp.txt','a')
#content = fp.read()
#print(content)
new_line = 'This is a new line'
fp.writelines(new_line)


#fp = open('temp.txt','a')
fp = open('temp.txt','r')
content = fp.read()
print(content)
#new_line = 'This is a new line'
#fp.writelines(new_line)

#print(content)
fp.close()

#syntax
#file_obj = open(file_name [,access_model][,buffering])
#access mode = Refers to the mode in which the file has to be opened
#buffering = Number of bytes that can be flushed to a file
#file_obj.close()

#Opening a file
fo = open('sample.txt', 'w')
print('The name of opened file is :', fo.name)

#closing a file
fo.close()
