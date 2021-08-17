
# Python program to read
# json file
  
  
import json
  
# Opening JSON file
file_data = open('b.json',"r",encoding='utf-8')
  
file_output = open('data.csv',"w",encoding='utf-8')

file_output.write("date,content\n")

for i in file_data:
    # returns JSON object as
    # a dictionary
    data = json.loads(i)
    date = data["date"]
    content = data["content"]
    if (date != None and content != None and len(content)!=0):

        content_list=content.split(" ");

        line_filter=[]
        for s in content_list:
            
            # remove hastags and mentions
            if(s.startswith("#") or s.startswith("@")):
                break
            line_filter.append(s)

        line_filter_s = " ".join(line_filter)

        line = date+","+line_filter_s.replace("\n"," ")+"\n"
        file_output.write(line)
    
  
# Closing file
file_data.close()
