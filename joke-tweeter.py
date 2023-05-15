import openai
import tweepy
from dotenv import load_dotenv
import os
import random

# Load environment variables
load_dotenv()

# Set OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

# Set your Twitter API credentials
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
app_key=os.getenv('API_KEY')
app_secret=os.getenv('API_SECRET_KEY')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
bearer_token_value = os.getenv('BEARER_TOKEN')


def choose_random_prompt(filename):
    with open(filename, 'r') as file:
        prompts = file.readlines()
    return random.choice(prompts).strip()


def generate_response(prompt):

    messages = [
        {"role": "user", "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        max_tokens=8000,
        temperature=1.0,
        messages=messages
    )

    return response.choices[0].message['content']


def post_joke():

    # Generate a joke from a random prompt, specifying it's twitter specific
    prompt = choose_random_prompt('joke-prompts.txt')+ " This is for twitter, so keep within character restrictions and use hashtags."
    joke = generate_response(prompt)

    # Initialize the Tweepy client
    client = tweepy.Client(bearer_token=bearer_token_value, 
                        consumer_key=app_key, 
                        consumer_secret=app_secret, 
                        access_token=access_token, 
                        access_token_secret=access_token_secret)

    # Post the joke
    response = client.create_tweet(text=joke)

    print(f"Your joke has been posted!\n {response}")

# Test the function
try:
    post_joke()
except Exception as e:
    print("An error occurred: ", e)