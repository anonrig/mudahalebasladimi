var express = require('express');
var Twit = require('twit');
var cors = require('cors');

var app = express();
app.use(cors());

var twitter = new Twit({
	consumer_key: 'NfrOmg2osL5l80uNCwqQ',
    consumer_secret: 'pH44EeZaqFLEO5badp5U8iiw46YNg1thO4UoYKcYftU',
    access_token: '1589638196-WcKd3zO2wt4Wg2AzLkWnTQcyRY97QU54xLvBQ1W',
    access_token_secret: 'Y2CpbokN04JN7PHxsGWcym036it06yogWPeliBNWw4DW8'
});

app.get('/api', function(req, res){
	var resultSet = [];
	twitter.get('search/tweets', 
			{ 	q:'mudahale', 
				count: 50,
				include_rts: true,
			}, function(err, reply) {
				reply = reply['statuses'];
				reply.forEach(function(item) {
					var hash = {};
					hash['id'] = item.id;
					hash['createdAt'] = new Date(item.created_at);
					hash['retweetCount'] = item.retweet_count;
					hash['favoriteCount'] = item.favorite_count;
					hash['screen_name'] = item.user.screen_name;
					hash['thumbnail'] = item.user.profile_image_url;
					hash['isRetweeted'] = item.retweeted;
					hash['isFavorited'] = item.favorited;
					hash['text'] = item.text;
					resultSet.push(hash);
				})
				res.send({'result': resultSet});
			}
	);
});

app.get('/api/search/since/:id', function(req, res) {
	var id = req.params.id,
		resultSet = [];
	twitter.get('search/tweets', 
			{ 	q:'mudahale', 
				count: 50,
				include_rts: true,
				since_id: id
			}, function(err, reply) {
				reply = reply['statuses'];
				reply.forEach(function(item) {
					var hash = {};
					hash['id'] = item.id;
					hash['createdAt'] = new Date(item.created_at);
					hash['retweetedCount'] = item.retweet_count;
					hash['favoriteCount'] = item.favorite_count;
					hash['screen_name'] = item.user.screen_name;
					hash['thumbnail'] = item.user.profile_image_url;
					hash['isRetweeted'] = item.retweeted;
					hash['isFavorited'] = item.favorited;
					hash['text'] = item.text;
					resultSet.push(hash);
				})
				res.send({'result': resultSet});
			}
	);
});


var server = app.listen(8080, function() {
	console.log('Listening on port %d', server.address().port);
});