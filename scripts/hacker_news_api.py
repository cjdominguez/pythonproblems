"""

hacker new api -> gather most recent stories save url for eventually being sent using Twilio
steps:

- make a get request to retrieve information from
  hacker-news @ "https://hacker-news.firebaseio.com/v0/topstories.json"

-

"""

import requests

# make the api call and store the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(url)
print("Status Code: " , response.status_code)

# store API response in managed variable
story_ids = response.json()
story_lookups = []

# only collect and send top 3 stories
for story_id in story_ids[:3]:
    print(story_id)



print(response.json())

#print(len(response.json()))




"""
submission_dict={
            'title':response_dict['title'],
            'hn_link':f"http://news.ycombinator.com/item?id={submission_id}",
            'comments':response_dict['descendants']
        }

"""
