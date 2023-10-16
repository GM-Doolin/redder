# redder_module: Redder Module

    # Input: Takes in Various Reddit related String Data (Name of Subreddit, URL of Reddit Post, Read/Write .py/.json objects)

    # Output: Subreddit/Post python objects with scrapped data, and/or '.json'/'.txt' files of their associated data

    # Usage: Main Module of Redder App To Scrape Subreddit Data and Create python subreddit objects, which can be serialized to JSON and written out to files and/or read-back/parsed

# Dependencies
    # Standard Module(s)
import re
import time
    # Installed Module(s)
import jsonpickle
import praw
    # Local Module(s)

###### ###### ###### ###### ######
###### Interface For Redder ######
###### ###### ###### ###### ######

# Create subredder class object from given subreddit name and post count
def QuerySubredder(subName: str, postCount: int = 10) -> 'subredder':
    try:
        ri = praw.Reddit(
            client_id     = Creds.client_id,
            client_secret = Creds.client_secret,
            user_agent    = Creds.user_agent
        )
        return subredder(ri.subreddit(subName), postCount)
    except Exception as e: 
        print("Redder ran into unexpected issues when retrieving data from the URL the subreddit data!")
        raise e

# Create class object from given reddit url
def QueryPost(URL: str) -> 'post':
    try:
        ri = praw.Reddit(
            client_id     = Creds.client_id,
            client_secret = Creds.client_secret,
            user_agent    = Creds.user_agent
        )
        return post(ri.submission(url=URL))
    except Exception as e: 
        print("Redder ran into unexpected issues when retrieving data from the URL provided!")
        raise e

# Container For Redder Credentials for PRAW API
class Creds:

    client_id     = "2ywZ-_sgiTazjJo-ue2hfQ"
    client_secret = "LMxkB2T9P9klCYG-NHGLGX-7cWHwtA"
    user_agent    = "redder:v1.0.0"

    # Check if ID is parent ID (PRAW ID)
    @staticmethod
    def IsParentId(id: str) -> bool:
        if parentMatch := re.match(r"t1_", id):
            return True
        else:
            return False

###### ###### ###### ###### ###### ###### ###### ######
###### Containers For Retrieved Sub-Reddit Data  ######
###### ###### ###### ###### ###### ###### ###### ######

# data container for retrieved reddit subreddit data
class subredder:

    # subredder class object constructor
    def __init__(self, subreddit: 'praw.Reddit.subreddit', postCount: int) -> 'subredder':
        self.snapshotTime = int(time.time())
        self.id = str(subreddit.id)
        self.name = str(subreddit.display_name)
        self.description = str(subreddit.public_description)
        self.posts =  []
        for pst in subreddit.new(limit=postCount):
            newPst = post(pst)
            self.posts.append(newPst)
    
    # Convert formated subredder JSON string to subredder class object
    @staticmethod
    def JSONToSubredder(cls, json: str) -> 'subredder':
        try:
            jsonpickle.set_decoder_options('json')
            return jsonpickle.decode(json, keys = True)
        except Exception as e:
            print("Redder ran into unexpected issues decoding JSON to subredder!")
            raise e

    # Update subredder class object data, optional
    def Update(self) -> None:
        newSubRedderInst = QuerySubredder(self.name, len(self.posts))
        self.snapshotTime = int(time.time())
        self.posts = newSubRedderInst.posts

    # Get the average score among the retrieved posts
    def GetAvgPostScore(self) -> float:
        scoreTotal = 0
        for pst in self.posts:
            scoreTotal += int(pst.score)
        scoreAvg = scoreTotal / len(self.posts)
        return scoreAvg

    # Get the average upvote ratio among retrieved posts
    def GetAvgPostUpvoteRatio(self) -> float:
        ratioTotal = 0
        for pst in self.posts:
            ratioTotal += int(pst.upvoteRatio)
        ratioAvg = ratioTotal / len(self.posts)
        return ratioAvg

# data container for retrieved reddit post data
class post:

    # post class object constructor
    def __init__(self, submission: 'praw.Reddit.submission') -> 'post':
        self.creationTime = int(submission.created_utc)
        self.id = str(submission.id)
        self.author = str(submission.author)
        self.title = str(submission.title)
        self.body = str(submission.selftext)
        self.score = int(submission.score)
        self.upvoteRatio = submission.upvote_ratio
        self.comments = []
        submission.comments.replace_more()
        for cmt in submission.comments.list():
            newCmt = comment(cmt)
            self.comments.append(newCmt)
    
    # Convert formated post JSON string to post class object
    @staticmethod
    def JSONToPost(json: str) -> 'post':
        try:
            jsonpickle.set_decoder_options('json')
            return jsonpickle.decode(json, keys = True)
        except Exception as e:
            print("Redder ran into unexpected issues decoding JSON to post!")
            raise e
    
    # Return comments of post
    def ListComments(self) -> str:
        try:
            comments = ""
            for cmt in self.comments:
                comments += cmt.body + "\n\n"
            return comments
        except Exception as e:
            print("Redder ran into unexpected issues listing comments from the post!")
            raise e
    
    # get the average comment score of the post
    def GetAvgCommentScore(self) -> float:
        scoreTotal = 0
        for cmt in self.comments:
            scoreTotal += int(cmt.score)
        scoreAvg = scoreTotal / len(self.comments)
        return scoreAvg
            
# data container for retrieved reddit comment data
class comment:

    # comment class object constructor
    def __init__(self, comment: 'praw.Reddit.comment') -> 'comment':
        self.creationTime = int(comment.created_utc)
        self.id = str(comment.id)
        self.parent_id = None
        if Creds.IsParentId(comment.parent_id):
            self.parent_id = str(comment.parent_id)
        self.author = str(comment.author)
        self.score = int(comment.score)
        self.body = str(comment.body)