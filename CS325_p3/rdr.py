# rdr_main: Main Redder Application

    # Input: Takes in Various User Command Line Agruments of type string (URL/Name of Subreddit, URL of reddit Post, Name of File in raw 'Data\raw\post-id.json')

    # Output: '.json' and '.txt' files in 'Data/'

    # Usage: Redder Application Entry Point, Where The User-Side of the Redder Application Begins and Ends

# Dependencies
    # Standard Module(s)
import argparse
    # Installed Module(s)
    # Local Module(s)
from module_1 import redder, fio
from module_2 import clrx
from module_3 import mrkr

###### ###### ###### ###### ###### ######
###### Main Redder App. Entry Pt.  ######
###### ###### ###### ###### ###### ######

try:
    parser = argparse.ArgumentParser(
        prog = 'Redder',
        description = 'Collect Subreddit Data Into Local Files',
        epilog = 'Positional Arg. Types: string'
    )
    p = parser.add_mutually_exclusive_group()
    p.add_argument(
        '-s',
        '--subreddit',
        help = 'Name and/or URL of Desired Subreddit to Scrape',
        type = str
    )
    p.add_argument(
        '-p',
        '--post',
        help = 'URL of Desired Reddit Post to Scrape',
        type = str
    )
    p.add_argument(
        '-c',
        '--comments',
        help = 'File Name of Previously Ouput Scrapped Post File in the Local App. Path, For Example: \'\\Data\\raw\\post-id.json\'',
        type = str
    )
    args = parser.parse_args()

    if args.subreddit:
        mySub = redder.QuerySubredder(clrx.GetURLPage(args.subreddit))
        mrkr.Cyan("Redder is retrieving data from the \"" + mySub.name + "\" subreddit!")
        fio.WriteDataFile("subreddit-" + mySub.id, clrx.ToJSON(mySub), "raw")
        mrkr.Green("Redder has successfully finished collecting data from the \"" + mySub.name + "\" subreddit into the file : subreddit-" + mySub.id + ".json")
    elif args.post:
        myPost = redder.QueryPost(args.post)
        mrkr.Cyan("Redder is retrieving data from the \"" + myPost.title + "\" post!")
        fio.WriteDataFile("post-" + myPost.id, clrx.ToJSON(myPost), "raw")
        mrkr.Green("Redder has successfully finished collecting data from the \"" + myPost.title + "\" reddit post into the file : post-" + myPost.id + ".json")
    elif args.comments:
        myFile = clrx.RemoveFileExt(args.comments)
        mrkr.Cyan("Redder is retrieving comments from file: " + args.comments)
        fio.WriteDataFile(myFile + "-comments", redder.post.JSONToPost(fio.ReadDataFile(myFile, "raw")).ListComments(), "processed", fileExt = "txt")
        mrkr.Green("Redder has successfully finished retrieving the comments into the file: " + myFile + "-comments.json")
except Exception as e:
    mrkr.Red("Exception: " + str(e))
mrkr.Cyan("Redder Exiting Safely...")
exit()