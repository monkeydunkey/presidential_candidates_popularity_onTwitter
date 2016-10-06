# presidential_candidates_popularity_onTwitter
This is the code base for our CSE573 project

The aim of the project is to analyse the sentiments of people in their tweets and using to identify which way they lean politically left or right. Further, Using this information we will analyse the popularity of each of the candidate and try to predict who will win.
To achieve this we will build an end to pipeline that would consist of the following five subsystems:

1. Datagrabber: Using Twitter’s public API download and store tweets related to the candidates and their campaign. This would handle both historical as well real-time data pulls
2. Data-cleaner: Clean the data collected by the data grabber in order to make it ready for analysis. This will also handle both real time and historical data
3. Learning-module : Using the historical data pulled from twitter build and compare various models such as: nearest neighbour clustering to identify the various groups of people and store the best model among them. The best model will be calculated based on its correlation to the actual polls conducted by various organization.
4. Data-modeller: Using the model generated in the learning phase classify new tweets into the various categories
5. Data-visualization: This will visualize all the current trends as per our model and its comparison with other poll results

Datagrabber Module - Historical data pull implemented. Exporter.py file pulls all 100000 tweets for a given query 'currently set to hillary' for the time range '2016-07-25' to '2016-09-05'
