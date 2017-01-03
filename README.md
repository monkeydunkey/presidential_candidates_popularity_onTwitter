# Presidential Candidates Popularity on Twitter
This is the code base for my CSE-573 project. We analysed the tweets related to US 2016 presidential candidates  

The aim of the project was to build a classifier to predict the people's sentiment by their tweets and then use it to identify their political preferences. Using this information we then  analysed the popularity of each of the candidate and tried to predict who will win.
The solution is divided into the follwing subsystems:

1. Datagrabber: Using Twitter’s public API download and store tweets related to the candidates and their campaign. This would handle both historical as well real-time data pulls
2. Data-cleaner: Clean the data collected by the data grabber in order to make it ready for analysis. Folowing is the processing performed:
	- Extract hashtags and emojis
	- Remove the letter '#'
	- Remove english stopwords
	- Remove user mentions
	- Remove Urls
	- Convert words to their logical root
3. Learning-module : Using the hashtags and emojis as a distant label for sentiments. we created a small sample set for the purposes of training and comparing our statistical models. But first we needed to convrert our text in to feature. To create features out of the text the following methods were tried out:
	- Count Vectorizer: Use the frequency of n-grams as features
	- TF-IDF Vectorizer: Calculate tf-idf scores for the n-grams
using these feature we trained our learning models. Following machine learning models were used:
	- Random Forests
	- Scalar Vector: Linear kernel
	- Gradient boosting
4. Data-modeller: Using scoring accuracy on the test set, we determined the best combination of machine learning model and feature. Using the best model for each candidate, we predicted the sentiments for the rest of the downloaded dataset. 
5. Data-visualization: We visualized the positive, neutral and negative tweet for each of the candidate as a time series data for the date range for which we ran our experiment

All the code for cleaning and modeling the data as well as the final analysis is present in the SentimentAnalysis_Experiments.ipynb file. Description of methods used can be found in the jupyter notebook itself  

## Datagrabber Module 
	datagrabber/queries.json contains the various parameters that can be set to pull data from twitter. 
	Following are the parameters that can be set.

	1. "StartDate": Start date,
	2. "Days" : No of days for which data is needed,
	3. "queries": An array of query terms,
	4. "maxTweets": No of tweets to be pulled for each day

	The data is pulled by scrapping Twitter's website so it might or might not work. On the other hand as it does not uses the public API there is no rate limit.


P.S. Many files were created on a as need basis for the eperiment and hence there is no code for the creation of those files. 
