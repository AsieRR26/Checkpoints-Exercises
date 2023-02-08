# Exercise 7: Get the first word from your string using indexes. Use the upper function to
# transform the letters into uppercase. Create a new string that takes the uppercase word and the
# rest of the original string.

string = 'Beautiful piano music for studying'

first = string[:9].upper()

new_string = first + string[9:]

print(new_string)