message = input(">")
words = message.split('   ')

emojis = {
    ":)": "Smile",
    ":(": "Sad"
}

output =""

for word in words:
    output += emojis.get(word, word) + " "
print(output)