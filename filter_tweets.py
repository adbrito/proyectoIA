
# Python program to read
# json file


import json
import csv
encoding_files = "utf-8"  # utf-8

# Opening JSON file
file_data = open('b.json', "r", encoding=encoding_files)

file_output = open('tweets.csv', "w", encoding=encoding_files, newline='')

header = ['date', 'content']

# write the header
writer = csv.writer(file_output)
writer.writerow(header)

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
            if(s.count("#") > 0 or s.count("@") > 0 or s.count("https:") > 0 or s.count("http:") > 0):
                continue
            line_filter.append(s)

        line_filter_s = " ".join(line_filter)

        if(len(line_filter_s) > 0):
            #date=" ".join(date.split("+"))
            # remove T and time location
            date=" ".join(date.split("T"))
            date=date.split("+")[0]

            #remove \n tweet adn tab
            #line_filter_s =line_filter_s.replace('\n'," ")
            line_filter_s =" ".join(line_filter_s.split("\n"))
            line_filter_s =" ".join(line_filter_s.split("\t"))
            
            
            line = [date, line_filter_s]
            writer.writerow(line)

# Closing file
file_data.close()
file_output.close()
