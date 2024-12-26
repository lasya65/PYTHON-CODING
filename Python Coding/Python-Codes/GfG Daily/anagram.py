#This is a code to check whether two strings are anagrams of each other or not.\
#An anagram of a string is another string that contains same characters, only the order of characters can be different.\
def areAnagram(str1, str2):
    # If lengths of both strings are not same, they cannot be anagram
    if len(str1) != len(str2):
        return False

    # Sort both strings and compare
    return sorted(str1) == sorted(str2)

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if areAnagram(str1, str2):
    print("The two strings are anagram of each other")
else:
    print("The two strings are not anagram of each other")