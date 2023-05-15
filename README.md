# Twitter Joke Bot

This is a Python application that uses GPT4 from OpenAI to generate jokes and posts them on Twitter.


## Prerequisites

- Python 3.x
- OpenAI API key (paid for access to gpt4 api)
- Twitter API credentials (v2 - free)


## Getting OpenAI API Key

1. Visit the OpenAI website (https://platform.openai.com/signup/) and sign up for an account if you haven't already.

2. After logging in, go to the API section.

3. Here, you will find your API key. It will look something like this: sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx

4. Copy this key and save it. You will use this as your OPENAI_API_KEY environment variable.

5. Please note that OpenAI may have usage limitations and charges associated with it. Make sure you understand their pricing model before using the API extensively.


## Getting Twitter API Credentials

1. You must apply for a Twitter developer account and create an application.

2. Go to the Twitter Developer website (https://developer.twitter.com/en/apps) and sign in with your Twitter account.

3. Click on "Create an app" and fill out the application details.

4. After your application has been created, you will be taken to a page with your API keys (API key & secret, Access token & secret).

5. Make sure to also enable 3-legged OAuth in the "Authentication settings" and set the Callback URL to "https://127.0.0.1:8000" or any URL of your choosing if you plan to implement a callback.

6. Next, go to the "Keys and tokens" tab to find your CLIENT_ID, CLIENT_SECRET, API_KEY, API_SECRET_KEY, ACCESS_TOKEN, and ACCESS_TOKEN_SECRET.

7. Lastly, under "App settings", you will find the BEARER_TOKEN.

8. Save these credentials as you will use them as your environment variables.

Remember to keep these keys secure! Do not share them with anyone or publish them online. Always store them in a secure location, such as environment variables or a secure configuration file that is ignored by source control systems.


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    ```

2. Navigate into the project directory:
    ```bash
    cd your-repo-name
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Make a `.env` by creating a copy of the "template.env" file and filling in the relevant API keys and secrets.


## Usage

To run the application, use the following command:
```bash
python joke-tweeter.py
```

The script will generate a joke and post it on Twitter.


## Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.
