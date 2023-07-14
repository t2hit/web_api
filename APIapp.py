import time

import requests


def get_top_stories_id():
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    params = {'print': 'pretty'}
    story_ids = requests.get(url, params).json()
    return story_ids


def get_story_by_id(story_id):
    url = f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json'
    response = requests.get(url)
    story = response.json()
    return story


def get_params_by_story(title, url="", **args):
    params = {"title": title,
              "link": url}
    return params


def main():
    story_ids = get_top_stories_id()

    for story_id in story_ids[:30]:
        time.sleep(1)
        story = get_story_by_id(story_id)
        if 'title' in story:
            params = get_params_by_story(**story)
            print(params)


if __name__ == '__main__':
    main()
