# iris-api

API to serve a classifier for the well-known iris dataset.

Build the docker image.

`docker-compose build.`

`docker-compose up -d`

Test example:
```
curl -X POST \
  'http://localhost:8008/predict' \
  --header 'Content-Type: application/json' \
  --data-raw '{ "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}'
```

Response example:
```
{ "sepal_length":5.1,
  "sepal_width":3.5,
  "petal_length":1.4,
  "petal_width":0.2,
  "flower_type":"setosa"}
```
See that the flower_type attribute was returned.
