import praw

reddit = praw.Reddit(client_id='KS3WhZR4SDHvDQ', client_secret='7khAfZXIkoPfdM6eIT6UlJkeO9hdpg', user_agent='testscrape')
stonks = []
subreddit = input("sub: ")
hot_posts = reddit.subreddit(subreddit).top("day", limit=20)
for post in hot_posts:
    print(post.title)
    # title = post.title
    # split = title.strip().split(" ")
    # for word in split:
    #     if len(word) < 5 and len(word) > 1 and word == word.upper() and word not in stonks and any(char.isdigit() for char in word) == False:
    #         stonks.append(word)

# print(stonks)
