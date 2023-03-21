import similarityFinder as sF
import bestSimilarityFinder as bF
from flask import Flask,render_template,request
app=Flask(__name__)
allTitles=sF.getTitles()

@app.route('/')
def webDeploy():
    return render_template('home.html')

@app.route('/2docSimilarity')
def docSimilarityPage():
    return render_template('2docSimilarity.html',similarity="",similarityText="",allTitles=allTitles)

@app.route('/2docSimilarity',methods=["POST"])
def docSimilarityFinder():
    if request.method=="POST":
        first=request.form['first']
        second=request.form['second']
        first=sF.abstract(first)
        second=sF.abstract(second)
        similarity=sF.similarityFinder(first,second)
        return render_template("2docSimilarity.html",similarity=str(similarity)+"%",similarityText="The Similarity is:",allTitles=allTitles)
    
@app.route('/bestSimilarity')
def clusterSimilarity():
    return render_template("bestDoc.html",data='',allTitles=allTitles)

@app.route('/bestSimilarity',methods=["POST"])
def clusterSimilarityData():
    if request.method=="POST":
        title=request.form['Input']
        data=''
        data='Most similar document : '+bF.documentsSimilarityFinder(title)
        return render_template("bestDoc.html",data=data,allTitles=allTitles)

if __name__=="__main__":
    app.run(debug=True,host="localhost")