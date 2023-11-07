#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, after=None):
    counts = {}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Set a custom User-Agent and disable following redirects
    headers = {'User-Agent': 'RedditDataAnalyzer/1.0 (ALX Africa)'}
    params = {'limit': 100}  # Limit the number of posts to 100 (maximum)

    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        # Extract and parse the titles of the posts
        for post in data.get('data', {}).get('children', []):
            title = post.get('data', {}).get('title', '').lower()
            words = title.split()

            # Count the occurrences of keywords in the title
            for word in word_list:
                if word.lower() in words:
                    counts[word] += words.count(word.lower())

        # Check if there are more pages (pagination) and continue the recursion
        after = data.get('data', {}).get('after')
        if after:
            return count_words(subreddit, word_list, after, counts)

        if len(counts) == 0:
            return

        # If no more pages, print the sorted results
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
    else:
        return
