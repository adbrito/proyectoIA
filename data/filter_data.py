
# Python program to read
# json file


import json

# Opening JSON file
file_data = open('b.json', "r", encoding='utf-8')

file_output = open('data.csv', "w", encoding='utf-8')

file_output.write("date,content\n")

for i in file_data:
    # returns JSON object as
    # a dictionary
    data = json.loads(i)
    date = data["date"]
    content = data["content"]
    if (date != None and content != None and len(content) > 0):

        content_list = content.split(" ")

        line_filter = []
        for s in content_list:

            # remove hastags, mentions and links
            if(s.count("#")>0 or s.count("@")>0 or s.count("https:")>0 or s.count("http:")>0):
                break
            line_filter.append(s)

        line_filter_s = " ".join(line_filter)
        line_filter_s = line_filter_s.replace("\n", " ")

        if(len(line_filter_s) > 0):
            line = date+","+line_filter_s+"\n"
            file_output.write(line)


# Closing file
file_data.close()
