# path should be a .json file produced by https://github.com/Tyrrrz/DiscordChatExporter
from secret import path
import json

print(path)

with open(path) as f:
      content = json.load(f)

message_lengths = []

for chat in content["messages"]:
	message_lengths.append(len(chat["content"]))

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
    print()
    print(f"times \t- name")
    print(f"---------------")
    for i in criminals:
        print(f"{criminals[i]} \t- {i}")

def get_author_of_message(message_content):
    authors = []
    for chat in content["messages"]:
        if chat["content"] == message_content:
            authors.append(chat["author"]["name"])
    if len(authors) > 1:
        print_occurences(authors, message_content)
    return authors[0]

def get_author_of_message_with(message_content):
    authors = []
    for chat in content["messages"]:
        if message_content in chat["content"]:
            authors.append(chat["author"]["name"])
    if len(authors) > 1:
        print_occurences(authors, message_content)
    return authors[0]

def average(a):
    n = len(a)
    # Find sum of array element
    sum = 0
    for i in range(n):
        sum += a[i]
    return sum/n;

print(f"average length - {average(message_lengths)}")
print(f"number of messages - {len(message_lengths)}")

max_len = max(message_lengths)
longest_message = get_message_with_length(max_len)
print(f"longest message = {longest_message}")
print(get_author_of_message(longest_message))

#  quirky_bois = get_messages_with_length(69)
#  for i in quirky_bois:
    #  print(f"quirkiest messages = {i} \n\t^^ by: {get_author_of_message(i)}")

print(f"owo -- {get_author_of_message('owo')}")
print(f"owo -- {get_author_of_message_with('owo')}")
