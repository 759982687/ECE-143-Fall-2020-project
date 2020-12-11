## Write by Zhizheng Qiao
'''
Initial dataset is from karggle "emojitweets-01-04-2018.txt"    
This dataset is a 1.18GB txt file and too large to upload. We divided this file in to three smaller files (emoji_1.txt,
emoji_2.txt, emoji_3.txt) for the data process convience. 
You can see the detail about this dataset in https://www.kaggle.com/rexhaif/emojifydata-en

'''
import numpy as np
import pandas as pd
import re
import emojis
import json
from textblob import TextBlob

##Collect all different kinds of emojis in the data set end then just seve the emoji list and their numbers
filename = "emoji_1.txt"
content = {}
print(1)
for line in open("emoji_1.txt",encoding='utf-16'): 
    for i in emojis.get(line):
        num = line.count(i)        
        if i not in content.keys():
            content[i] = num
        else:
            content[i] = content[i] + num
print(2)
for line in open("emoji_2.txt",encoding='utf-16'): 
    for i in emojis.get(line):
        num = line.count(i)        
        if i not in content.keys():
            content[i] = num
        else:
            content[i] = content[i] + num
print(3)
for line in open("emoji_3.txt",encoding='utf-16'): 
    for i in emojis.get(line):
        num = line.count(i)        
        if i not in content.keys():
            content[i] = num
        else:
            content[i] = content[i] + num
print(4)

# use pandas to process and seve the data
df = pd.DataFrame(data=content.keys(), columns=['emoji'])
df['count'] = content.values()
df.sort_values(by=['count'], ascending=False, inplace=True)
df.to_excel('Tweet.xlsx', sheet_name='Sheet1') 
df.to_csv('Tweet.csv')

#since the emoji data is too large, we chose top 200 common emojis to do the further analysis
#the top 200 emojis information is saved in save.json
myemoji = list(df['emoji'])
myemoji = myemoji[0:200]
save = {}
for i in myemoji:
    save[i] = content[i]
jsObj = json.dumps(save) 
 
fileObject = open('save.json', 'w') 
fileObject.write(jsObj) 
fileObject.close()


#do the analysis for the top 200 common emojis, use TextBolb do the sentiment analysis
#including eomji number, sentence polarity, sentence subjectivity, emoji position
cont = {}

for line in open("emoji_1.txt",encoding='utf-16'): 
    clean_tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", line).split())
    analysis = TextBlob(clean_tweet)
    polarity = round(analysis.polarity,5)
    subjectivity = round(analysis.subjectivity,5)
    for i in emojis.get(line):
        if i in save:
            num = line.count(i)
            position = round((line.find(i)/len(line)+line.rfind(i)/len(line))/2,5)

            if i not in cont.keys():
                cont[i] = [emojis.decode(i)]
                cont[i].append(num)
                cont[i].append([polarity])
                cont[i].append([subjectivity])
                cont[i].append([position])
            else:
                cont[i][1] = cont[i][1] + num
                cont[i][2].append(polarity)
                cont[i][3].append(subjectivity)
                cont[i][4].append(position)
print(1)
for line in open("emoji_2.txt",encoding='utf-16'): 
    clean_tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", line).split())
    analysis = TextBlob(clean_tweet)
    polarity = round(analysis.polarity,5)
    subjectivity = round(analysis.subjectivity,5)
    for i in emojis.get(line):
        if i in save:
            num = line.count(i)
            position = round((line.find(i)/len(line)+line.rfind(i)/len(line))/2,5)

            if i not in cont.keys():
                cont[i] = [emojis.decode(i)]
                cont[i].append(num)
                cont[i].append([polarity])
                cont[i].append([subjectivity])
                cont[i].append([position])
            else:
                cont[i][1] = cont[i][1] + num
                cont[i][2].append(polarity)
                cont[i][3].append(subjectivity)
                cont[i][4].append(position)
print(1)
for line in open("emoji_3.txt",encoding='utf-16'): 
    clean_tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", line).split())
    analysis = TextBlob(clean_tweet)
    polarity = round(analysis.polarity,5)
    subjectivity = round(analysis.subjectivity,5)
    for i in emojis.get(line):
        if i in save:
            num = line.count(i)
            position = round((line.find(i)/len(line)+line.rfind(i)/len(line))/2,5)

            if i not in cont.keys():
                cont[i] = [emojis.decode(i)]
                cont[i].append(num)
                cont[i].append([polarity])
                cont[i].append([subjectivity])
                cont[i].append([position])
            else:
                cont[i][1] = cont[i][1] + num
                cont[i][2].append(polarity)
                cont[i][3].append(subjectivity)
                cont[i][4].append(position)
print(1)

#save the result in data_all.json this file is also too large to upload (448 MB)
#we will use this file to do the analysis and plot
jsObj = json.dumps(cont) 
 
fileObject = open('data_all.json', 'w') 
fileObject.write(jsObj) 
fileObject.close()


