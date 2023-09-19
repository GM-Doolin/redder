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
    args= parser.parse_args()

    if args.subreddit:
        mySub = redder.GetSubreddit(redder.clrx.GetURLPage(args.subreddit))
        redder.mrkr.printCyan("Redder is retrieving data from the \"" + mySub.name + "\" subreddit!")
        redder.WriteJSONFile("subreddit-" + mySub.id, mySub.ToJSON())
        redder.mrkr.printGreen("Redder has successfully finished collecting data from the \"" + mySub.name + "\" subreddit!")
    elif args.post:
        myPost = redder.GetPost(args.post)
        redder.mrkr.printCyan("Redder is retrieving data from the \"" + myPost.title + "\" post!")
        redder.WriteJSONFile("post-" + myPost.id, myPost.ToJSON())
        redder.mrkr.printGreen("Redder has successfully finished collecting data from the \"" + myPost.title + "\" post!")
except Exception as e:
    redder.mrkr.printRed("Exception: " + str(e))

redder.mrkr.printCyan("Redder Exiting Safely...")
exit()