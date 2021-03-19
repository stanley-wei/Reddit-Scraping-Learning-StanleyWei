import praw
import gpt_2_simple as gpt2

# gpt2.download_gpt2()
reddit = praw.Reddit(client_id='KS3WhZR4SDHvDQ', client_secret='7khAfZXIkoPfdM6eIT6UlJkeO9hdpg', user_agent='testscrape')
stonks = []
subreddit = input("sub: ")

hot_posts = reddit.subreddit(subreddit).top("year", limit=1000)
file_name = subreddit + "_titles.csv"
file_path = "post_titles/" + file_name

titles = open(file_path, "w")
for post in hot_posts:
    titles.write(post.title + ",\n")
titles.close()

titles = open(file_path, 'r')
sess = gpt2.start_tf_sess()
gpt2.finetune(sess, dataset=file_path, model_name='124M', steps=50, restore_from='fresh', run_name= subreddit + '_post_titles', print_every=10, sample_every=10, save_every=10)

output = gpt2.generate(sess, run_name=subreddit + '_post_titles', prefix="<|startoftext|>", truncate="<|endoftext|>", include_prefix=False, nsamples=10)
print(output)

titles.close()
