from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import json
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
import similarityFinder as sF
import joblib
ex=open("extracted.json","r")
e=json.load(ex)
para=[]
for i in e:
    para.append(sF.punct(e[i]['abstract']))
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(para)


def elbow():
    wcss=[]
    n=10
    for i in range(1,n):
        model = KMeans(n_clusters=i, init='k-means++',n_init=10,random_state=42)
        model.fit(X)
        wcss.append(model.inertia_)
    plt.plot(range(1,n),wcss)
    plt.title('The Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()


def model(noOfClusters):
    model = KMeans(n_clusters=noOfClusters, init='k-means++',n_init=10, random_state=42)
    model.fit(X)
    joblib.dump(model,"kmeans.pkl")

if __name__=="__main__":
    elbow()
    noOfClusters=input("enter the number of clusters")
    model(noOfClusters)
