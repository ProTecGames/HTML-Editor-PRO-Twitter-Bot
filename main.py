import os
import tweepy
import google.generativeai as genai

# Twitter API Authentication
client = tweepy.Client(
    bearer_token=os.getenv("TWITTER_BEARER_TOKEN"),
    consumer_key=os.getenv("TWITTER_API_KEY"),
    consumer_secret=os.getenv("TWITTER_API_SECRET"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_SECRET")
)

# Gemini API Configuration
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config={
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 280,
        "response_mime_type": "text/plain",
    },
    system_instruction="You are a Twitter bot. Your job is to pos tweets tagging @TanmayD8791248 and making his fun using sarcasm related to random things mainly to his VFX skill, make him feel angry, cry, laugh all at same time. Keep them human-like and within Twitter's character limit. Reply only with the tweet content, nothing else. You can use double meaning lines in hindi language. Hinglish language mein tweet krna hai kise bhi topic se realte krke random",
)

def generate_tweet():
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message("Generate a funny, sarcastic, and engaging tweet.")
    return f"@TanmayD8791248 {response.text.strip()}"

def post_tweet():
    """Posts a tweet using the generated content."""
    tweet_text = generate_tweet()
    try:
        client.create_tweet(text=tweet_text)
        print(f"Tweeted: {tweet_text}")
        return {"status": "success", "tweet": tweet_text}
    except tweepy.TweepyException as e:
        print(f"Error posting tweet: {e}")
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    post_tweet()
