import twitter


# Enter your Twitter API credentials here
api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='',
                  sleep_on_rate_limit=False)

# declaring empty list
followingList = []

# initializing cursor
cursor = -1


while cursor != 0:
    # calling API with cursor value
    friends = api.GetFriendsPaged(cursor=cursor)

    # printing the friends list from that call
    print(friends[2])

    # adding all those friends to the list
    for friend in friends[2]:
        followingList.append(friend.AsDict()["id"])

    # updating the cursor
    cursor = friends[0]

unmutedList = []
cursor = -1

while cursor != 0:
    unmuteCall = api.GetMutesIDsPaged(cursor=cursor)
    print(unmuteCall)

    for unmute in unmuteCall[2]:
        unmutedList.append(unmute)

    cursor = unmuteCall[0]

for unmute in unmutedList:
    print(unmute)

unmuteCalls = 0

alreadyUnmuted = 0
unmuted = 0

# printing all the people you follow
print("Processing mutes:")
for follow in followingList:

    if follow in unmutedList:
        try:
            api.DestroyMute(user_id=follow)
            unmuteCalls += 1
            print("Unmute calls is now " + str(unmuteCalls))

        except twitter.error.TwitterError:
            print("Ran out of API calls")
            print("Unmuted " + str(muted) + " and " + str(alreadyUnmuted) + " were already unmuted")
            print("Users left to process: " + str(len(followingList) - (alreadyUnmuted + unmuted)))
            break

        print("unmuting: " + str(follow))
        unmuted += 1
    else:
        # do nothing
        print("already unmuted: " + str(follow))
        alreadyUnmuted += 1

print("followingList length: " + str(len(followingList)))
print("already unmuted count: " + str(alreadyUnmuted))
print("Unmuted count: " + str(unmuted))
print("total processed is: " + str(alreadyUnmuted + unmuted))
