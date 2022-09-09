"""

hacker new api -> gather most recent stories save url for eventually being sent
using Twilio steps:

-   make a get request to retrieve information from
    hacker-news to retrieve story_ids

-   make another request for each story_id's to get the unique stories information

-   title: title of the article
    by: author
    time: of post
    url: for post to corresponding site (different from link)
    link: for hacker news post (different than url)

-   store that info in a dictionary

"""
import requests

# make the api call and store the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(url)
print("Status Code: " , response.status_code)
#print(response.json()) # will give entire LIST of unique id's for those specific topstories

# store API response in managed variable
story_ids = response.json() # this will store the id's in a new variable to be used later
#print(story_ids)


story_lookups = [] # going to store a nested dictionary eventually once we get the neccaracy json data from each story

# only collect and send top 3 stories
for story_id in story_ids[:3]:
    """
    another API call to retrieve items from Hacker News - so we already made one
    request above to retrieve the orginal id's - Now we need to make another
    request to get the rest of the information we need to include
    title, by, time, url from hacker news, link to original website
    """
    # simplified request compared to first
    data = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json')
    #print(data.status_code)
    # store preceding api call into dict_data
    dict_data = data.json()


    """
    title: title of the article
    by: author
    time: of post
    url: for post to corresponding site (different from link)
    link: for hacker news post (different than url)
    """
    submission_dict={
                'title':dict_data['title'],'by':dict_data['by'],'time':dict_data['time'],'url':dict_data['url'],
                'link':f"http://news.ycombinator.com/item?id={story_id}"
            }
    story_lookups.append(submission_dict)


for x in story_lookups:
    print(x)
