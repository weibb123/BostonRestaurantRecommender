# BostonRestaurantRecommender

Link to WEB APP: https://weibb123-bostonrestaurantrecommender-app-esfyxy.streamlit.app/

<h2>Problem statement</h2>
Recommend user Boston Restaurants

<h2>Backstory</h2>
As Bostonian, I keep track of the restaurant name and details whenever I visit one. As time goes, I have a list of 44 restaurants in Boston area. I want to use these data to make a recommender for my friends who are new to boston or when cannot think of a place to go!

<h2>Methods</h2>
Dataset comes from my personal list of 44 Boston restaurants in Notion.

Dataset:

restaurant name

restaurant type: korean, chinese, coffee, brtunch, ...  we will predict based on restaurant type

rating (from yelp)

img url of restaurant (from google)

First, using nltk to clean up text before using Machine Learning algorithms

Next, use TFIDF(term frequency-inverse document frequency) to measure how frequent a word appear and also how frequent this word appear throughout other documents.

This algorithm TFIDF is used to create matrix of TFIDF on the dataset to then prepare using cosine similarity

then utilized cosine similarity to find similar restaurants based on user input.

<h2>Challenge</h2>
Because this is my first time trying to build ML APP and I didn't have strong expertise on front end. I decided to give streamlit a try and reading through the documentation which then help me build and deploy my app efficiently.

<h2>Result</h2>
<img src="https://user-images.githubusercontent.com/84426364/208280331-f7cefcef-fcb6-4d8e-b397-5c2f282b6bff.png">

<h2>Conclusion</h2>
Scale up with Neural Network Algorithms

This ML model does not need any data about other users since it recommends specific to this user. Easy to scale up to large number of user.

Model can capture specific interests of a user.

However, model can only make recommendations based on existing interests of the user, which not fully allowing user to expand their existing interest.

Try hybrid recommender(collaborative recommender) requires user-information which need backend implemented
