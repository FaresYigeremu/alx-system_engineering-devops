#!/usr/bin/python3
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    
    headers = {"User-Agent": "your_custom_user_agent"}
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            
            post_titles = [post['data']['title'] for post in data['data']['children'][:10]]
            
            for title in post_titles:
                print(title)
        else:
            print(None)
    except Exception as e:
        print(None)
