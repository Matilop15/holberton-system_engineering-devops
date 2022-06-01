#!/usr/bin/python3
"""Querie to the reddit API"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    reddit = 'http://reddit.com/r/{}/about.json'
    head = {'User-agent': 'root:mati:v1'}
    res = requests.get(reddit.format(subreddit), headers=head)
    if res.status_code != 200:
        return 0
    return res.json().get('data', {}).get('subscribers', 0)
