## Tweet-Clustering
#### All_tweets.csv consists of all the tweets from the following speakers: 'JustinTrudeau', 'realDonaldTrump', 'ElizabethMay', 'AndrewScheer', 'theJagmeetSingh', 'elonmusk', 'BarackObama', 'HillaryClinton', 'MittRomney', 'SpeakerRyan', 'JoeBiden', 'SenJohnMcCain', 'narendramodi', 'algore', 'GavinNewsom', 'SarahPalinUSA', 'SpeakerBoehner' ####
#### I would recommend using virtual environments for this so:
    pip install virtualenv
#### From here, got to a directory where you'd like to save the environment and call
    python -m venv CP421_environment
#### Activate the environment and install requirements.txt:
    source CP421_environment/Scripts/activate
    pip install -r requirements.txt
#### If you're using eclipse, change the interpreter of the project to the directory:
    CP421_environments/Scripts/python.exe
#### and there shouldn't be anymore unresolved imports ####
#### To run tweet_grabber, you need to get the API tokens from registering. ####
#### Run doc2vec.py (if you have a model and want to load the file, run as is, otherwise uncomment everything that currently has a comment and comment out the Doc2Vec.load line). ####
#### Run k_means_processing.py (if you have the clusters already in clusters.pkl, comment #1 and uncomment #2, otherwise run as is). ####
