# Dependencies
    # Standard Lib(s)
import argparse
    # Installed Lib(s)
    # Local Module(s)
import src.redder as redder

###### ###### ###### ###### ######
###### Redder App Entry Pt. ######
###### ###### ###### ###### ######

try:
    parser = argparse.ArgumentParser(
        prog='Redder',
        description='Collect Subreddit Data into Local JSON File',
        epilog='Positional Arg. Types: string'
    )
    p = parser.add_mutually_exclusive_group()
    p.add_argument(
        '-s',
        '--subreddit',
        help='Name of desired Subreddit',
        type=str
    )
    p.add_argument(
        '-p',
        '--post',
        help='URL of desired reddit post',
        type=str
    )
    p.add_argument(
        '-c',
        '--comments',
        help='File name',
        type=str
    )
    args= parser.parse_args()

    if args.subreddit:
        mySub = redder.GetSubreddit(redder.clrx.GetURLPage(args.subreddit))
        redder.mrkr.Cyan("Redder is retrieving data from the \"" + mySub.name + "\" subreddit!")
        redder.WriteFile("subreddit-" + mySub.id, mySub.ToJSON())
        redder.mrkr.Green("Redder has successfully finished collecting data from the \"" + mySub.name + "\" subreddit into the file : subreddit-" + mySub.id + ".json")
    elif args.post:
        myPost = redder.GetPost(args.post)
        redder.mrkr.Cyan("Redder is retrieving data from the \"" + myPost.title + "\" post!")
        redder.WriteFile("post-" + myPost.id, myPost.ToJSON())
        redder.mrkr.Green("Redder has successfully finished collecting data from the \"" + myPost.title + "\" reddit post into the file : post-" + myPost.id + ".json")
    elif args.comments:
        myFile = redder.clrx.RemoveFileExt(args.comments)
        redder.mrkr.Cyan("Redder is retrieving comments from file: " + args.comments)
        redder.WriteFile(myFile + "-comments", redder.JSONToPost(redder.ReadFile(myFile)).ListComments(), fileExt = "txt")
        redder.mrkr.Green("Redder has successfully finished retrieving the comments into the file: " + myFile + "-comments.json")
except Exception as e:
    redder.mrkr.Red("Exception: " + str(e))
redder.mrkr.Cyan("Redder Exiting Safely...")
exit()