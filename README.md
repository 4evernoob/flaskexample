# flaskexample
Basic movie reccomender using flask and gensim with this same project one can build a docker container modifying app.py.
To process recomendations you can use postman using POST method with the next json structure

{"name":"movie"}

movie is any of the movies in the movies.csv file(be careful some movies are not valid because lack of data)
