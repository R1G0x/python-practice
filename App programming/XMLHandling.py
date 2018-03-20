#XML is a generalized way of describing 
#hierarchical structured data

#An XML document contains one or more elements,
#which are delimited by start and end tags.

#Elements can be nested to any depth

#The first element in every XML document
#is called the root element

#Elements can have attributes, which are name-value
#pairs.

#Attributes are listed within the start tag
#of an element and separated by whitespace

#Elements may or may not have text content

#Python can parse XML documents in several ways
#. It has traditional DOM and SAX parsers,
#but examples of using a feature rich module
#'lxml' (a third party module) are considered here.

#'lxml' module is highly feature rich
#with ElementTree API and supports 
#querying the xml content using XPATH

#In the ElementTree API, an element acts like
#a list. The items of the list are the element's children.
#The attributes of an element can be
#accessed as a Python dictionary

#XML search is faster with 'lxml'

#Python's support for XML is not limited to parsing
#existing documents. You can also create
#XML documents from scratch

#XML Parsing using lxml package:
from lxml import etree

tree = etree.parse('sample.xml')
root = tree.getroot()
skills = tree.findall('//skill')

print("Existing skillset of the employee:")
for skill in skills:
  print('SKILL :',skill.attrib['name'])
  
#adding new skill
skill = etree.SubElement(root,'skill', attrib={'name':'PHP'})
skills = tree.findall('//skill')

print("Skillset of the employee after adding a new skill:")
for skill in skills:
  print('SKILL :',skill.attrib['name'])
