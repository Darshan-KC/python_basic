# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

#   My name is Michele
# Then I would see the string:

#   Michele is name My
# shown back to me.

def reverse(sentence :str)->str:
    return sentence[::-1]

word = input("Enter a string : ")
print("The enter word is {}".format(word))

print("The word in backward order is ",reverse(word))