#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, make_response, current_app  
from flask_cors import cross_origin
from datetime import datetime
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper
import twitter

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator
    
app = Flask(__name__)
api = twitter.Api(
	consumer_key= 'NfrOmg2osL5l80uNCwqQ',
    consumer_secret= 'pH44EeZaqFLEO5badp5U8iiw46YNg1thO4UoYKcYftU',
    access_token_key= '1589638196-WcKd3zO2wt4Wg2AzLkWnTQcyRY97QU54xLvBQ1W',
    access_token_secret= 'Y2CpbokN04JN7PHxsGWcym036it06yogWPeliBNWw4DW8'
)

@crossdomain(origin='*') 
@app.route("/", methods=['GET', 'OPTIONS'])
def hello():
    return "Hello World!"
    
@crossdomain(origin='*')    
@app.route('/api', methods=['GET', 'OPTIONS'])
@app.route('/api/search/since/<int:sinceId>', methods=['GET', 'OPTIONS'])
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