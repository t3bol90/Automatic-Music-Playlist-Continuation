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

# Table of contents

- [Abstract](#abstract)
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
if "spotipy" in conda_env_string:
    print("requirement has been installed")
else:
    print("install requirement")
    !conda env create --file .\min_ds-env.yml --force
```

<!-- (remove in final submission) -->
# Todo 
[(Back to top)](#table-of-contents)

- [x] Survey of the problem
- [x] Plan used for teamwork (Grantt file, current: TODO list) 
- [ ] Crawl data from Spotify API (Spotipy lib)
- [ ] Parse HTML from Spotify web-app
- [ ] Explore data 
- [ ] Preprocess data
- [ ] Reflection
- [ ] Slides
- [ ] Team up seminar


![Footer](https://i.imgur.com/PSMD4pJ.png)
