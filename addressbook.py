""" Address Book app - sorts/filters/stores contact details from a txt file """
import re

names_file = open("names.txt", encoding = "utf-8")
data = names_file.read()
names_file.close()


#last_name = r"Ballard"
#first_name = r"George"
#print(re.match(last_name, data))
#print(re.search(first_name, data))

line = re.compile(r'''
    ^(?P<name>(?P<last>[-\w ]*), \s(?P<first>[-\w ]+))\t  # Last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # Phone Numbers
    (?P<job>[\w\s]+,\s[\w\s.]+)\t? # Job and company
    (?P<twitter>@[\w\d]+)?$ # Twitter
''', re.X|re.MULTILINE)


#print(line.search(data).groupdict())

for match in line.finditer(data):
    print("{first} {last} <{email}>".format(**match.groupdict()))
    
