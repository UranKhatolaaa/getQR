## 1. Install
First, check that python 3.9 is installed on your system, and is set to be the default python interpreter on the command line. You can do this check by running the following command in the terminal:
```sh
which python
```
If you have multiple versions of python installed, you can use pyenv to manage the versions.

Second, check that you have poetry installed by running the following command in the terminal:
```sh
poetry --version
```
If it's not installed, you can install it by using the following command in the terminal:
```sh
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```
If poetry is still not found, it might be because you're using Z shell and need to manually add it to PATH by adding the following statement to ~/.zprofile
```sh
export PATH="$HOME/.poetry/bin:$PATH"
```

Third, once you have python 3.9 with poetry installed and available on the command line, clone this repo in this way:
```sh
git clone https://github.com/zjohn77/dataviz.git
```

Fourth, change into the directory just created by the git clone statement and then install all dependencies by:
```sh
poetry install
```

At this point, your Plotly Dash app should be ready to be used.


## 2. Use
```
poetry shell
gunicorn app:server
```
Once the gunicorn server is up and running, point your browser to [localhost:8000](http://localhost:8000/)