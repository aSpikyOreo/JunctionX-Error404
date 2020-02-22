import praw
import json

#mental health dictionary for scraping different subreddits
mh_dict = {
    'hard':['depression','Anxiety','autism','ptsd','ADHD'],
    'soft':['Stress','ImposterSyndrome','FamilyIssues','friendship']
}

#config information, temporary reddit account
client_id = "xTHf-JvXZkbHuA"
client_secret = "Qc8w4_YpH5rf1LRMImujwogqA80"
user_agent = "Ami"
username = "praw1729"
password = "$w1r7a2p9$"

#set up reddit client
reddit = praw.Reddit(client_id = client_id,
                     client_secret = client_secret,
                     user_agent = user_agent,
                     username = username,
                     password = password)
list_of_items = []
# types = string, string, int, string, [string]
#fields = ('title','id','score','subreddit','comments')
#go through subreddits in above dict
with open('data.json', 'w') as f:
    for type in mh_dict:
        print('*'*30)
        print(type+'\n') #what type of mental health issue is it
        print('*'*30)
        for i in range(len(mh_dict[type])):
            #get the subreddit
            sr = mh_dict[type][i]
            print('/'*25)
            print('SUBREDDIT: {}'.format(sr))
            subred = reddit.subreddit(sr)
            #limit submissions to maximum 3 per subreddit
            submissions = subred.hot(limit=3)
            for submission in submissions:
                #get the non sticky ones
                if not submission.stickied:
                    sub_dict = {}
                    sub_dict['title'] = submission.title
                    sub_dict['id'] = submission.id
                    sub_dict['score'] = submission.score
                    sub_dict['subreddit'] = sr
                    coms=submission.comments.list()
                    comments = [comment.body for comment in coms]
                    # print("printing comments\n")
                    # print(comments)
                    sub_dict['comments'] = comments
                    list_of_items.append(sub_dict)
            json.dump(list_of_items, f)
f.close()
