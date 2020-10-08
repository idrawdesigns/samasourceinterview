import json

#readfile
jsonfile = open("sample-json.json", 'r')
read_content = jsonfile.read()


#parseData

interview_access = json.loads(read_content)



save_data =[]

def get_unique_shape_types():
    for interview_data in interview_access:
        taggable_access = interview_data['taggable image']
        for taggable_data in taggable_access:
            shape_type = taggable_data["type"]
            save_data.append(shape_type)



get_unique_shape_types()
remove_duplicates = list(dict.fromkeys(save_data))
print('number of unique shapes', len(remove_duplicates))



