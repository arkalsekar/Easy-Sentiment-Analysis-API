import os
from fastapi import FastAPI, Header
from textblob import TextBlob
import json

app = FastAPI()

# For Verification and Rate Limits. Will be Implemented later
# with open('tokens.json', 'r+') as f:
#     tokens = json.load(f)
#     print(tokens['tokens'])
        

@app.get("/")
def read_root():
    return {"Welcome to ": "Sentiment Analysis API", "Creator": "Abdul Rehman", "Endpoints": {"/get-sentiments/your-sentence", "/get-subjectives/your-sentence", }}
        
@app.get("/get-sentiments/{sentence}")
def get_sentiments(sentence: str):
    blob = TextBlob(sentence)
    polarity = blob.polarity
    
    if polarity==0:
        sentiment = 'Neutral'
    elif polarity>0:
        sentiment = 'Positive'
    else:
        sentiment = 'Negative'                
    return {'sentence':sentence, 'polarity': polarity, 'sentiment': sentiment}

    
@app.get("/get-subjectives/{sentence}")
def get_sentiments(sentence : str):
    blob = TextBlob(sentence)
    subjectivity = blob.subjectivity
    if (subjectivity==0.50) or (subjectivity>0.30):
        subjective = 'Fairly Subjective'
    elif subjectivity>0.75:
        subjective = 'Subjective'
    elif subjectivity<0.30:
        subjective = 'Not Subjective'
    else:
        subjective = 'Too Sujective'                
    
    return {'sentence':sentence, 'subjetivity': subjectivity, 'is_subjective': subjective}
