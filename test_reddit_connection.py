
import praw

def test_reddit_connection():
    try:
        reddit = praw.Reddit(
            client_id="CF6kIM4Ltf-C1mkvu5lChA",
            client_secret="P9h4PEP4z6iffYDwT4UMK5SxoggqRg",
            user_agent="data_pipeline"
        )

        print("Testing Reddit connection...")
        print(f"Read-only mode: {reddit.read_only}")

        subreddit = reddit.subreddit("dataengineering")
        posts = subreddit.top(time_filter="day", limit=5)

        print("\nFetching posts...\n")
        for post in posts:
            print(f"Title: {post.title}")
            print(f"Score: {post.score}")
            print(f"Author: {post.author}")
            print(f"URL: {post.url}\n")

        print("Connection to Reddit is working!")
    except Exception as e:
        print(f"Error connecting to Reddit: {e}")


test_reddit_connection()