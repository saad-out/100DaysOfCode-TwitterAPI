#!/usr/bin/python3
"""
Handle authentication and create the `api` instance
"""
import os
import json
import tweepy
import sys


# Get `credentials.json` file path
current_path = os.path.abspath(__file__)
credentials_path = os.path.join(os.path.dirname(current_path), 'credentials.json')

# Load credentials from file if exists
try:
    with open(credentials_path, "r") as cred_file:
        credentials = json.load(cred_file)
except FileNotFoundError:
    sys.stderr.write("Your `credentials.json` file is not present, or not located in the required location !\n")
    exit(1)

# Authenticate
auth = tweepy.OAuthHandler(credentials.get('api_key'), credentials.get('api_key_secret'))
auth.set_access_token(credentials.get('access_token'), credentials.get('access_token_secret'))

# Create API instance
api = tweepy.API(auth)
