# A RegEx, or Regular Expression, is a sequence of characters
#  that forms a search pattern.

# RegEx can be used to check if a string contains the
#  specified search pattern.


# Python has a built-in package called re,
#  which can be used to work with Regular Expressions.

# Import the re module:

import re

# # The findall() function returns a list 
# containing all matches.

# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)

#--------------------------
# The search() function searches the string 
# for a match, 
# and returns a Match object if there is a match.

# If there is more than one match, only
#  the first occurrence
#  of the match will be returned:


# txt = "The rain in Spain"
# x = re.search("ai", txt)
# print(x)
# print('''The first space character 
# is located in position:''', x.start())


#-------------
# # []	A set of characters	"[a-m]"
# txt = "Th1e raI3in in Sp7ain"
# print(txt)
# #Find all lower case characters 
# # alphabetically between "a" and "m":
# x = re.findall("[a-zA-Z]", txt)
# print(x)

#---------------------
#Replace all white-space characters with 
# the digit "9":

# txt = "The rain in Spain"
# print(txt)
# x = re.sub("\s", "9", txt,2)
# print(x)

#------------------------------

# # Replace the first 2 occurrences:

# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt, 2)
# print(x)

#-----------------------

# 7ww

#---------------------
# txt = "Th5e ra20in in1 Spain"
# print(txt)
# # #Check if the string has any 0, 1, 2, or 3 digits:

# x = re.findall("[0123]", txt)  #"az" [a-z] "[az]"
 
# print(x)

#----------------------------

# # # ^	Starts with
# txt = " rain The in Spain"
# x = re.findall("^The", txt)
# print(x)
# if x:
#   print("Yes, the string starts with 'hello'")
# else:
#   print("No match")

#-----------------
# txt = "The rain in Spain"
# print(txt)
# #Check if the string has other characters than a, r, or n:
# x = re.findall("[^arn]", txt)
# print(x)
#-----------------------rrrr

# $	Ends with	"world$
# txt = "hello world"
# #Check if the string ends with 'world':
# x = re.findall("d$", txt)
# print(x)
# if x:
#   print("Yes, the string ends with 'world'")
# else:
#   print("No match")

#-----------------------------
# # Print the position (start- and end-position) of
#  the first match occurrence.

# # The regular expression looks for any words 
# # that starts with an upper case "S":

# txt = "The  Sain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x)
# print(x.start())
# print(x.span())
# print(x.string)
# print(x.group())

# #-----------------------------

# # #The string property returns the search string:

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.string)


# #------------------------------


# # # Print the part of the string where there was a match.

# # # The regular expression looks for any words
# #  that starts with an upper case "S"


# # txt = "The rain in Spain"
# # x = re.search(r"\bS\w+", txt)
# print(x.group())

#-----------------------------
# Metacharacters
#----------------------------

# # {}	Exactly the specified number of
# #  occurrences

# txt = "The ralin in Spain falls mainly in the plain!"
# # # # #Check if the string contains "a" followed
# # # #  by exactly two "l" characters:

# x = re.findall("al{2}", txt)
# print(x)


#----------------------------------
# –––
#-------------------------------------------

# \A	Returns a match if the specified characters 
# are at the beginning of the string	"\AThe"	
	
# \d	Returns a match where the string 
# contains digits (numbers from 0-9)	"\d"
# 	
# \D	Returns a match where the string
#  DOES NOT contain digits	"\D"	

# \s	Returns a match where the string
#  contains a white space character	"\s"
# 	
# \S	Returns a match where the string 
# DOES NOT contain a white space character	"\S"
# 	
# \w	Returns a match where the string 
# contains any word characters (characters from a to Z,
#  digits from 0-9, and the underscore _ character)	"\w"
# 	
# \W	Returns a match where the string
#  DOES NOT contain any word characters	"\W"
# 	
# \Z	Returns a match if the specified 
# characters are at the end of the string

txt = " rain The in S#pai_7"
x = re.findall("n\Z", txt)
print(x)