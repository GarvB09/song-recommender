import numpy as np, pandas as pd, streamlit as st

T = pd.read_csv("tracks.csv")
X = np.load("X.npy")
labels = T.track_name + " — " + T.artists
picked = st.multiselect("Songs you like", labels)

if picked:
    ids = T.index[labels.isin(picked)].values
    prof = X[ids].mean(0)
    s = X @ (prof / np.linalg.norm(prof))
    s[ids] = -np.inf
    st.dataframe(T.loc[np.argsort(-s)[:10], ["track_name", "artists", "track_genre"]])