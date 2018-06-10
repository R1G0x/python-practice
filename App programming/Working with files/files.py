# How to handle data in a file?
#     Data from an opened file can be read using any of the methods: read, readline and readlines.
#     Data can be written to a file using either write or writelines method.
#     A file must be opened, before it is used for reading or writing.

#     A file mus be closed after performing all operations needed on it
#
#fp = open('temp.txt','a')
#content = fp.read()
#print(content)
#new_line = 'This is a new line'
#fp.writelines(new_line)


#fp = open('temp.txt','a')
#fp = open('temp.txt','r')
#content = fp.read()
#print(content)
#new_line = 'This is a new line'
#fp.writelines(new_line)

#print(content)
#fp.close()

#syntax
#file_obj = open(file_name [,access_model][,buffering])
#access mode = Refers to the mode in which the file has to be opened
#buffering = Number of bytes that can be flushed to a file
#By default, a file is opened is read mode
#file_obj.close()

#Opening a file in write mode
#fo = open('sample.txt', 'w')
#print('The name of opened file is :', fo.name)

#closing a file
#fo.close()

#Reading data 3 methods.
# read() reads all the file
fo = open('sample.txt')
content = fo.read()
print(content)
fo.close()

# readline() read a line
fo = open('sample.txt')
line = fo.readline()
fo.close()
print(line)
# readlines() read all lines, each line becomes an element from a list.
fo = open('sample.txt')
lines = fo.readlines()
fo.close()
print(lines)

#Writing data using 2 methods
#write()
fo = open('sample_out.txt','a')
content = 'Writing to a file.\n really easy\n'
fo.write(content)
fo.close()
#writelines() writes multiple lines at a time
fo = open('sample_out.txt','a')
lines = ['Python is a scripting or a high-level language.\n',
         'Python supports object oriented style of programming.\n']
fo.writelines(lines)
fo.close()