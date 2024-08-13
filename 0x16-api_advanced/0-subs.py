#!/usr/bin/python3
"""a function that queries the Reddit API and returns the number of subscribers"""
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    headers = {"User-Agent": "your_custom_user_agent"}
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            
            subscriber_count = data['data']['children'][0]['data']['subscriber_count']
            
            return int(subscriber_count)
        else:
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
