# redder_module: Redder Module

    # Input: Takes in Various Reddit related String Data (Name of Subreddit, URL of Reddit Post, Read/Write .py/.json objects)

    # Output: Subreddit/Post python objects with scrapped data, and/or '.json'/'.txt' files of their associated data

    # Usage: Main Module of Redder App To Scrape Subreddit Data and Create python subreddit objects, which can be serialized to JSON and written out to files and/or read-back/parsed

# Dependencies
    # Standard Module(s)
import re
    # Installed Module(s)
import jsonpickle
import praw
    # Local Module(s)

###### ###### ###### ###### ######
###### Interface For Redder ######
###### ###### ###### ###### ######

# Create class object from given reddit url
def QueryPost(URL: str) -> 'post':
    try:
        ri = praw.Reddit(
            client_id     = PRAWCreds.client_id,
            client_secret = PRAWCreds.client_secret,
            user_agent    = PRAWCreds.user_agent
        )
        return post(ri.submission(url=URL))
    except Exception as e: 
        print("Redder ran into unexpected issues when retrieving data from the URL provided!")
        raise e

# Container For Redder Credentials for PRAW API
class PRAWCreds:

    client_id     = "2ywZ-_sgiTazjJo-ue2hfQ"
    client_secret = "LMxkB2T9P9klCYG-NHGLGX-7cWHwtA"
    user_agent    = "redder:v1.0.0"

    # Check if ID is parent ID (PRAW ID)
    @staticmethod
    def IsParentID(id: str) -> bool:
        if parentMatch := re.match(r"t1_", id):
            return True
        else:
            return False

###### ###### ###### ###### ###### ###### ###### ######
###### Containers For Retrieved Sub-Reddit Data  ######
###### ###### ###### ###### ###### ###### ###### ######

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
            self.comments.append(comment(cmt))
    
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
        if PRAWCreds.IsParentID(comment.parent_id):
            self.parent_id = str(comment.parent_id)
        self.author = str(comment.author)
        self.score = int(comment.score)
        self.body = self.FormatComment(str(comment.body))

    # Format comment for proper entry use for analyzing
    @staticmethod
    def FormatComment(cmt: str) -> str:
        try:
            # remove unecessary whitespace above 1 space
            newCmt = re.sub(r"[\s]{2,}", " ", cmt).strip()
            # remove unecessary escape sequences for different lines
            newCmt = re.sub(r"[\t|\r|\n]", "", newCmt)
            return newCmt
        except Exception as e:
            raise e