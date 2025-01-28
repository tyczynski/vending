# Vending

A RSS feed generator that creates RSS feeds from websites that don't offer native RSS functionality.

## Currently supports

- Paul Graham's Essays (https://paulgraham.com/articles.html)

## Installation 

```sh
# create env
python -m venv env

# activate env
source env/bin/activate

# install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Usage

```sh
# Start the server
python app.py
```

Access RSS feeds via: `http://localhost:5000/feed/<website_id>`
