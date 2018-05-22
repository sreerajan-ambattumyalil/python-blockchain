# Simple blockchain implementation in Python

#### Dependencies

* Python 3.6.5

#### Virtual environment

```
pip install virtualenv
virtualenv -p /usr/bin/python3.6 bc
source bc/bin/activate
```

#### Build and deploy

```
pip install -r requirements.txt

export FLASK_APP=main.py

GET http://localhost:5000/block_chain
POST http://localhost:5000/block_chain?data=<block data>
``` 
    