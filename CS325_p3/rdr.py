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
from module_2 import clrx, saai
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
        '-p',
        '--post',
        help = 'URL of Desired Reddit Post to Scrape',
        type = str
    )
    p.add_argument(
        '-c',
        '--comments',
        help = 'File Name of Previously Scraped and Ouput Post JSON File in the Local App. Path, For Example: redder\\CS325_p3\\Data\\raw\\post-id.json',
        type = str
    )
    p.add_argument(
        '-s',
        '--sentiments',
        help = 'File Name of Previously processed and Ouput Post comments Text File in the Local App. Path, For Example: redder\\CS325_p3\\Data\\processed\\post-id-comments.txt',
        type = str
    )
    args = parser.parse_args()

    if args.post:
        myPost = redder.QueryPost(args.post)
        mrkr.Cyan("Redder is retrieving data from the \"" + myPost.title + "\" post!")
        fio.WriteDataFile("post-" + myPost.id, clrx.ToJSON(myPost), "raw")
        mrkr.Green("Redder has successfully finished collecting data from the \"" + myPost.title + "\" reddit post into the file : post-" + myPost.id + ".json")
    elif args.comments:
        myFile = clrx.RemoveFileExt(args.comments)
        mrkr.Cyan("Redder is retrieving comments from file: " + args.comments)
        fio.WriteDataFile(myFile + "-comments", redder.post.JSONToPost(fio.ReadDataFile(myFile, "raw")).ListComments(), "processed", fileExt = "txt")
        mrkr.Green("Redder has successfully finished retrieving the comments into the file: " + myFile + "-comments.txt")
    elif args.sentiments:
        myFile = clrx.RemoveFileExt(args.sentiments)
        mrkr.Cyan("Redder is Analyzing the Sentiments of the comments from file: " + args.sentiments)
        fio.WriteCSVFile(myFile + "-sentiments", saai.CreateSentimentTextList(fio.ReadDataFile(myFile, "processed", fileExt = "txt").split("\n\n")), "Sentiments", fileExt = "txt")
        mrkr.Green("Redder has successfully finished analyzing the sentiments of the comments into the file: " + myFile + "-sentiments.txt")
except Exception as e:
    mrkr.Red("Exception: " + str(e))
mrkr.Cyan("Redder Exiting Safely...")
exit()