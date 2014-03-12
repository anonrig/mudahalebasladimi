var Twit = require('twit');

var twitter = new Twit({
	consumer_key: 'NfrOmg2osL5l80uNCwqQ',
    consumer_secret: 'pH44EeZaqFLEO5badp5U8iiw46YNg1thO4UoYKcYftU',
    access_token: '1589638196-WcKd3zO2wt4Wg2AzLkWnTQcyRY97QU54xLvBQ1W',
    access_token_secret: 'Y2CpbokN04JN7PHxsGWcym036it06yogWPeliBNWw4DW8'
});

twitter.get('search/tweets', 
		{ 	q:'mudahale', 
			count: 10,
			include_rts: true,
		}, function(err, reply) {
			console.log(reply);
		}
);

var stream = twitter.stream('statuses/sample');

stream.on('mudahale', function(tweet) {
	console.log(tweet);
});