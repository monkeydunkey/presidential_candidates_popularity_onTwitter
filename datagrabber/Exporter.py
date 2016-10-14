# -*- coding: utf-8 -*-
import sys
import getopt
import got
import datetime
import codecs
import argparse
import datetime
outputFile = codecs.open("tweets.csv", "a+", "utf-8")

outputFile.write('username;date;retweets;favorites;text;geo;mentions;\
				  hashtags;id;permalink')

def dataExporter(argv):
	if len(argv) > 4 or len(argv) < 3:
		print 'You must only pass the following parameters - query, since, until. Optional - maxTweets'
		return
	try:
		tweetCriteria = got.manager.TweetCriteria()
		tweetCriteria.since = argv['since']
		tweetCriteria.until = argv['until']
		tweetCriteria.querySearch = argv['query']
		if 'maxTweets' in argv:
			tweetCriteria.maxTweets = argv['maxTweets']

		print 'Searching...'
		def receiveBuffer(tweets):
			for t in tweets:
				outputFile.write(('\n%s;%s;%d;%d;"%s";%s;%s;%s;"%s";\
								%s' % (t.username, t.date.strftime("%Y-%m-%d %H:%M"),
								       t.retweets, t.favorites, t.text, t.geo,
									      t.mentions, t.hashtags, t.id, t.permalink)))
			outputFile.flush()
			print 'More %d saved on file...\n' % len(tweets)

		got.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)

	except Exception:
		print 'Arguments parser error, ensure that the parameters passed are since, until and query' + argv
	finally:
		outputFile.close()
		print 'Done. Output file generated "tweets.csv".'

if __name__ == '__main__':
	days = 26
	startDate = datetime.datetime.strptime('2016-09-05', '%Y-%m-%d')
	while days > 0:
		endDate = startDate + datetime.timedelta(days=1)
		dataExporter({'query': 'hillary OR trump', 'since': startDate.strftime('%Y-%m-%d')
					, 'until': endDate.strftime('%Y-%m-%d'), 'maxTweets':50000})
		startDate = endDate
		days -= 1
