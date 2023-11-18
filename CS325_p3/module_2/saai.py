# saai_module: Sentiment Analysis AI Module

    # Input: Takes in User text

    # Output: Analyzed Sentiment from OpenAI API and its input Text, returned as a Pair List: [sentiment, text]

    # Usage: Quickly retrieve sentiment of user text using OpenAI API

# Dependencies
    # Standard Module(s)
import time
    # Installed Module(s)
import openai
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
                        {"role": "system", "content": "You will be provided with a comment, and your task is to classify its sentiment, your response must be: 'positive', 'neutral', or 'negative'"},
                        {"role": "user", "content": text}
                    ],
                    timeout=15.0
                )
                sentiment = response.choices[0].message.content
                return [sentiment, text]
        except Exception as e:    
            if e:   
                mrkr.Magenta('OpenAI API Timeout, Retrying Query...')    
                requests -= 1
                if requests <= 0:
                    raise e
                time.sleep(1)    
            else:    
                raise e

# Create List of Sentiment Pair List's -> [[sentiment, text], [sentiment, text], [sentiment, text]]
# size by default is small (50) to avoid OpenAI API request limit breaches
def CreateTextSentimentList(textList: [str], size: int = 50) -> []:
    sentimentList = []
    i = 0
    for text in textList:
        if i >= size:
            break
        # Limit comment char count per comment to avoid high token usage and improve processing times for each comment
        if len(text) >= 10 or len(text) <= 512:
            sentiment = QueryTextSentiment(text)
            sentimentList.append(sentiment)
            if i % 5 == 0:
                mrkr.Cyan("\tSentiment Query Progress: " + str((i/size) * 100) + "%")
            i += 1
    return sentimentList