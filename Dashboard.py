
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


file_path = "github_dataset.csv"
github_data = pd.read_csv(file_path)


language_stats = github_data.groupby('language').agg({
    'stars_count': 'mean',
    'forks_count': 'mean',
    'issues_count': 'mean',
    'pull_requests': 'mean',
    'contributors': 'mean'
}).sort_values(by='stars_count', ascending=False).head(10)


st.title("GitHub Projects Dashboard")
st.write("This dashboard showcases insights from GitHub repository data.")


st.subheader("Top 10 Programming Languages by Average Stars")
st.dataframe(language_stats)


st.subheader("Average Stars by Programming Language")
plt.figure(figsize=(10, 5))
plt.bar(language_stats.index, language_stats['stars_count'], color='skyblue')
plt.xlabel("Programming Language")
plt.ylabel("Average Stars")
plt.xticks(rotation=45)
plt.title("Average Stars by Programming Language")
st.pyplot(plt)


st.subheader("Average Forks by Programming Language")
plt.figure(figsize=(10, 5))
plt.bar(language_stats.index, language_stats['forks_count'], color='lightgreen')
plt.xlabel("Programming Language")
plt.ylabel("Average Forks")
plt.xticks(rotation=45)
plt.title("Average Forks by Programming Language")
st.pyplot(plt)
