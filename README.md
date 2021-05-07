# Mlopsinabox

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._


#### [Project homepage](https://github.com/sharathtirumalaraju/mlopsinabox)

#### Installing MLOps setup environment
----------
MLOps working environment can be installed on Windows and Linux distributions.
 
- Ubuntu 20.04 or any linux distribution

```bash
$ pip install python ansible
```
```bash
$ ansible-playbook mlopsinabox.yml
```

- Windows

    - Download git from [git_download](https://git-scm.com/downloads) and install git.
    - Install pip package manager for windows
    - Install all required packages with pip
        ```bash
        $ pip install -r requirements.txt
        ```
     
### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    python -m cookiecutter https://github.com/sharathtirumalaraju/mlopsinabox


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

    ├── LICENSE
    ├── README.md               <- The top-level README for developers using this project.
    ├── data
    │   ├── external            <- Data from third party sources.
    │   ├── interim             <- Intermediate data that has been transformed.
    │   ├── processed           <- The final, canonical data sets for modeling.
    │   └── raw                 <- The original, immutable data dump.
    ├── models                  <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks               <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                              the creator's initials, and a short `-` delimited description, e.g.
    │                              1.0-jqp-initial-data-exploration`.
    │
    ├── references              <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports                 <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures             <- Generated graphics and figures to be used in reporting
    │
    ├── deploy
    │   ├── Dockerfile          <- Intermediate data that has been transformed.
    │   ├── app.py              <- The final, canonical data sets for modeling.
    │   └── requirements.txt    <- The original, immutable data dump.
    │
    ├── requirements.txt        <- The requirements file for reproducing the analysis environment, e.g.
    │                              generated with `pip freeze > requirements.txt`
    │
    ├── setup.py                <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                     <- Source code for use in this project.
    │   ├── __init__.py         <- Makes src a Python module
    │   │
    │   ├── data                <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features            <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models              <- Scripts to train models and then use trained models to make
    │   │   │                      predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization       <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    ├── config.ini              <- configuration for git,dvc and mlflow

{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

--------
