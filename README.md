TWITTER-MUTER

Python script to mute or unmute all Twitter users you are following. Simply follow these steps:

1) go to https://apps.twitter.com/
    - figure out your consumer key (token), consumer secret, access token key, access token secret
    - if you do not have an app already, create a bogus one
 
2) open up twitter-muter.py
3) In line 5, input the appropriate fields (consumer key, consumer secret, etc.)
4) Go to your command line and do the following:
    - pip install python-twitter
    - python3 twitter_muter.py (or twitter_unmuter.py)
    
** Sometimes there is a cap on how many APIs the program can use. If the program does not mute/unmute all of the accounts you are following, wait 25-30 mins, and then run the program again
