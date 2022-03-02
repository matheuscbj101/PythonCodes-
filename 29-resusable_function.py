def emoji_converter (message):
 words = message.split(" ")
 emojis = {
     ":)" : "😀"
 }
 output = ""
 for word in words:
     output += emojis.get(word, word) + " " #the second "word" is used when there isn´t a word with this name
 return output
message = input(">")
print (emoji_converter (message))
