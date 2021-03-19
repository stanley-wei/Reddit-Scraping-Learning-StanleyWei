import praw
import gpt_2_simple as gpt2

# gpt2.download_gpt2()
reddit = praw.Reddit(client_id='KS3WhZR4SDHvDQ', client_secret='7khAfZXIkoPfdM6eIT6UlJkeO9hdpg', user_agent='testscrape')
subreddit = input("sub: ")
sess = gpt2.start_tf_sess()
output = gpt2.generate(sess, run_name=subreddit + '_post_titles', prefix="<|startoftext|>", truncate="<|endoftext|>", include_prefix=False, nsamples=1)
print(output)

titles.close()
