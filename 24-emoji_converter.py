message = input (">")
words = message.split(' ')
emojis = {
    ":)" : "😀"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " " #the second "word" is used when there isn´t a word with this name
print (output)