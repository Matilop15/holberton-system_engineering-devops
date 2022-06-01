#!/usr/bin/python3
"""Querie to the reddit API"""
import requests


def top_ten(subreddit):
    """returns the number of subscribers"""
    reddit = 'http://reddit.com/r/{}/hot.json'
    head = {'User-agent': 'root:mati:v1'}
    res = requests.get(reddit.format(subreddit), headers=head)
    if res.status_code != 200:
        print("None")
    else:
        filter = res.json().get('data').get('children')
        for i in filter[:10]:
            print(i.get('data').get('title'))
