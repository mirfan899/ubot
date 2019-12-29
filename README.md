installing rasa
```shell
pip install rasa==1.4.6
pip install rasa-x==0.22.2 --extra-index-url https://pypi.rasa.com/simple
```

### Train the model
```shell script
python -m rasa train
```

### Run Rasa server
```shell script
python -m rasa run
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