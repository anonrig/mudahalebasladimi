#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from flask_cors import cross_origin
from datetime import datetime
import twitter

app = Flask(__name__)
api = twitter.Api(
	consumer_key= 'NfrOmg2osL5l80uNCwqQ',
    consumer_secret= 'pH44EeZaqFLEO5badp5U8iiw46YNg1thO4UoYKcYftU',
    access_token_key= '1589638196-WcKd3zO2wt4Wg2AzLkWnTQcyRY97QU54xLvBQ1W',
    access_token_secret= 'Y2CpbokN04JN7PHxsGWcym036it06yogWPeliBNWw4DW8'
)

@cross_origin()
@app.route("/")
def hello():
    return "Hello World!"
    
@app.route('/api', methods=['GET'])
@app.route('/api/search/since/<int:sinceId>', methods=['GET'])
def search(sinceId=None):
	resultSet = []
	
	results = api.GetSearch('mudahale', since_id=sinceId)
	
	for item in results:
		resultSet.append({
		'id': item.user.id,
		'createdAt': datetime.fromtimestamp(item.now).isoformat(), 
		'favoriteCount': item.favorite_count, 
		'retweetCount': item.retweet_count, 
		'screen_name': item.user.screen_name, 
		'text': item.text, 
		'thumbnail': item.user.profile_image_url, 
		'isRetweeted': item.retweeted, 
		'isFavorited': item.favorited})

	return jsonify({ 'result': resultSet})
		
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)