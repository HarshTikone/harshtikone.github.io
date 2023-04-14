import streamlit as st
import pandas as pd
import pickle as pc
import requests


def get_poster(mov_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key='
                            '61076793ff76365fb1703a81695d9f8e'.format(mov_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']


def recommend(movie):
    mov_ind = df[df['title'] == movie].index[0]
    dis = similar_movies[mov_ind]
    mov = sorted(list(enumerate(dis)), reverse=True, key=lambda x: x[1])[1:11]

    rec_list = []
    pos_list = []
    for i in mov:
        pos_id = df.iloc[i[0]].id
        rec_list.append(df.iloc[i[0]].title)
        pos_list.append(get_poster(pos_id))

    return rec_list, pos_list


st.title('Movie Recommender System')


mov_list = pc.load(open("movietitle.pkl", "rb"))
df = pd.DataFrame(mov_list)

similar_movies = pc.load(open("similar_movies.pkl", "rb"))

option = st.selectbox(
    'What Movies are you interested in',
    df['title'].values)

if st.button('Recommend'):
    reco, pos = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(reco[0])
        st.image(pos[0])
    with col2:
        st.text(reco[1])
        st.image(pos[1])
    with col3:
        st.text(reco[2])
        st.image(pos[2])
    with col4:
        st.text(reco[3])
        st.image(pos[3])
    with col5:
        st.text(reco[4])
        st.image(pos[4])

    
    col6, col7, col8, col9, col10 = st.columns(5)
    with col6:
        st.text(reco[5])
        st.image(pos[5])
    with col7:
        st.text(reco[6])
        st.image(pos[6])
    with col8:
        st.text(reco[7])
        st.image(pos[7])
    with col9:
        st.text(reco[8])
        st.image(pos[8])
    with col10:
        st.text(reco[9])
        st.image(pos[9])
