# path should be a .json file produced by https://github.com/Tyrrrz/DiscordChatExporter
# deadnames should be a dictionary of strings to replace, going from the string to replace to the string you want
from secret import path, deadnames
import json

with open(path) as f:
      content = json.load(f)

message_lengths = []

# load all messages
for chat in content["messages"]:
	message_lengths.append(len(chat["content"]))

# replace the deadnames of my trans friends
def remove_deadnames(names):
    real_names = []
    for deadname in deadnames:
        for username in names:
            if deadname == username:
                real_names.append(deadnames[deadname])
            else:
                real_names.append(username)

    return real_names

def get_message_with_length(n):
	for chat in content["messages"]:
		if len(chat["content"]) == n:
			return chat["content"]

def get_messages_with_length(n):
	messages = []
	for chat in content["messages"]:
		if len(chat["content"]) == n:
			messages.append(chat["content"])
	return messages

def print_occurences(dic, s):
    print(f"{len(dic)} messages found with {s}")
    criminals = {}
    for i in dic:
        try:
            criminals[i] += 1
        except:
            criminals[i] = 1
    # sort by value:
    criminals = dict(sorted(criminals.items(), key=lambda item: item[1], reverse=True))

    print(f"times \t- name")
    print(f"---------------")
    for i in criminals:
        print(f"{criminals[i]} \t- {i}")

def get_author_of_message(message_content):
    authors = []
    for chat in content["messages"]:
        if chat["content"] == message_content:
            authors.append(chat["author"]["name"])
    authors = remove_deadnames(authors)
    if len(authors) > 1:
        print()
        print_occurences(authors, message_content)
    return authors[0]

def get_author_of_message_with(message_content):
    authors = []
    for chat in content["messages"]:
        if message_content.lower() in chat["content"].lower():
            authors.append(chat["author"]["name"])
    authors = remove_deadnames(authors)
    if len(authors) > 1:
        print()
        print_occurences(authors, message_content)
    return authors[0]

def average(a):
    n = len(a)
    # Find sum of array element
    sum = 0
    for i in range(n):
        sum += a[i]
    return sum//n;

def get_number_of_vowels():
    count = 0
    vowels = ['a','e','i','o','u']
    for chat in content["messages"]:
        for v in vowels:
            count += chat["content"].count(v)
    return count

print(f"Average length: {average(message_lengths)} characters")
print()
print(f"Number of messages in all channels: {len(message_lengths)}")

max_len = max(message_lengths)
longest_message = get_message_with_length(max_len)
print()
print(f"longest message is {len(longest_message)} characters long ({longest_message[:10]}...)")
print(f"which was said by {get_author_of_message(longest_message)}")

#  quirky_bois = get_messages_with_length(69)
#  for i in quirky_bois:
    #  print(f"quirkiest messages = {i} \n\t^^ by: {get_author_of_message(i)}")

#  print(f"owo -- {get_author_of_message('owo')}")
#  print(f"owo -- {get_author_of_message_with('owo')}")

print()
print(":___ Curse Word Statistics ___:")
get_author_of_message_with("owo")
get_author_of_message_with("shit")
get_author_of_message_with("fuck")
get_author_of_message_with("poop")
get_author_of_message_with("heck")
get_author_of_message_with("trump")
get_author_of_message_with("beep")
get_author_of_message_with("boop")

print()
print(f"Number of vowels: {get_number_of_vowels()}")


