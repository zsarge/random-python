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
    def remove_deadname(name):
        if name in deadnames.keys():
            return deadnames[name]
        else:
            return name
    names = list(map(remove_deadname, names))
    return names

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
        if chat["content"].lower() == message_content.lower():
            authors.append(chat["author"]["name"])
    authors = remove_deadnames(authors)
    if len(authors) > 1:
        print()
        print_occurences(authors, message_content)
    return authors[0]

def get_people_who_said(message_content):
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
print()
print(f"Number of vowels: {get_number_of_vowels()}")
print()
print("___ Curse Word Statistics ___")
get_people_who_said("owo")
get_people_who_said("shit")
get_people_who_said("fuck")
get_people_who_said("poop")
get_people_who_said("heck")
get_people_who_said("trump")
get_people_who_said("beep")
get_people_who_said("boop")


