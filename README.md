> # `Redder User Guide`
>
> Redder is a simple python application which allows users to easily scrape and save data from reddit to their local system.
>
> Redder currently has 3 modes of operation for the user to choose from depending on their situation.
>
> Read through the user guide and find what works best for you.
>
> ## `Project 1`
>
>> ### `Operation 1 - Scrape Post`
>>
>> **The first use case for Redder is when you would like to scrape data from a specific reddit post.**
>>
>> Redder uses the `post` argument of the format `-p` or `--post` for this operation.
>>
>> This `post` argument takes in a url of the desired reddit post.
>>
>> Example of this arguments use:
>>
>> ```
>> python rdr.py -p https://www.reddit.com/r/desired_subreddit/comments/post_id#/post_title/
>> ```
>>
>> The data scraped using this operation will contain information regarding the post and the comments associated with.
>>
>> This operation will produce a file in the local application path subfolder in `redder\CS325_p3\Data\raw\`
>>
>> This new file will be titled `post-id#.json` in the local path `redder\CS325_p3\Data\raw\`, where id# is the internal unique ID of the post.
>>
>
> ## `Project 2`
>
>> ### `Operation 2 - Retrieve Post Comments`
>>
>> **The second use case for Redder is when you would like to get comments from a previously scraped reddit post using Operation 1.**
>>
>> Redder uses the `comments` argument of the format `-c` or `--comments` for this operation.
>>
>> This `comments` argument takes in a filename of the desired file located in the local app directory `redder\CS325_p3\Data\raw\`
>> 
>> The filename should be of the format `post-id#.json`, a file which is has been output using operation 1 in Project 1.
>>
>> Example of this arguments use:
>>
>> ```
>> python rdr.py -c post-id#.json
>> ```
>>
>> This operation method will retrieve the post data from the file and save the associated comments into a new .txt file.
>>
>> This operation will produce a file in the local application path subfolder in `redder\CS325_p3\Data\processed\`
>>
>> This new file will be titled `post-id#-comments.txt`, where id# is the internal unique ID of the post.
>>
>
> ## `Project 3`
>
>> The main functional component of Redder, `rdr.py` has been moved inside the `redder\CS325_p3\` folder located inside the main repository directory
>>
>> The Output Location(s) have been Moved To Their Respective Folder inside the `redder\CS325_p3\Data\` Subfolder of `redder\CS325_p3\`
>
> ## `Project 4 - Grant Doolin & Gautam Aneja`
>
>> ### `Operation 3 - Analyze Sentiments of Comments`
>>
>> **The third use case of Redder is the ability to analyze the sentiments of the comments previously extracted using Operation 2.**
>> 
>> To do this, Redder utilizes `OpenAI's API` to leverage the `GPT-3.5-turbo` model to analyze the comments and return their sentiments.
>>
>>> *Before using this method, be sure you have a valid and active OpenAI account, and have properly set up your account's API key for redder. If not, follow the OpenAI setup guide further down.*
>>
>> Redder uses the `sentiments` argument of the format `-s` or `--sentiments` for this operation.
>>
>> The `sentiments` argument takes in the filename of the desired file located in the local app directory `redder\CS325_p3\Data\processed\`
>>
>> This filename should be of the format `post-id#-comments.txt`, a file which has been output using Operation 2 in Project 2.
>>
>> Example of this arguments use:
>>
>> ```
>> python rdr.py -s post-id#-comments.txt
>> ```
>>
>> This argument will produce a CSV file titled `post-id#-comments-sentiments.txt` in the local app path `redder\CS325_p3\Data\Sentiments\`
>>
>> The CSV format inside of this new file will be like so: "sentiment","Text Analyzed"
>> 
>> The file will contain only 50 comments (**As noted in the project 4 outline**) that have been analyzed as to avoid wasting API tokens.
>>
>> ***`You may experience wait times of several minutes`***, this is expected as there are by default a max of 50 queries that need to be made for possible 50 comments and each query relies on a 3rd party API that has request latency, connectivity dependencies, processing time, and then transfer times.
>>
>> Progress updates will be given in the form of a percentage during during sentiment analysis to keep you informed on the operations progress and state.
>>
>> The application may get hung up and timeout while waiting for OpenAI's API to properly query a request. If this happens, Redder will notify you of the situation and automatically re-query the request a number of times if needed.
>>
>> ***`If you notice the sentiment query progress has been stuck on the same percentage for an unusually long amount of time AND you have not gotten any new messages displayed back to you from Redder updating you on the sentiment analysis progress state, try killing the process and running the command again as there is a high likelyhood that OpenAI API is having issues and currently has trouble serving requests.`***
>
> ## `Project 5 - Grant Doolin & Gautam Aneja`
>
>> ### `Operation 4 - Fully Process Multiple Reddit Post URL's from File` 
>>
>> **The Fourth use case of Redder is the ability to get the sentiments of the comments from multiple Reddit Post URL's at once using a file.**
>>
>> To do this, Redder just needs a single user input text file, that for each line used, contains a single reddit post URL.  (a .txt file is preferred for simplicity sake)
>>
>> For Example, for 5 different Reddit Post URL's the user input text file would contain nothing else but the URL's in this format:
>>
>> ```
>> https://www.reddit.com/r/desired_subreddit1/comments/post_id#1/post_title1/
>> https://www.reddit.com/r/desired_subreddit2/comments/post_id#2/post_title2/
>> https://www.reddit.com/r/desired_subreddit3/comments/post_id#3/post_title3/
>> https://www.reddit.com/r/desired_subreddit4/comments/post_id#4/post_title4/
>> https://www.reddit.com/r/desired_subreddit5/comments/post_id#5/post_title5/
>> ```
>>
>>> *Before using this method, be sure you have a valid and active OpenAI account, and have properly set up your account's API key for redder. If not, follow the OpenAI setup guide further down.*
>>
>> To process these URL's, Redder uses the `file` argument of the format `-f` or `--file` for this operation.
>>
>> The `file` argument takes in the filename (and the files path, if necessary) of the desired file located in the user's local machine.
>>
>> Example of this arguments use:
>>
>> ```
>> python rdr.py -f C:\Users\User\FolderWithFile\URLfile.txt
>> ```
>>
>> This argument operation consists of running operations 1 through 3 back to back for each URL in the input file.
>>
>> As such, `this operation will produce 3 files for each URL corresponding to operations 1 through 3`. (Visit those operation sections in the README to see more about each operation and their output)
>>
>> The 3 files output for each URL are as follows:
>>
>> - File 1: `post-id#.json` - This file contains the raw data scraped from Reddit Post URL. See Redder Operation 1 for more information.
>>
>> - File 2: `post-id#-comments.txt` - This file contains parsed comments from File 1. See Redder Operation 2 for more information.
>>
>> - File 3: `post-id#-comments-sentiments.txt` - This file contains the sentiment's of each comment from File 2. See Redder Operation 3 for more information.
>>
>> Note that the `id#` in the file names will be consistent to each URL, meaning each URL will ouput 3 files that contain the same `id#` in their file names.
>> 
>> Different URL's will output files with different `id#`s in the file name.
>>
>> ***`You may experience wait times of several minutes per URL`***, this is expected as there are by default 50 queries that need to be made per URL and each query relies on a 3rd party API that has request latency, connectivity dependencies, and transfer times.
>>
>> Progress updates will be given in the form of a percentage during during sentiment analysis stage for each URL to keep you informed on the operations progress and state.
>>
>> The application may get hung up and timeout while waiting for OpenAI's API to properly query a request. If this happens, Redder will notify you of the situation and automatically re-query the request a number of times if needed.
>>
>> ***`If you notice the sentiment query progress has been stuck on the same percentage for an unusually long amount of time AND you have not gotten any new messages displayed back to you from Redder updating you on the sentiment analysis progress state, try killing the process and running the command again as there is a high likelyhood that OpenAI API is having issues and currently has trouble serving requests.`***
>
> ## `Redder OpenAI API Setup Guide`
>
>> In order to use the features of Redder which are enabled by OpenAI's API, please follow these steps to ensure correct app execution.
>>
>> 1. First create an OpenAI account at: https://platform.openai.com/ and log in. (If this is your first account you should be given $5.00 in free credit to use the API, If not see OpenAI's fees for more information)
>>
>> 2. Once logged in, navigate to the left side of the page in the nav bar and select the 'API Keys' tab:
>>
>> ![Logged In](rsc/P4_LoggedIn.jpg)
>> 
>> 3. On the API Keys page, select the Button 'Create new secret key' and give the key a name, then click the 'Create secret key' to confirm.
>>
>> ![Create Key](rsc/P4_CreateKey.jpg)
>>
>> 4. After clicking 'Create secret key', the website will return your new secret key. Copy this key now and save it somewhere safe, you will not be able to recover it once you move forward.
>>
>> ![Created Key](rsc/P4_CreatedKey.jpg) 
>>
>> 5. The last step is to actually use the key to call the API and I will show how below.
>>
>> ## `Using OpenAI API Key`
>>
>> Before proceding with writing python code, make sure you have installed the necessary `openai` python package:
>>
>> ```
>> pip install openai
>> ```
>>
>> Now that we are ready, we can setup and use our key.
>>
>> To safely use your new key you should add the key to your systems environment variables.
>>
>> To do this, navigate to your operating systems environment variables (this will depend on your Operating System, look it up if necessary).
>>
>> Once there, Add the new Environment User Variable like so:
>>
>> ```
>> Variable name: OPENAI_API_KEY
>>
>> Variable value: YourOpenAIAPIKeyGoesHere
>> ```
>>
>> ![Environment Variable](rsc/P4_EnvVar.jpg)
>>
>> Once the variable has been added successfully, you can now use the key in python directly (Proceed to the end of this section to see how) however the next step is recommended.
>>
>> Next, create a new file in the local directory of the target python application called `.env`
>>
>> Redder has this file natively so the `.env` file already exists and is waiting for you at the local app path `redder\CS325_p3\`
>>
>> Inside of this file named `.env`, simply use the following line at the top of the file and replace it with your key, save, and close it:
>>
>> ```
>> OPENAI_API_KEY=YourOpenAIAPIKeyGoesHere
>> ```
>>
>> Once your key has been added to the file, save and exit the file. The key is now ready to be used.
>>
>> To use our key in python, we first need to import `openai` package.
>>
>> Now we can call the function `OpenAI()` and assign it to a variable instance called `clientAI` that we can use to make requests from:
>>
>> ```
>> import openai
>>
>> clientAI = openai.OpenAI()
>> 
>> response = clientAI.chat.completions.create(
>>     model="gpt-3.5-turbo",
>>     messages=[
>>         {"role": "system", "content": "You will be provided with a comment, and your task is to classify its sentiment, your response must be: 'positive', 'neutral', or 'negative'"},
>>         {"role": "user", "content": "This is so cool, I love it!"}
>>     ]
>> )
>> ```
>>
>> If the environment variable and `.env` file key were added properly, the function will return an openai instance which can be used to make a number of different requests now.
>>
>> Calling `OpenAI()` will look in the local directory for the `.env` file we made earlier and use the `OPENAI_API_KEY` value found in it for the Environment Variable value.
>> 
>>> *If you chose to not use a .env file to avoid clutter, below will show you how to use your key directly from your system environment variable.*
>>>
>>> This is almost identical to the process before, just a bit less pleasing to the eyes.
>>>
>>> To assign your key in python for the API, import the `openai` and `os` packages, then just get the OS environment variable and assign it to the API's `api_key` instance. You can then make requests with the API like so:
>>>
>>> ```
>>> import openai
>>> import os
>>>
>>> openai.api_key = os.environ["OPENAI_API_KEY"]
>>>
>>> response = openai.chat.completions.create(
>>>     model="gpt-3.5-turbo",
>>>     messages=[
>>>         {"role": "system", "content": "You will be provided with a comment, and your task is to classify its sentiment, your response must be: 'positive', 'neutral', or 'negative'"},
>>>         {"role": "user", "content": "This is so cool, I love it!"}
>>>     ]
>>> )
>>> ```
>>
>