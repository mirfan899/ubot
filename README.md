## Install Urdu model
```shell script
pip3 install ur/ur_model-0.0.0.tar.gz
```

## Installing rasa
```shell script
pip install rasa==1.8.1
pip install rasa-x==0.26.1 --extra-index-url https://pypi.rasa.com/simple
```

### Train the model
```shell script
python -m rasa train
```

### Run Rasa server
```shell script
python -m rasa run
## run with core policy
python -m rasa run --enable-api --cors "*"
```

### Run the custom actions
```shell script
python -m rasa run actions
```

### Some issues to fix if happens
maybe related to sanic errors if so then update.
```shell script
pip install sanic==19.9.0
```