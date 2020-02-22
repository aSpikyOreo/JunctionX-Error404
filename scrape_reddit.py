import praw
import json

#mental health dictionary for scraping different subreddits
mh_dict = {
    'hard':['depression','Anxiety','autism','ptsd','ADHD'],
    'soft':['Stress','ImposterSyndrome','FamilyIssues','schoolproblems']
}

client_id = "xTHf-JvXZkbHuA"
client_secret = "Qc8w4_YpH5rf1LRMImujwogqA80"
user_agent = "Ami"
username = "praw1729"
password = "$w1r7a2p9$"

reddit = praw.Reddit(client_id = client_id,
                     client_secret = client_secret,
                     user_agent = user_agent,
                     username = username,
                     password = password)

for type in mh_dict:
    print('*'*30)
    print(type+'\n')
    print('*'*30)
    for i in range(len(type)):
        title = mh_dict[type][i]
        subred = reddit.subreddit(title)
        hot_python = subred.hot(limit=5)
        for submission in hot_python:
            if not submission.stickied:
                #print(submission.title)
                print('Title: {}, ups: {}, downs: {}, Have we visited: {}'.format(
                    submission.title,
                    submission.ups,
                    submission.downs,
                    submission.visited))


# for cat in mh_dict:
#     for subred in mh_dict[cat]:
#         response = requests.get("https://www.reddit.com/r/" + subred + "/")
#         content = BeautifulSoup(response.content, "html.parser")
#         print(content.title)
