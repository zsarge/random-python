"""
this file takes all of the files found in the directory
"unjoined" and joines them all together in a file named
"joined.json" in the filepath "joined".

THIS FILE WILL LIKELY NOT WORK ON WINDOWS,
as I join files for a linux system
"""


from secret import unjoined, joined
import json
import os

newfile = {}
filepaths = []
joined_messages = []

def parse(content):
	messages = content["messages"]
	for message in messages:
		joined_messages.append(message)

# for all files
for filename in os.listdir(unjoined):
	if filename.endswith(".json"):
		filepath = f"{unjoined}/{filename}"
		with open(filepath) as f:
			parse(json.load(f))

newfile["messages"] = joined_messages

with open(f"{joined}/joined.json", 'w') as f:
	f.write(json.dumps(newfile))


print(f"joined {len(joined_messages)} messages")

