# ask user tu input numner and print it in words

numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Ten",

}

entry = input("Phone: ")
words = ''

for number in entry:
    #words += numbers[number] + ' ' # if there is no matching entry terminates
    words += numbers.get(number, ' ') + ' '
print(words)


####### Emoji converter

message = input('>')
words = message.split(' ') # separator string
emojis = {
    ":)": "😊",
    ":(": "🙁"
}
output = ''
for word in words:
    output += emojis.get(word, word) + " "

print(output)