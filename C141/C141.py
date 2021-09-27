from flask import Flask,jsonify,request
import csv
allMovies=[]
with open("movies.csv") as f:
    reader=csv.reader(f)
    data=list(reader)
    allMovies=data[1:]
likedMovies=[]
unlikedMovies=[]
didnotwatch=[]


app=Flask(__name__)

@app.route("/get-movie")
def getMovie():
    return jsonify({
        "data":allMovies[0],
        "status":"success"
    })


@app.route("/liked-movies",methods=["POST"])
def likedMovies():
    movie=allMovies[0]
    allMovies=allMovies[1:]
    likedMovies.append(movie)
    return jsonify({
        "status":"success"
    }),201
@app.route("/unliked-movies",methods=["POST"])
def unlikedMovies():
    movie=allMovies[0]
    allMovies=allMovies[1:]
    unlikedMovies.append(movie)
    return jsonify({
        "status":"success"
    }),201
@app.route("/didnotwatch",methods=["POST"])
def didnotwatch():
    movie=allMovies[0]
    allMovies=allMovies[1:]
    didnotwatch.append(movie)
    return jsonify({
        "status":"success"
    }),201
if __name__ =="__name__":
    app.run()
