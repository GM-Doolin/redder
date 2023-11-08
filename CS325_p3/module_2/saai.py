# saai_module: Sentiment Analysis AI Module

    # Input: Takes in User text

    # Output: Analyzed Sentiment from OpenAI API and its input Text, returned as a Pair List: [sentiment, text]

    # Usage: Quickly retrieve sentiment of user text using OpenAI API

# Dependencies
    # Standard Module(s)

    # Installed Module(s)
import openai
    # Local Module(s)

clientAI = openai.OpenAI()

###### ###### ###### ###### ######
###### Interface For saai   ######
###### ###### ###### ###### ######

# Query OpenAI API (GPT-3.5-turbo) for Sentiment Analysis of Text, returns value pair for sentiment operation: [sentiment, text]
def QueryTextSentiment(text: str) -> []:
    try:
        if text:
            response = clientAI.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You will be provided with a comment, and your task is to classify its sentiment, your response must be: 'positive', 'neutral', or 'negative'"},
                    {"role": "user", "content": text}
                ]
            )
            sentiment = response.choices[0].message.content
            return [sentiment, text]
        return None
    except Exception as e:
        raise e
    
# Create List of Sentiment Pair List's -> [[sentiment, text], [sentiment, text], [sentiment, text]]
# size by default is small (50) to avoid Open API request limits
def CreateSentimentTextList(textList: [str], size: int = 50) -> []:
    sentimentList = []
    i = 0
    for text in textList[:size]:
        sentimentList.append(QueryTextSentiment(text))
        i += 1
    return sentimentList