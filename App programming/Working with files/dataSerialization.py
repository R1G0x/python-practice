#Data serialization
#Data types/objects -> pickle & JSON -> Transmittable / Storable format

#It is most common to use pickle, since there is a fast C implementation of it and it is integrated
#with some other modules that actually store the serialized data.
#However web-based applications prefer using json

#Serialized data -> written to -> File/Socket/Pipe -> Data can be deserialized -> New Object

#Using Pickle not all object can be pickled. Sockets, file handles, database connections and other objects
#with runtime state cannot be saved in a meaningful way.

#The file containing data serialized by pickle cannot be viewed as the serialized data is present in binary format.
#However, data serialized by json can be viewed

#using pickle
import pickle 

data = [  {'name': 'Rishi', 'Age':28, 'Desg':'ITA'},
          {'name': 'George', 'Age':32, 'Desg': 'AST'}
       ]

print('BEFORE Pickling: ', data)
with open('records.pickle','wb') as fo:
  pickle.dump(data,fo)

with open('records.pickle','rb') as fo:
  data_new = pickle.load(fo)
print('AFTER Pickling: ', data_new)

print('SAME? :',data is data_new)
print('EQUAL? :', data == data_new)

#Using JSON
import json

data = [  {'name': 'Rishi', 'Age':28, 'Desg':'ITA'},
          {'name': 'George', 'Age':32, 'Desg': 'AST'}
       ]

print('BEFORE ENCODING:', data)
with open('records.json', 'w') as fo:
  json.dump(data,fo, indent=2)
  
with open('records.json') as fo:
  data_new = json.load(fo)
print('AFTER ENCODING: ', data_new)

print('SAME? :', data is data_new)
print('EQUAL? :', data == data_new)