import json

f = open("calendar2021.csv", "w")

f.write("Subject,Start Date,End Date,All Day Event,Description\n")
with open('json2021.txt') as json_file:
    data = json.load(json_file)
    items = data['items']
    for item in items:
        # print item["fraction"]["name"]["nl"]
        f.write("%s,%s,%s,True,%s\n" % (item["fraction"]["name"]["nl"], item["timestamp"][0:10], item["timestamp"][0:10], item["fraction"]["logo"]["name"]["nl"]))


f.close()
