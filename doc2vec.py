import gensim
from gensim.test.utils import get_tmpfile
from gensim.models.doc2vec import Doc2Vec
import pickle

tweet_file = open('all_tweets.csv')

# preprocessed = list()
tweets = list()

# id = 0

for tweet in tweet_file:
    tweets.append(gensim.utils.simple_preprocess(tweet))
#     preprocessed.append(gensim.models.doc2vec.TaggedDocument(tweet, [id]))
#
#     id += 1
#
# tweet_file.close()
#
# model = gensim.models.doc2vec.Doc2Vec(vector_size=500, min_count=2, epochs=40)
#
# model.build_vocab(preprocessed)
#
# model.train(preprocessed, total_examples=model.corpus_count, epochs=model.epochs)
#
# model.save(get_tmpfile("doc2ve.model"))

model = Doc2Vec.load(get_tmpfile("doc2ve.model"))

# tweet_of = =open('tweetVectors.csv', 'w')

vectors = list()

for tweet in tweets:
    vectors.append(model.infer_vector(tweet))

tf = open('yeet.pkl', 'wb')

pickle.dump(vectors, tf)