import webRender as w
import twitterStream as t

import configparser

if __name__ == '__main__':
    # move all of this to util.py
    # https://stackoverflow.com/questions/13034496/using-global-variables-between-files

    # get settings from file
    print('!!!!!!!!!!!!!!')
    print('Opening settings file...')
    config = configparser.ConfigParser()
    config.readfp(open(r'config.cfg'))

    flask = config['FLASK OPTIONS']
    settings = config['APPLICATION']

    # get network settigns
    print('Getting network settings...')
    host = flask['HOST']
    port = flask['PORT']
    print('Host: {} Port: {}'.format(host, port))

    # get keyword (might be list)
    print('Getting keyword(s)...')
    keywords = settings['KEYWORDS'].split(',')
    print (keywords)

    # get language (might be list)
    print('Getting language(s)...')
    languages = settings['LANGUAGE'].split(',')
    print (languages)

    # setup twitter stream
    print('Initialize twitter stream...')
    twitter_streamer = t.TwitterStreamer()
    twitter_streamer.stream_tweets(settings['DB'], keywords, languages)

    # starting Flask application
    print('Initialize Flask...')
    app = w.create_app()  # Create application
    app.run(host=host, port=port)  # Run application
