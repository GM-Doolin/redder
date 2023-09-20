# Redder App
Redder is a simple python application which allows users to easily scrape and save data from reddit to their local system.

> ## User Guide
> Redder currently has 2 modes of operation for the user to choose from depending on their situation.
>> ### Mode 1 - Scrape Subreddit
>> The first and more general use case for Redder is to scrape data from a specific subreddit.
>>
>> Redder uses the **subreddit** argument formated '-s' or '--subreddit' for this operation.
>>
>> This argument takes in a url of the desired subreddit.
>>
>> Example of this arguments use:
>>> **python rdr.py -s https://www.reddit.com/r/desired_subreddit/**
>>
>> The data scraped using this method will contain information regarding the subreddit, 10 of the most recent posts from the subreddit, and the comments associated with them.
>
>> ### Mode 2 - Scrape Post
>> The second use case for Redder is when you would like to scrape data from a post from reddit.
>>
>> Redder uses the **post** argument formated '-p' or '--post' for this operation.
>>
>> This argument takes in a url of the desired reddit post.
>>
>> Example of this arguments use:
>>> **python rdr.py -p https://www.reddit.com/r/desired_subreddit/comments/post_id#/post_title/**
>>
>> The data scraped using this method will contain information regarding the post and the comments associated with.
>
> Both of these methods will produce a json file to the local relative application path "redder\output\".
>
>* Method 1 will produce a file titled "subreddit-id#.json" where id# is the internal unique ID of the subreddit.
>
>* Method 2 will produce a file titled "post-id#.json" where id# is the internal unique ID of the post.