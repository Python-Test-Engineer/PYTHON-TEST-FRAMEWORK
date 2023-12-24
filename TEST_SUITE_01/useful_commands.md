Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

VS


python -m venv venv

.\venv\Scripts\activate

pip freeze > requirements.txt

python -m pip install -r requirements.txt

GIT

git rm -r --cached .

git remote remove origin

git remote add origin https://github.com/iwswordpress/drl-python-test.git

Flake8

flake8 --ignore=E1,E23,W503 path/to/files/

flake8 --exclude=venv --ignore=E501


### These two do the trick

```
pyrightconfig.json {
   "ignore": [
      "**"
   ]
}

# pylint: disable-all
```