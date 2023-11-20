# saai_module: Sentiment Analysis AI Module

    # Input: Takes in User text

    # Output: Analyzed Sentiment from OpenAI API and its input Text, returned as a Pair List: [sentiment, text]

    # Usage: Quickly retrieve sentiment of user text using OpenAI API

# Dependencies
    # Standard Module(s)
import re
import time
    # Installed Module(s)
import matplotlib.pyplot as matplot
import openai
import pandas

    # Local Module(s)
from module_3 import mrkr

clientAI = openai.OpenAI()

###### ###### ###### ###### ######
###### Interface For saai   ######
###### ###### ###### ###### ######

# Query OpenAI API (GPT-3.5-turbo) for Sentiment Analysis of Single Text, returns value pair for sentiment operation: [sentiment, text]
# Will attempt 5 total requests for the Query before throwing exception. It is assumed the API is likely very busy or down currently if this is happening.
def QueryTextSentiment(text: str) -> []:
    requests = 5    
    while requests > 0:   
        try:
            if text:
                response = clientAI.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You will be provided with a comment, and your task is to classify its sentiment, your response must be one of three options: 'positive', 'neutral', or 'negative'"},
                        {"role": "user", "content": text}
                    ],
                    timeout=15.0
                )
                sentiment = response.choices[0].message.content
                return [sentiment, text]
        except Exception as e:    
            if e:   
                mrkr.Magenta('\tOpenAI API Timeout, Retrying Query...')    
                requests -= 1
                if requests <= 0:
                    raise e
                time.sleep(1)    
            else:    
                raise e

# Create List of Sentiment Pair List's -> [[sentiment, text], [sentiment, text], [sentiment, text]]
# size by default is small (50) to avoid OpenAI API request limit breaches
def CreateSentimentList(textList: [str], size: int = 50) -> []:
    sentimentList = []
    headerRow = ["Sentiment", "Comment"]
    sentimentList.append(headerRow)
    i = 0
    for text in textList:
        if i >= size:
            break
        # Limit comment char count per comment to avoid high token usage and improve processing times for each comment
        if len(text) >= 16 and len(text) <= 512:
            sentiment = QueryTextSentiment(text)
            if not IsValidSentiment(sentiment[0]):
                continue # sentiment not valid, query again for valid response
            sentimentList.append(sentiment)
            if i % 5 == 0:
                mrkr.Cyan("\tSentiment Query Progress: " + str((i/size) * 100) + "%")
            i += 1
    return sentimentList
    
# Tally up the totals for each possible sentiment type, return list of the tallied totals
def TallySentiments(sentiments: []) -> []:
    try:
        sentimentTally = {"positive": 0, "neutral": 0, "negative": 0}
        for sentiment in sentiments:
            if sentiment == "positive":
                sentimentTally["positive"] += 1
            elif sentiment == "neutral":
                sentimentTally["neutral"] += 1
            elif sentiment == "negative":
                sentimentTally["negative"] += 1
        return [sentimentTally["positive"], sentimentTally["neutral"], sentimentTally["negative"]]
    except Exception as e:    
        raise e

# Using pandas, Read processed sentiments CSV file located in "redder\CS325_p3\Data\Sentiments\" to DataFrame, return list of sentiments
def ReadFileSentiments(fileName: str) -> []:
    try:
        sentimentData = pandas.read_csv("Data\\Sentiments\\" + fileName)
        return list(sentimentData.loc[:,"Sentiment"])
    except Exception as e:
        raise e

# Using matplotlib, Plot out bar graph file of the sentiments using matplotlib package
def PlotSentimentBarGraph(fileName: str, header: str, id: str,  xLabel: str = "Comment Sentiment", yLabel: str = "Number of Comments",) -> None:
    try:
        #saai.PlotSentimentBarGraph(saai.TallySentiments(saai.ReadFileSentiments(file)), redder.QueryPostTitleFromID(clrx.GetFileID(file)), clrx.GetFileID(file))

        sentimentTypes = ["positive", "neutral", "negative"]
        sentimentTotals = TallySentiments(ReadFileSentiments(fileName))
        sentimentColors = [(0.0, 0.42, 0.24), (1.0, 0.83, 0.0), (0.88, 0.23, 0.20)]

        #sentimentTypes = ["positive", "neutral", "negative"]
        #sentimentTotals = [sentimentTally["positive"], sentimentTally["neutral"], sentimentTally["negative"]]
        #sentimentColors = [(0.0, 0.42, 0.24), (1.0, 0.83, 0.0), (0.88, 0.23, 0.20)]
        bar = matplot.bar(sentimentTypes, sentimentTotals, label=sentimentTypes, width=0.6, color=sentimentColors)
        matplot.tight_layout(pad=6)
        matplot.title(header, pad=16, wrap=True)
        matplot.xlabel(xLabel, labelpad=16)
        matplot.ylabel(yLabel, labelpad=16)
        matplot.xlim(right=4)
        matplot.bar_label(bar, label_type='center', padding=4, fmt='%0.2f')
        matplot.legend(title='Sentiment Colors', bbox_to_anchor=(1, 1))
        matplot.savefig("Data\\Plots\\post-" + id + "-comments-sentiments-plot.png" )
        matplot.close()
    except Exception as e:    
        raise e

# Check if Sentiment is Valid Option, return bool
def IsValidSentiment(sentiment: str) -> bool:
    if sentiment == "positive" or sentiment == "neutral" or sentiment == "negative":
        return True
    return False

# Check if File Name is a output comment sentiment file, return bool
def IsValidSentimentFile(fileName: str) -> bool:
    if re.match(r"^post-", fileName) and re.search(r"-comments-sentiments.txt$", fileName):
        return True
    return False