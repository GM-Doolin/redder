# Dependencies
    # Standard Lib(s)
import time
    # Installed Lib(s)
import jsonpickle
import praw
    # Local Module(s)
from .util.util import *

###### ###### ###### ###### ######
###### Interface For Redder ######
###### ###### ###### ###### ######

# Create subredder class object from given subreddit name and post count
def GetSubreddit(subName: str, postCount: int = 10) -> 'subredder':
    try:
        ri = praw.Reddit(
            client_id     = Creds.client_id,
            client_secret = Creds.client_secret,
            user_agent    = Creds.user_agent
        )
        sr = subredder(ri.subreddit(subName), postCount)
        return sr
    except Exception as e: 
        mrkr.Yellow("Redder ran into unexpected issues when retrieving data from the URL the subreddit data!")
        raise e

# Create class object from given reddit url
def GetPost(URL: str) -> 'post':
    try:
        ri = praw.Reddit(
            client_id     = Creds.client_id,
            client_secret = Creds.client_secret,
            user_agent    = Creds.user_agent
        )
        sr = post(ri.submission(url=URL))
        return sr
    except Exception as e: 
        mrkr.Yellow("Redder ran into unexpected issues when retrieving data from the URL provided!")
        raise e

# Convert class object to JSON str
def ToJSON(obj, isIndented: bool = True) -> str:
    try:
        jsonpickle.set_encoder_options('json')
        if isIndented:
            return jsonpickle.encode(obj, keys = True, indent=4, separators=(',', ': '))
        else:
            return jsonpickle.encode(obj, keys = True)
    except Exception as e:
        mrkr.Yellow("Redder ran into unexpected issues encoding python object to JSON!")
        raise e
    
# Convert subredder JSON str to subredder class object
def JSONToSubredder(json: str) -> 'subredder':
    try:
        jsonpickle.set_decoder_options('json')
        return jsonpickle.decode(json, keys = True)
    except Exception as e:
        mrkr.Yellow("Redder ran into unexpected issues decoding JSON to subredder!")
        raise e

# Convert post JSON str to post class object
def JSONToPost(json: str) -> 'post':
    try:
        jsonpickle.set_decoder_options('json')
        return jsonpickle.decode(json, keys = True)
    except Exception as e:
        mrkr.Yellow("Redder ran into unexpected issues decoding JSON to post!")
        raise e

# Write file "output\filename.fileExt"
def WriteFile(fileName: str, json: str, fileExt: str = "json") -> None:
    try:
        file = open("output\\" + fileName + "." + fileExt, "w", encoding = "utf-8")
        file.write(json)
        file.close()
    except Exception as e:
        mrkr.printYellow("Redder ran into unexpected issues writing file!")
        raise e
    
# Read file "output\fileName.fileExt", return str
def ReadFile(fileName: str, fileExt: str = "json") -> str:
    try:
        file = open("output\\" + fileName + "." + fileExt, "r", encoding = "utf-8")
        json = file.read()
        file.close()
        return json
    except Exception as e:
        mrkr.Yellow("Redder ran into unexpected issues reading file!")
        raise e

# Container For Redder Credentials for PRAW API
class Creds:
    client_id     = "2ywZ-_sgiTazjJo-ue2hfQ"
    client_secret = "LMxkB2T9P9klCYG-NHGLGX-7cWHwtA"
    user_agent    = "redder:v0.8.0"

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

    # Update subredder class object data, optional
    def Update(self) -> None:
        newSubRedderInst = GetSubreddit(self.name, len(self.posts))
        self.snapshotTime = int(time.time())
        self.posts = newSubRedderInst.posts

    # Get JSON str of the subredder class object
    def ToJSON(self, isIndented: bool = True) -> str:
        return ToJSON(self, isIndented)

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

    # Get JSON str of the post class object
    def ToJSON(self, isIndented: bool = True) -> str:
        return ToJSON(self, isIndented)
    
    # Return comments of post
    def ListComments(self) -> str:
        try:
            comments = ""
            for cmt in self.comments:
                comments += cmt.body + "\n\n"
            return comments
        except Exception as e:
            mrkr.Yellow("Redder ran into unexpected issues listing comments from the post!")
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
        if clrx.IsParentId(comment.parent_id):
            self.parent_id = str(comment.parent_id)
        self.author = str(comment.author)
        self.score = int(comment.score)
        self.body = str(comment.body)