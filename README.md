<!-- Add banner here -->
![Banner](https://i.imgur.com/j4SyTWD.png)



## Collaborators
- `18127080` **Kiều Vũ Minh Đức** ([@kvmduc](https://github.com/kvmduc))
- `18127231` **Đoàn Đình Toàn** ([@t3bol90](https://github.com/t3bol90))
## Instructor
- `HCMUS` **Trần Trung Kiên** ([@ttkien](ttkien@fit.hcmus.edu.vn))
- `HCMUS` **Phan Thị Phương Uyên** ([@ptpuyen](ptpuyen@fit.hcmus.edu.vn))

# Abstract

Automatic music playlist continuation is a task focused on `ACM Recommender Systems Challenge 2018`. It is specific case of sequential recommendation problem in recommendation system. Solving this problem also create a formula of playlist recommendation, given a set of `P` metadata of tracks which have the similarity features, the formula need to recommend `Q` track from the dataset related to `P`. In `Recsys Challenge`, Spotify released a dataset for participants to train their model. In context of this course, we will crawl playlist metadata by using `Sporify Developer API` and crawl external  data by parsing html on Spotify web-app version.

---
<div style="page-break-after: always"></div>

> To teachers of this course, please read the content of this file as a navigator for this project. Because we split the tasks and phrases into different notebook, it's inconvenient when go to each notebook and paste them the same content.


This report can be view at better render at [Hackmd site](https://hackmd.io/x1wAsXQeRtuhJIsQXA0r4A).


# Teamwork schedule
[Notion site](https://t3bol90.notion.site/Teamwork-d58a388013604464ac0a9eedaf81a39d)

# Slide

[Overleaf site](https://www.overleaf.com/read/dqszczyytsrv)

# Problem statement
How can I get a different recommended song from list tracks of my playlist ? Answer this question will solve the problem of sequential recommendation problem, with a user's playlist Q, we can offer/recommend them a list of suitable tracks which fit with their playlist. In this course, our team will use Machine Learning to solve this problem.

Our model is an system which tries to calculate the rating or score of how fit is a track to a playlist. For mathematics approach, the problem statement is defined by:
- Given a list of playlist Q, calculate score of each tracks in $\Omega'$.
- In recommendation stage, we choose $P$ tracks with highest score for recommendation.


# Table of contents

- [Abstract](#abstract)
- [Problem statement](#problem-statement)
- [Table of contents](#table-of-contents)
- [Installation](#installation)
- [Installation](#installation)
- [Collect data](#collect-data)
- [Explore Data Analysis](#explore-data-analysis)
- [Preprocessing Data & Modeling](#preprocessing-data-&-modeling)
- [Reflection](#reflection)



# Installation
[(Back to top)](#table-of-contents)

Install the customized version of min_ds-env:
```bash
!conda env create --file .\min_ds-env.yml --force
```

## Crawling notebook
[(Back to top)](#table-of-contents)

First, create a Developer API at https://developer.spotify.com/.
Put the Client ID and Serect ID to `config.yaml` file:
```yaml 
SPOTIPY_CLIENT_ID: "xxxxxxxxxxxxxxxxxxxxxxxxxx"
SPOTIPY_CLIENT_SECRET: "yyyyyyyyyyyyyyyyyyyyyyyyyy"
```

Then select `Restart Kernel` and `Run all` to re-run the experiment.

(Note that the `crawling.ipynb` take 30 mins to finish).

## Others
[(Back to top)](#table-of-contents)

To run this project, just go to each `notebook`, select `Restart Kernel` and `Run all` to re-run the experiment.

# Collect data:
[(Back to top)](#table-of-contents)

We use Spotify API over [`spotipy`](https://spotipy.readthedocs.io/en/2.19.0/) official package provided with Developer Token from Spotify API.

Instead of a GET request like this:
![](https://i.imgur.com/6Q3kVVb.png)

The `spotipy` way:
![](https://i.imgur.com/Xla0veA.png)

Read more about how it work in [`draft_crawl_data.ipynb`](source\crawling\draft_crawl_data.ipynb).

We crawled metadata of 4 objects: `playlist`, `artist`, `tracks`, `audio`.

![](https://i.imgur.com/pFToNYU.png)

# Explore Data Analysis
[(Back to top)](#table-of-contents)

See the result in [`explore_data_analysis.ipynb`](source\eda\explore_data_analysis.ipynb)

# Preprocessing Data & Modeling
[(Back to top)](#table-of-contents)

For each model: KMeans, DBSCAN and KNN, checkout result on:

```
source\model\
```

Our final result on R-precision metrics:

![](https://i.imgur.com/neovoTx.png)

# Reflection
[(Back to top)](#table-of-contents)

## Toan Doan
### Challenge I have
- I know WHAT it is? HOW to use it but I don't know WHY we have to use it or not to use it?
### How I overcome it
- More research, more reading, more practice
- Discuss with teammate and friends to get insight of problem
### What I have learned
- Data Science Research method, WHAT - HOW - WHY - WHAT IS THE BEST?

## Minh Duc

### Challenge I have
- I had is try to figure out what to do to solve this problem
- Algorithms take a huge amount of time to apply on the full tracks dataset (Preprocessing steps)
- How to evaluate the performance of algorithms (Metrics)
- Understanding my teammate’s works

### How I overcome it
- Referenced to other methods
- Meet my teammate to report the process more frequently

### What I have learned
- Learned how to teamwork, how to overcome when stuck with ideas,and learned how a data science project can be implemented
## Group
- With traditional Machine Learning approach:
    - Run the experiment with full 88819 tracks.
    - Using recommendation method in ML: Content filtering,Collaborative filtering, ...

- With the view of State-of-the-art method:
    - Try with some Deep Learning model from the Recsyc 2018 challenge:: Two-stage model architecture [4], hybrid recommender system combining features from text and audio [1],...

# References

[1] Andres Ferraro et al. “Automatic playlist continuation using a hybridrecommender system combining features from text and audio”. In:Proceedings of the ACM Recommender Systems Challenge 2018 on -RecSys Challenge ’18(2018).doi:10.1145/3267471.3267473.url:http://dx.doi.org/10.1145/3267471.3267473.

[2] Music Recommendation System using Spotify Dataset. Jan. 2021.url:https://www.kaggle.com/vatsalmavani/music-recommendation-system-using-spotify-dataset.prathamsharma123.Spotify

[3] EDA Recommendation System. Aug.2021.url:https://www.kaggle.com/prathamsharma123/spotify-eda-recommendation-system.MaksimsVolkovs et al. 

[4] “Two-stage Model for Automatic PlaylistContinuation at Scale”. In:Proceedings of the ACM RecommenderSystems Challenge 2018 on - RecSys Challenge 18(2018).


# Project structure:
[(Back to top)](#table-of-contents)
```
📦intro2ds_final_project
 ┣ 📂docs
 ┃ ┗ 📜SpotifyAPIDocs.html
 ┣ 📂source
 ┃ ┣ 📂crawling
 ┃ ┃ ┗ 📜draft_crawl_data.ipynb # nb of data crawling
 ┃ ┣ 📂data # data crawling
 ┃ ┃ ┣ 📜20210824_212829_artists.tsv
 ┃ ┃ ┣ 📜20210824_212829_audios.tsv
 ┃ ┃ ┣ 📜20210824_212829_playlists.tsv
 ┃ ┃ ┗ 📜20210824_212829_tracks.tsv
 ┃ ┣ 📂eda
 ┃ ┃ ┣ 📂data_description # description files
 ┃ ┃ ┃ ┣ 📜des_artist.csv
 ┃ ┃ ┃ ┣ 📜des_audio.csv
 ┃ ┃ ┃ ┣ 📜des_playlist.csv
 ┃ ┃ ┃ ┗ 📜des_tracks.csv
 ┃ ┃ ┣ 📜data_description.ipynb # description only
 ┃ ┃ ┗ 📜explore_data_analysis.ipynb # eda
 ┃ ┣ 📂images # visualized images
 ┃ ┃ ┣ 📜dbscan_7000tracks_13cluster.png
 ┃ ┃ ┣ 📜db_scan_dfpca2.png
 ┃ ┃ ┣ 📜db_scan_dftsne.png
 ┃ ┃ ┣ 📜ground_truth.png
 ┃ ┃ ┣ 📜kmeans_dfpca2.png
 ┃ ┃ ┣ 📜kmeans_dftsne.png
 ┃ ┃ ┗ 📜kmean_7000tracks_13cluster.png
 ┃ ┗ 📂model # model stuff
 ┃ ┃ ┣ 📜dbscan.ipynb
 ┃ ┃ ┣ 📜knn.ipynb
 ┃ ┃ ┣ 📜k_means.ipynb
 ┃ ┃ ┗ 📜utils.py
 ┣ 📜config.yaml # config for crawling
 ┗ 📜README.md
```

![Footer](https://i.imgur.com/PSMD4pJ.png)
