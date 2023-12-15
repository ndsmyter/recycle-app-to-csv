import json

year = 2023
f = open("calendar%s.csv" % year, "w")

f.write("Subject,Start Date,End Date,All Day Event,Description\n")
with open('json%s.txt' % year) as json_file:
    data = json.load(json_file)
    items = data['items']
    for item in items:
        # print item["fraction"]["name"]["nl"]
        f.write("\"%s\",\"%s\",\"%s\",True,\"%s\"\n" % (item["fraction"]["name"]["nl"], item["timestamp"][0:10], item["timestamp"][0:10], item["fraction"]["logo"]["name"]["nl"]))


f.close()
