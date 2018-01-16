msg = "CAMELCASE GENERATOR PROGRAM"
stars = '*' * len(msg)
print('\n', stars, '\n', msg, '\n', stars, '\n')

print('Your sentence will have its first word converted to lower case')
print('The following words will have the first letter capitalized')

# Ask the user for a sentence
# Initialize an empty string variable
sentence = input("Enter a sentence: ")
newSentence = ''
# Split the sentence into a list of words
myWords = sentence.split()
# Loop over the list of words, remove white spaces
# Convert the first word to lower case
# The following words have the first character Uppercase only
for x in myWords:
    if (x == myWords[0]):
        newSentence += x.lower()
    elif (x != myWords[0]):
        newSentence += x.capitalize()
print(newSentence)

