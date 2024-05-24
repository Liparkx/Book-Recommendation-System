import pickle
import streamlit as st
import numpy as np

st.header("Book Recommender System")

model = pickle.load(open('finalinfo/model.pkl', 'rb'))
books_name = pickle.load(open('finalinfo/books_name.pkl', 'rb'))
books_pivot = pickle.load(open('finalinfo/books_pivot.pkl', 'rb'))
final_rating = pickle.load(open('finalinfo/final_rating.pkl', 'rb'))

def fecth_poster(sugestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in sugestion:
        book_name.append(books_pivot.index[book_id])

    for name in book_name[0]:
        ids = np.where(final_rating['TITLE'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['IMAGE-URL-L']
        poster_url.append(url)
    
    return poster_url


def recommend_books(books_name):
    books_list = []
    book_id = np.where(books_pivot.index == books_name)[0][0]
    distances, sugestions = model.kneighbors(books_pivot.iloc[book_id,:].values.reshape(1, -1), n_neighbors=6)
     
    poster_url = fecth_poster(sugestions)

    for i in range(len(sugestions)):
        books = books_pivot.index[sugestions[i]]
        for j in books:
            books_list.append(j)
    
    return books_list, poster_url


selected_books = st.selectbox(
    "Type or Select a Book",
    books_name
)

if st.button('Show Recommendations'):
    recommended_books,poster_url = recommend_books(selected_books)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_books[1])
        st.image(poster_url[1])
    with col2:
        st.text(recommended_books[2])
        st.image(poster_url[2])
    with col3:
        st.text(recommended_books[3])
        st.image(poster_url[3])
    with col4:
        st.text(recommended_books[4])
        st.image(poster_url[4])
    with col5:
        st.text(recommended_books[5])
        st.image(poster_url[5])
