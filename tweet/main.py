#!/usr/bin/python3
"""
This is a script that helps you tweet everyday about your progress
in the #100DaysOfCode challenge using the Twitter API
"""


def tweet():
    """
    Construct the tweet content and post it using the `api`
    """
    import json
    import os
    import tweepy
    import sys
    from twitter_api import api

    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Get current day for the challenge
    day_path = os.path.join(current_dir, 'current_day.json')
    try:
        with open(day_path, "r") as day_file:
            day_dict = json.load(day_file)
            current_day = day_dict.get('current_day')
    except FileNotFoundError:
        sys.stderr.write("Your tweet day file `current_day.json` is not present, or not located in the required location !\n")
        exit(1)

    # Get content of the tweet
    content_path = os.path.join(current_dir, 'tweet.txt')
    try:
        with open(content_path, "r") as content_file:
            content = content_file.read()
    except FileNotFoundError:
        sys.stderr.write("Your tweet content file `tweet.txt` is not present, or not located in the required location !\n")
        exit(1)
    
    # Construct the complete content of the tweet
    final_tweet = ""

    final_tweet += "#100DaysOfCode\n\n"
    final_tweet += "Day {}:\n".format(current_day)
    final_tweet += content.rstrip("\n")

    # Post tweet
    try:
        api.update_status(status=final_tweet)
    except tweepy.errors.Unauthorized:
        sys.stderr.write("Invalid credentials !\n")
        exit(1)

    print("Posted successfully")
    print("-------------------")
    print(final_tweet)
    print("-------------------")

    # Increment day
    with open(day_path, "w") as day_file:
        day_dict['current_day'] = current_day + 1
        json.dump(day_dict, day_file)


if __name__ == '__main__':
    tweet()
