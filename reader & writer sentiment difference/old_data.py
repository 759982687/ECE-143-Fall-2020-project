import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import sys
import os
import emoji

### Load the files as pd.Database ###
# Reader vs Writer
temp3 = pd.read_csv(os.path.join(sys.path[0], '__readervswriter.csv'))
# Emoji Table
temp4 = pd.read_csv(os.path.join(sys.path[0], 'ijstable.csv'))
# Employee questionaire votes
temp5 = pd.read_csv(os.path.join(sys.path[0], 'votes_cleaned.csv'))

# Matplotlib formatting to allow the emojis to be displayed on the plot
prop = FontProperties(fname = 'C:\\Windows\\Fonts\\seguiemj.ttf')

# Substitute Emoji List of incorrect names with correct names
emoji_list = []
error_list =[':dancing_woman:',':person_raising_both_hands_in_celebration:', ':clapping_hands_sign:',':christmas_tree:',':multiple_musical_notes:',':thumbs_up_sign:',
            ':face_throwing_a_kiss:', ':face_with_stuck-out_tongue_and_winking_eye:',':ok_hand_sign:',':wrapped_present:',':person_with_folded_hands:',':thumbs_down_sign:',
            ':disappointed_but_relieved_face:',':face_with_cold_sweat:']

sub_list = [':woman_dancing:',':raising_hands:',':clapping_hands:',':Christmas_tree:',':musical_notes:',':thumbs_up:',':face_blowing_a_kiss:', ':winking_face_with_tongue:',
            ':OK_hand:',':wrapped_gift:',':folded_hands:',':thumbs_down:',':sad_but_relieved_face:',':downcast_face_with_sweat:']

for i in range(len(temp3['description'])):
    if ':'+str(temp3['description'][i]).lower().replace(' ','_')+':' not in error_list:
        emoji_list.append(emoji.emojize(':'+str(temp3['description'][i]).lower().replace(' ','_')+':'))
        # emoji_list.append(emojis.encode(':'+str(temp3['description'][i]).lower().replace(' ','_')+':'))
    else:
        ind = error_list.index(':'+str(temp3['description'][i]).lower().replace(' ','_')+':')
        emoji_list.append(emoji.emojize(sub_list[ind]))
        # emoji_list.append(emojis.encode(sub_list[ind]))

# Sort list
sort_list = sorted(zip(temp3['diff'], temp3['description']))
# print(sort_list)

# Second Emoji List for emoji table pd file
emoji_list2 = []
for i in range(len(temp4['Unicode name'])):
    if ':'+str(temp4['Unicode name'][i]).lower().replace(' ','_')+':' not in error_list:
        emoji_list2.append(emoji.emojize(':'+str(temp4['Unicode name'][i]).lower().replace(' ','_')+':'))
        # emoji_list.append(emojis.encode(':'+str(temp3['description'][i]).lower().replace(' ','_')+':'))
    else:
        ind = error_list.index(':'+str(temp4['Unicode name'][i]).lower().replace(' ','_')+':')
        emoji_list2.append(emoji.emojize(sub_list[ind]))


# Plots Emoji Count
# p1 = plt.bar(range(len(temp3['s.writer'])),temp3['count'])
# for rect1, label in zip(p1, emoji_list):
#     height = rect1.get_height()
#     plt.annotate(
#         label,
#         (rect1.get_x() + rect1.get_width()/2, height),
#         ha="center",
#         va="bottom",
#         fontsize=15,
#         fontproperties=prop
#     )
# plt.title("Emoji Count")
# plt.ylabel("Frequency")
# plt.show()

### Plots Writer Sentiment and Reader Sentiment ###
width = 0.35
fig, ax = plt.subplots()
x = np.arange(len(temp3['s.writer']))
rects1 = ax.bar(x - width/2, temp3['s.writer'], width, label='Writer Sentiment')
rects2 = ax.bar(x + width/2, temp3['s.reader'], width, label='Reader Sentiment')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Happiness Level')
ax.set_title('Happiness Level Based on Emojis Used')
ax.set_xticks(x)
ax.set_xticklabels(x)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect , label in zip(rects, emoji_list):
        height = rect.get_height()
        if height < 0:
            height = height - 0.05
        ax.annotate(label,
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontproperties = prop)


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()
plt.show()

### Plots sentiment difference between writer and reader for each emoji ### 
p1 = plt.bar(x,temp3['diff'])
plt.title("Difference Between Write and Reader Sentiment")
plt.ylabel("Difference")
for rect1, label in zip(p1, emoji_list):
    height = rect1.get_height()
    if height < 0:
        height = height - 0.03
    plt.annotate(
        label,
        (rect1.get_x() + rect1.get_width()/2, height),
        ha="center",
        va="bottom",
        fontsize=15,
        fontproperties=prop
    )
plt.show()

### Plots the standard deviation for each emoji ###
p1 = plt.bar(x,temp3['sd'])
plt.title("Standard Deviation Between Write and Reader Sentiment")
plt.ylabel("SD")
for rect1, label in zip(p1, emoji_list):
    height = rect1.get_height()
    if height < 0:
        height = height - 0.05
    plt.annotate(
        label,
        (rect1.get_x() + rect1.get_width()/2, height),
        ha="center",
        va="bottom",
        fontsize=15,
        fontproperties=prop
    )
plt.show()

### Plot top 19 Sentiment score, and frequency ###
test = temp4['Sentiment score'].tolist()
test = [str(i) for i in test]
test2 = temp4['Unicode name'].tolist()
test2 = [str(i) for i in test2]
test3 = temp4['Occurrences'].tolist()
test3 = [i for i in test3]

top_15_sentiment = test[1:18]
top_15_name = test2[1:18]
top_15_count = test3[1:18]
top_15_sentiment.reverse()
top_15_name.reverse()
top_15_count.reverse()

# top_15_sentiment.insert(0,0)
top_15_count.insert(0,'0')
# print(top_15_name[3])
# sorted_list = sorted(zip(top_15_count, top_15_name, top_15_sentiment), reverse = True)
# for i in range(len(sorted_list)):
#     top_15_count[i], top_15_name[i], top_15_sentiment = sorted_list[i]
emj_list = []
for i in range(len(top_15_name)):
    if ':'+str(top_15_name[i]).lower().replace(' ','_')+':' not in error_list:
        emj_list.append(emoji.emojize(':'+str(top_15_name[i]).replace(' ','_')+':'))
        # emoji_list.append(emojis.encode(':'+str(temp3['description'][i]).lower().replace(' ','_')+':'))
    else:
        ind = error_list.index(':'+str(top_15_name[i]).replace(' ','_')+':')
        emj_list.append(emoji.emojize(sub_list[ind]))
# width = 0.35
# fig, ax = plt.subplots(
# top_15_count[0] = 0
x = np.arange(len(top_15_name))
# rects1 = ax.bar(x - width/2, top_15_count, width, label='Frequency')
# rects2 = ax.bar(x + width/2, top_15_sentiment, width, label='Sentiment')

# Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('Happiness Level')
# ax.set_title('Happiness Level Based on Emojis Used')
# ax.set_xticks(x)
# ax.set_xticklabels(x)
# ax.legend()


# worst_15_sentiment = test[-15:]
# worst_15_name = test2[-15:]
# worst_15_count = test3[-15:]
### TOP 15 Sentiment and Occurance ###
# for i in range(len(top_15_sentiment)):
#     top_15_sentiment[i] = float(top_15_sentiment[i])
# p1 = plt.bar(x, top_15_sentiment)
# plt.ylabel('Sentiment')
# plt.title('Sentiment Level of Emojis')
# for rect1, label in zip(p1, emj_list):
#     height = rect1.get_height()
#     if height < 0:
#         height = height - 0.05
#     plt.annotate(
#         label,
#         (rect1.get_x() + rect1.get_width()/2, height),
#         ha="center",
#         va="bottom",
#         fontsize=15,
#         fontproperties=prop
#     )
# plt.show()
# top_15_name.insert(0,'')
# emj_list = []
# for i in range(len(top_15_name)):
#     if ':'+str(top_15_name[i]).lower().replace(' ','_')+':' not in error_list:
#         emj_list.append(emoji.emojize(':'+str(top_15_name[i]).replace(' ','_')+':'))
#         # emoji_list.append(emojis.encode(':'+str(temp3['description'][i]).lower().replace(' ','_')+':'))
#     else:
#         ind = error_list.index(':'+str(top_15_name[i]).replace(' ','_')+':')
#         emj_list.append(emoji.emojize(sub_list[ind]))
# x = np.arange(len(top_15_count))
# p1 = plt.bar(x, top_15_count)
# plt.ylabel('Occurance')
# plt.title('Occurrance of Emojis')
# for rect1, label in zip(p1, emj_list):
#     height = rect1.get_height()
#     plt.annotate(
#         label,
#         (rect1.get_x() + rect1.get_width()/2,height*np.sign(height)),
#         ha="center",
#         va="bottom",
#         fontsize=15,
#         fontproperties=prop
#     )
# plt.show()

### "How happy are you at work today?" votes ### 
employee_num = temp5['employee']
votes = temp5['vote']
# print(len(votes))
employees = []
for i in employee_num:
    if i not in employees:
        employees.append(i)

# print(len(employees))
employee_votes = np.zeros((len(employees), len(votes)))

# for i in range(len(employee_num)):
#     ind = employees.index(employee_num[i])
#     employee_votes[ind, i] = votes[i]
votes1 = np.zeros((len(votes),4))
count1 = 0
count2 = 0
count3 = 0
count4 = 0
for i in range(len(votes)):
    if votes[i] == -1:
        votes1[i,0] = -1
        count1 += 1
    elif votes[i] == -0.5:
        count2 += 1
        votes1[i,1] = -0.5
    elif votes[i] == 0:
        count3 += 1
        votes1[i,2] = 0
    else:
        count4 += 1
        votes1[i,3] = 1
x_label = [-1,-0.5,0,1]
y_label = [count1, count2, count3, count4]
p1 = plt.bar(x_label, y_label, width = 0.3)
plt.ylabel('Votes')
plt.title('How Happy Are You at Work Today?')
plt.xlabel('Sentiment')
emj_temp_list = [':frowning_face:',':slightly_frowning_face:',':neutral_face:',':grinning_face_with_big_eyes:']
emj_temp_list = [emoji.emojize(i) for i in emj_temp_list]
for rect1, label in zip(p1, emj_temp_list):
    height = rect1.get_height()
    plt.annotate(
        label,
        (rect1.get_x() + rect1.get_width()/2, height),
        ha="center",
        va="bottom",
        fontsize=25,
        fontproperties=prop
    )
# plt.bar(range(len(votes)), votes1[:,0])
# plt.bar(range(len(votes)), votes1[:,1])
# plt.bar(range(len(votes)), votes1[:,2])
# plt.bar(range(len(votes)), votes1[:,3])
plt.show()
# width = 0.35
# fig, ax = plt.subplots()
# x = np.arange(len(top_15_sentiment))
# rects1 = ax.bar(x - width/2, top_15_sentiment, width, label='Writer Sentiment')
# rects2 = ax.bar(x + width/2, top_15_count, width, label='Reader Sentiment')

# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('Happiness Level')
# ax.set_title('Happiness Level Based on Emojis Used')
# ax.set_xticks(x)
# ax.set_xticklabels(x)
# ax.legend()
# plt.show()

# def autolabel(rects):
#     """Attach a text label above each bar in *rects*, displaying its height."""
#     for rect , label in zip(rects, emoji_list):
#         height = rect.get_height()
#         ax.annotate(label,
#                     xy=(rect.get_x() + rect.get_width() / 2, height),
#                     xytext=(0, 3),  # 3 points vertical offset
#                     textcoords="offset points",
#                     ha='center', va='bottom',
#                     fontproperties = prop)


# autolabel(rects1)
# autolabel(rects2)

# plt.bar(test2[:40], test[:40])
# plt.show()