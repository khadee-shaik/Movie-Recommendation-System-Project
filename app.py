import streamlit as st
import pickle
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
    data=requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = 'https://image.tmdb.org/t/p/w500/' + poster_path
    return full_path


movies = pickle.load(open('movies_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies_list = movies['title'].values

import streamlit.components.v1 as components

imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")


imageUrls = [
    fetch_poster(1632),
    fetch_poster(299536),
    fetch_poster(17455),
    fetch_poster(2830),
    fetch_poster(429422),
    fetch_poster(9722),
    fetch_poster(13972),
    fetch_poster(240),
    fetch_poster(155),
    fetch_poster(598),
    fetch_poster(914),
    fetch_poster(255709),
    fetch_poster(572154)
   
    ]

imageCarouselComponent(imageUrls=imageUrls, height=200)




st.header('Movie Recommender System')
selectvalue = st.selectbox('select movie from dropdown ',movies_list)




def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda vector:vector[1])
    recommended_movies = []
    recommended_posters = []
    for i in movies_list[1:6]:
        movies_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movies_id))
    return recommended_movies , recommended_posters
    
    

if st.button('show recommand'):
    movie_name,movie_posters = recommend(selectvalue)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_posters[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_posters[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_posters[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_posters[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_posters[4])
    