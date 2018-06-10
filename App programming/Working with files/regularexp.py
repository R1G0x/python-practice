#Regular expressions are useful to construct patterns that helps in filtering the text possesing the patterns
#The patterns are built using special chars and char classes
#Pattern | Description
#   ^    | Start of a string
#   $    | End of a string
#   b*   | Matches 0 or more ocurrences of preceding 'b' character
#   b+   | Matches 1 or more ocurrences of preceding 'b' character
#   b?   | Matches 0 or 1 ocurrence of preceding 'b' character
#   b{n} | Matches exactly n no. ocurrences of preceding 'b' char
#   b{n,}| Matches n or more ocurrences of preceding 'b' char
#  b{n,m}| Matches at least n and at most m ocurrence of 'b' char
#  a | b | Matches 'a' or 'b' 
#   .    | Match any character except new line
#[aeiou] | Matches any of the characters a,e,i,o,u
#[^aeiou]| Matches any character except a,e,i,o,u
#   \d   | Match a digit : [0-9]
#   \D   | Match a non digit : [^0-9]
#   \s   | Matches a white space character: [\t\r\n\f]
#   \w   | Matches a single word character: [A-Za-z0-9_]
#   \b   | Matches any word boundary character

#Finding patterns in Text
#re module is used in Python for dealing with regular expressions
#The search method takes the pattern and text to scan,and returns a Match object when the pattern is found
#If the pattern is not found , search() returns None
import re
patterns = ['this','that']
text = 'Does this text match the pattern?'

for pattern in patterns:
    print('Searching for "{}" in "{}"'.format(pattern,text))
    if re.search(pattern, text):
        print("Found a match!")
    else:
        print("No match!")

#The match object returned by search() holds information about the nature of the match
#which includes Original input string, Regular Expression, Location
import re
pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)
s = match.start()
e = match.end()
st = match.re.pattern
print('Found "{}" pattern, in "{}" from {} to {} '.format(st,text,s,e))

#Compiling Expressions

#  In Python, it is more efficient to compile the patterns that are used frequently
# The compile() function of re module converts an expression string into a RegexObject
import re

patterns = ['this','that']
text = 'Does this text match the pattern?'
regexes = [ re.compile(p) for p in patterns ]

for regex in regexes:
    print('Searching for "{}" in "{}" '.format(regex.pattern,text))
    if regex.search(text):
        print("found a Match!")
    else:
        print("No Match")


#Finding multiple matches
# the findall() function returns all of the substrings of the target string that match the pattern without overlapping

import re

pattern = 'ab'
text = 'abbaaabbbbaaaaa'

for match in re.findall(pattern,text):
    print('Found the match - {}'.format(match))


#Grouping the matches
#Adding groups to a pattern enables us to isolate parts of the matching text, expanding those capabilities to create
# a parser
# Groups are defined by enclosing patterns in parentheses 
import re

text = 'This is some text -- with punctuation.'

for pattern in [r'^(\w+)',# word at the start of string, word at end of string with punctuation, word starting with 't' and the next word ending with 't'
                r'(\w+)\S*$',           
                r'(\bt\w+)\W+(\w+)',
                r'(\w+t)\b'
                ]:
    regex = re.compile(pattern)
    match = regex.search(text)
    print(match.groups())


#Naming Grouped Matches
#Accesing the groups with defined names

import re

text = 'This is some text -- with punctuation.'

for pattern in [r'^(?P<first_word>\w+)',
                r'(?P<last_word>\w+)\S*$',
                r'(?P<t_word>\bt\w+)\W+(?P<other_word>\w+',
                r'(?P<ends_with_t>\w+t)\b'
                ]:
    regex = re.compile(pattern)
    match = regex.search(text)
    print("Groups:",match.groups())
    print("Group Dictionary:",match.groupdict())