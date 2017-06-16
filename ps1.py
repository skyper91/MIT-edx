### Ratio An
### Within 1 hour

# Problem 1
# 10.0 points possible (graded)
#
# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
# For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5

s = 'azcbobobegghakl'
valid_vowels = 'aeiou'
num_vowels = 0
for c in s:
    if c in valid_vowels:
        num_vowels += 1
print("Number of vowels:", num_vowels)

# Problem 2
# 10.0 points possible (graded)
#
# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2

s = 'bbazcbzbegghaklbob'
search_term, first, count = "bob" ,0 ,0
while s.find(search_term, first) != -1:
    count += 1
    first = s.find(search_term, first) + 1
print("Number of times bob occurs is:", count)

# Problem 3
# 15.0 points possible (graded)

# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters
# occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print
# "Longest substring in alphabetical order is: beggh"
#
# In the case of ties, print the first substring.
# For example, if s = 'abcbcd', then your program should print
# "Longest substring in alphabetical order is: abc"



s = 'azcbobobegghakl'
longest_str = None
for i in range(len(s)):
    current_str = s[i]
    while (i+1) < len(s) and s[i] <= s[i+1]:
        current_str += s[i+1]
        i += 1
    if longest_str == None or len(current_str) > len(longest_str):
        longest_str = current_str
print("Longest substring in alphabetical order is:", longest_str)
