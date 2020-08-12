message = input("> Input a greeting: ")
words = message.split(" ")
emoji = {
    ":)": "Yippee!",
    ":(": "Oops!"
}
print(words)
output = ""
for word in words:
    output += emoji.get(word, word) + " "
print(output)

def greet_user():
    words = message.split(" ")
    emoji = {
        ":)": "Yippee!",
        ":(": "Oops!"
    }
    print(words)
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "

print("Start")
greet_user()
print(f"Stop {word}")
