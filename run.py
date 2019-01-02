import webRender as w
import twitterStream as t
import csv

if __name__ == '__main__':

    # starting Flask application
    app = w.create_app()  # Create application with our config file
    app.run(host='0.0.0.0', port='8001')  # Run our application

    # load results from last session

    # setup twitter stream
    keywords = ['kristiansand', 'kilden', 'fake news']
    languages = ['en']
    db = 'db/tweets.csv'

    twitter_streamer = t.TwitterStreamer()
    twitter_streamer.stream_tweets(db, keywords, languages)
