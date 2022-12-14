import pickle
import pandas as pd
import streamlit as st
from streamlit import session_state as session
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel

def load_data():
    df = pd.read_csv('cleaned_data.csv')
    return df

new_df = load_data()
listRec = new_df['name'].tolist() 
tfidf = TfidfVectorizer()
TFmatrix = tfidf.fit_transform(new_df['type'])
mapping = pd.Series(new_df.index, index = new_df['name'])
similarity_matrix = linear_kernel(TFmatrix,TFmatrix)

# Next we will make the recommender function that recommend restaurants using cosine similarity
def recommend(name, count):
    restaurant_index = mapping[name] # get the index of input name restaurant

    # get similarity values with other restaurants
    # similarity score = list of index and similarity matrix
    similarity_score = list(enumerate(similarity_matrix[restaurant_index]))

    # sort in descend order
    similarity_score = sorted(similarity_score, key = lambda x: x[1], reverse=True)

    # get the scores of top restaurants based on input count
    similarity_score = similarity_score[1:count+1]

    # return restaurants name using the mapping series
    indices = [i[0] for i in similarity_score]

    return new_df[['name', 'type', 'rating', 'image']].iloc[indices]


## main structure of the app
dataframe = None
st.title("""Boston restaurants Recommendation System""")
st.text("")
st.text("")
st.text("")

session.options = st.selectbox(label="Select a restaurant you previous tried!", options=listRec)
st.text("")
st.text("")


buffer1, col1, buffer2 = st.columns([1.45, 1, 1])

is_clicked = col1.button(label="Recommend")

if is_clicked:
     dataframe = recommend(session.options, 3)
     col1, col2, col3 = st.columns(3)
     with col1:
        st.header(dataframe['name'].iloc[0])
        st.image(dataframe['image'].iloc[0])
     with col2:
        st.header(dataframe['name'].iloc[1])
        st.image(dataframe['image'].iloc[1])
     with col3:
        st.header(dataframe['name'].iloc[2])
        st.image(dataframe['image'].iloc[2])


