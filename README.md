# ClientServerCliChat

## Setup environment

> init python env

```
python3 -m venv venv && . ./venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
```

> init db

```
sqlite3 Notes.db
>.databases
>.quit
```

> init db structure

```
PYTHONPATH=./ python3 db_management/init_db.py
```

## Start client application

```
python3 app.py
```

## Start server application
