from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
# Test to see that API key is loaded correctly
# print("API Key Loaded:", api_key)

client = OpenAI(api_key=api_key)

def analyze_sentiment(user_text):
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
        "role": "system",
        "content": [
            {
            "type": "text",
            "text": "You are analyzing sentiment within couples texts to each other. For each text input you will return whether the text is positive, neutral, or negative and a small classification of the subjectivity of the text. If the text is short, you will also return a suggested common text couples send to each other, only if necessary, that has a more positive sentiment."
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "I liked today, hang soon again?"
            }
        ]
        },
        {
        "role": "assistant",
        "content": [
            {
            "type": "text",
            "text": "The sentiment is positive.\nRewritten Version: \"I enjoyed today and would love to hang out again soon!\""
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "Be safe"
            }
        ]
        },
        {
        "role": "assistant",
        "content": [
            {
            "type": "text",
            "text": "The sentiment is positive.\nNo changes needed here—it's a caring and considerate message!"
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "im feeling tired"
            }
        ]
        },
        {
        "role": "assistant",
        "content": [
            {
            "type": "text",
            "text": "The sentiment is neutral."
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "I love you"
            }
        ]
        },
        {
        "role": "assistant",
        "content": [
            {
            "type": "text",
            "text": "The sentiment is positive.\nNo changes needed—your message is already warm and affectionate!"
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "Yeah its chill lol"
            }
        ]
        },
        {
        "role": "assistant",
        "content": [
            {
            "type": "text",
            "text": "The sentiment is positive or casual."
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "it was a pretty good conversation"
            }
        ]
        },
        {
        "role": "assistant",
        "content": [
            {
            "type": "text",
            "text": "The sentiment is positive."
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "can you come back to me already"
            }
        ]
        },
        {
        "role": "assistant",
        "content": [
            {
            "type": "text",
            "text": "The sentiment is neutral with a hint of impatience."
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "I love you"
            }
        ]
        },
        {
        "role": "assistant",
        "content": [
            {
            "type": "text",
            "text": "The sentiment is positive.\nNo changes needed—your message is already warm and affectionate!"
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "I hate you"
            }
        ]
        },
        {
        "role": "assistant",
        "content": [
            {
            "type": "text",
            "text": "The sentiment is negative. \n\nSuggested Rewritten Version: \"I'm really upset right now.\""
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "It is Saturday"
            }
        ]
        },
        {
        "role": "assistant",
        "content": [
            {
            "type": "text",
            "text": "The sentiment is neutral. \n\nSuggested Rewritten Version: \"It's Saturday! Let's make the most of it!\""
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": user_text
            }
        ]
        }
        
    ],
    temperature=0.7,
    max_tokens=125,
    top_p=0.5,
    frequency_penalty=0,
    presence_penalty=0,
    response_format={
        "type": "text"
    }
    )
    return response.choices[0].message.content

while True:
    user_input = input("Enter a text to analyze (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break

    sentiment_response = analyze_sentiment(user_input)
    print("Analysis:", sentiment_response)

