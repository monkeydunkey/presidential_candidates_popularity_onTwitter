# presidential_candidates_popularity_onTwitter
This is the code base for my CSE-573 project

The aim of the project is to build a classifier to predict the  sentiments of people by their tweets and then use it to identify their political preferences. Further, Using this information we will analyse the popularity of each of the candidate and try to predict who will win.
To achieve this we will build an end to pipeline that would consist of the following five subsystems:

1. Datagrabber: Using Twitter’s public API download and store tweets related to the candidates and their campaign. This would handle both historical as well real-time data pulls
2. Data-cleaner: Clean the data collected by the data grabber in order to make it ready for analysis. This will also handle both real time and historical data
3. Learning-module : Using the historical data pulled from twitter build and compare various models such as: nearest neighbour clustering to identify the various groups of people and store the best model among them. The best model will be calculated based on its correlation to the actual polls conducted by various organization.
4. Data-modeller: Using the model generated in the learning phase classify new tweets into the various categories
5. Data-visualization: This will visualize all the current trends as per our model and its comparison with other poll results

Datagrabber Module - datagrabber/queries.json contains the various parameters that can be set to pull data from twitter. 
Following are the parameters that can be set.

1. "StartDate": Start date,
2. "Days" : No of days for which data is needed,
3. "queries": An array of query terms,
4. "maxTweets": No of tweets to be pulled for each day

The data is pulled by scrapping Twitter's website so it might or might not work. On the other hand as it does not uses the public API there is no rate limit.

Apart from the Datagrabber module rest all of the modules are merged in one jupyter notebook - SentimentAnalysis_Experiments.ipynb.

P.S. Many files were created on a as need basis for the eperiment and hence there is no code for the creation of those files. 
