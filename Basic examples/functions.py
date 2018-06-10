zenPython = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
# Convert the entire string zenPython into a list of words. Capture the words in the list - words.
# Hint: Use split method of strings. You may type python3.5 to use the latest version for the exercise
words = zenPython.split(' ')
# Now, remove the flanking characters (such as , . - * ! and space) from each of the word, present in list words.
# Store the obtained result again in the list words.
# Hint: Use List comprehensions and strip method of strings. You may type python3.5 to use the latest version for the exercise
auxWords = [char.strip() for char in words]

# Convert all the words of list words to lower case.
# Store the obtained result again in the list words.
# Hint: Use list comprehensions and lower method of strings. You may type python3.5 to use the latest version for the exercise


# Determine the unique set of words from the list words.
# Store obtained unique words in the list unique_words.
# Hint: Use set function You may type python3.5 to use the latest version for the exercise


# Calculate the frequency of each identified unique word in the list - words and store the result in the dictionary word_frequency.
# Hint: Use dictionary comprehensions and count method of lists. You may type python3.5 to use the latest version for the exercise


# Create the dictionary frequent_words, which filter words having frequency greater than five from word_frequency.
# Finally print the dictionary frequent_words.
# Hint : Use Dictionary comprehensions You may type python3.5 to use the latest version for the exercise


# Define the generator function fib_gen, which is capable of yielding values of infinite fibonacci series.
# For e.g : You should able to create a generator fs from fib_gen and if fs is 
# accessed using next for four times, then it should yield values 0, 1, 1, 2. 
# You may type python3.5 to use the latest version for the exercise


# Define the generator function factorial_gen, which is capable of yielding factorial values of natural numbers.
# For e.g : You should able to create a generator fs from factorial_gen and if fs is accessed using 
# next for five times, then it should yield values 1, 1, 2, 6,24, 120,... You may type python3.5 
# to use the latest version for the exercise


