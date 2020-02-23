import praw
import json

#mental health dictionary for scraping different subreddits
mh_dict = {
    'hard':['depression','Anxiety','autism','ptsd','ADHD'],
    'soft':['Stress','ImposterSyndrome','FamilyIssues','friendship','relationship_advice']
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
num = 0
# types = string, string, int, string, [string]
#fields = ('title','id','score','subreddit','comments')
#go through subreddits in above dict
with open('training_data.json', 'w') as f:
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
            #limit submissions to maximum 400 per subreddit
            submissions = subred.hot(limit=400)
            for submission in submissions:
                #get the non sticky ones
                if not submission.stickied:
                    num+=1
                    #print('submissions gathered: {}'.format(num))
                    sub_dict = {}
                    sub_dict['title'] = submission.title
                    sub_dict['id'] = submission.id
                    sub_dict['body'] = submission.selftext
                    sub_dict['score'] = submission.score
                    sub_dict['subreddit'] = sr
                    #print(coms)
                    submission.comments.replace_more(limit=0)
                    if len(submission.comments.list()) > 0:
                        #new for testing, best for training
                        submission.comment_sort = 'best'
                        comments = submission.comments.list()
                        if len(comments) >=2:
                            best_str = comments[0].body
                            second = comments[1].body
                        else:
                            best_str = comments[0].body
                            second = ''
                    else:
                        best_str = ''
                        second = ''
                    sub_dict['best_comment'] = best_str
                    sub_dict['second_best_comment'] = second

                    list_of_items.append(sub_dict)
    print("There were {} submissions".format(num))
    json.dump(list_of_items, f)
f.close()
