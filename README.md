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
- [Todo](#todo)

# Installation
[(Back to top)](#table-of-contents)

Install the customized version of min_ds-env:
```bash
!conda env create --file .\min_ds-env.yml --force
```
In notebook enviroment, use this block to make sure you have updated enviroment:
```bash
conda_list = !conda list
conda_env_string = "".join(conda_list)
def check_installed_requirement(reqs):
    for req in reqs:
        if req in conda_env_string:
            print(f"requirement {req} has been installed")
        else:
            print(f"installing {req} by using conda ...")
            !conda install {req}
```

<!-- (remove in final submission) -->
# Todo 
[(Back to top)](#table-of-contents)

- [x] Survey of the problem
- [x] Plan used for teamwork (Grantt file, current: TODO list) 
- [x] Crawl data from Spotify API (Spotipy lib)
- [ ] Explore data 
- [x] Preprocess data
- [ ] Reflection
- [ ] Slides
- [ ] Team up seminar


![Footer](https://i.imgur.com/PSMD4pJ.png)
