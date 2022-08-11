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


Request and response examples using thunder client for VSCode
![image](https://user-images.githubusercontent.com/158303/184049055-e722f02e-ca39-4340-8d7d-9f62c3d7b878.png)
![image](https://user-images.githubusercontent.com/158303/184049083-0b3b7902-c643-4cca-bcbd-351e2c97e283.png)


To see the docs go to: http://localhost:8008/docs
