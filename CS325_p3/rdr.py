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
    argparser = argparse.ArgumentParser(
        prog = 'Redder',
        description = 'Collect Subreddit Data Into Local Files',
        epilog = 'Positional Arg. Types: string'
    )
    o = argparser.add_mutually_exclusive_group()
    o.add_argument(
        '-p',
        '--post',
        help = 'URL of Desired Reddit Post to Scrape',
        type = str
    )
    o.add_argument(
        '-f',
        '--file',
        help = 'File Name of local user input file that contains Reddit Post URLs to be Scraped, For Example: C:\\Users\\User\\FolderWithFile\\URLfile.txt',
        type = str
    )
    o.add_argument(
        '-c',
        '--comments',
        help = 'File Name of Previously Scraped and Ouput Post JSON File in the Local App. Path, For Example: redder\\CS325_p3\\Data\\raw\\post-id#.json',
        type = str
    )
    o.add_argument(
        '-s',
        '--sentiments',
        help = 'File Name of Previously Processed and Ouput Post comments Text File in the Local App. Path, For Example: redder\\CS325_p3\\Data\\processed\\post-id#-comments.txt',
        type = str
    )
    o.add_argument(
        '-g',
        '--graph',
        help = 'Takes no value, Flag to process each sentiment CSV file in the Local App. Path redder\\CS325_p3\\Data\\Sentiments\\ and output a bar graph for each.',
        action = 'store_true'
    )
    args = argparser.parse_args()

    if args.post:
        myPost = redder.QueryPost(args.post)
        mrkr.Cyan("Redder is Retrieving Data from the \"" + myPost.title + "\" post!\n")
        fio.WriteDataFile("post-" + myPost.id, clrx.ToJSON(myPost), "raw")
        mrkr.Green("Redder has Successfully Finished Collecting Data from the \"" + myPost.title + "\" Reddit Post into File: post-" + myPost.id + ".json\n")
    elif args.file:
        URLS = list(filter(None, fio.ReadFile(args.file).split("\n")))
        mrkr.Cyan("Redder is Retrieving the Reddit URL's from File: " + args.file + "\n")
        for url in URLS:
            thisPost = redder.QueryPost(url)
            thisPostFileName = "post-" + thisPost.id
            fio.WriteDataFile(thisPostFileName, clrx.ToJSON(thisPost), "raw")
            mrkr.Green("\tRedder has Scraped the URL's Data into File: " + thisPostFileName + ".json")
            thisCommentFileName = thisPostFileName + "-comments"
            fio.WriteDataFile(thisCommentFileName, redder.post.JSONToPost(fio.ReadDataFile(thisPostFileName, "raw")).ListComments(), "processed", fileExt = "txt")
            mrkr.Green("\tRedder has Parsed the Comments into File: " + thisCommentFileName + ".txt")
            thisSentimentsFileName = thisCommentFileName + "-sentiments"
            mrkr.Yellow("\tRedder is now Analyzing the Sentiments, it may take Awhile to Query all API Sentiment Requests, Please be Patient and Standby!")
            fio.WriteCSVFile(thisSentimentsFileName, saai.CreateSentimentList(fio.ReadDataFile(thisCommentFileName, "processed", fileExt = "txt").split("\n\n")), "Sentiments", fileExt = "txt")
            mrkr.Green("\tRedder has Analyzed the Comment Sentiments into File: " + thisSentimentsFileName + "\n")
        mrkr.Green("Redder has Successfully Finished Processing All Data Associated with the Reddit URL's from File: " + args.file + "\n")
    elif args.comments:
        myFileName = clrx.RemoveFileExt(args.comments)
        mrkr.Cyan("Redder is Retrieving Comments from File: " + args.comments + "\n")
        fio.WriteDataFile(myFileName + "-comments", redder.post.JSONToPost(fio.ReadDataFile(myFileName, "raw")).ListComments(), "processed", fileExt = "txt")
        mrkr.Green("Redder has Successfully Finished Retrieving the Comments into File: " + myFileName + "-comments.txt\n")
    elif args.sentiments:
        myFileName = clrx.RemoveFileExt(args.sentiments)
        mrkr.Cyan("Redder is Analyzing the Sentiments of the Comments from File: " + args.sentiments + "\n")
        mrkr.Yellow("\tIt may take Awhile to Query all API Sentiment Requests, please be Ppatient and Standby!")
        fio.WriteCSVFile(myFileName + "-sentiments", saai.CreateSentimentList(fio.ReadDataFile(myFileName, "processed", fileExt = "txt").split("\n\n")), "Sentiments", fileExt = "txt")
        mrkr.Green("Redder has Successfully Finished Analyzing the Sentiments of the Comments into File: " + myFileName + "-sentiments.txt\n")
    elif args.graph:
        mrkr.Cyan("Redder is Looking for Comment Sentiment Files to Plot!\n")
        if sentimentFiles := [f for f in fio.GetDataFiles("Sentiments") if saai.IsValidSentimentFile(f)]:
            for file in sentimentFiles:
                saai.PlotSentimentBarGraph(file, redder.QueryPostTitleFromID(clrx.GetFileID(file)), clrx.GetFileID(file))
                mrkr.Green("\tRedder Plot the Comment Sentiments of " + file + " into File: " + clrx.RemoveFileExt(file) + "-plot.png\n")
            mrkr.Green("Redder has Finished Plotting the Comment Sentiment Bar Graph(s)!\n")
        else:
            mrkr.Yellow("Redder did not Find Any Appropriate Comment Sentiment Files in 'redder\\CS325_p3\\Data\\Sentiments\\'to Plot!" + "\n")
except Exception as e:
    mrkr.Red("Exception: " + str(e) + "\n")
mrkr.Cyan("Redder Exiting Safely...")
exit()