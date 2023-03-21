import kmeansModel as kM
import similarityFinder as sF
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity

#load the model
model=joblib.load("kmeans.pkl")
cluster_assignments=model.labels_
order_centroids=model.cluster_centers_


def findSecondLargest(arr):
    secondLargest = 0
    largest = min(arr)
 
    for i in range(len(arr)):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
        else:
            secondLargest = max(secondLargest, arr[i])
    return secondLargest

def documentsSimilarityFinder(inputDocumentTitle):
    titleNum=sF.extracted[inputDocumentTitle]['id']
    requieredCluster=cluster_assignments[titleNum]
    cluster_documents=kM.X[cluster_assignments==requieredCluster]
    similarities=cosine_similarity(cluster_documents)
    index=0
    for j in range(len(cluster_assignments)): 
        if cluster_assignments[j]==requieredCluster:
            if j!=titleNum:
                index+=1
            else:
                break
    requierdSimilarities=list(similarities[index,:])
    indices = [j for j in range(len(cluster_assignments)) if cluster_assignments[j] == requieredCluster]
    topDocSimilarity=findSecondLargest(requierdSimilarities)
    topIndex=requierdSimilarities.index(topDocSimilarity)
    titleNo=indices[topIndex]
    return sF.getTitleFromNum(titleNo)
     


#similarity of documents with respect to centroid of the cluster
def cosineGraph():
    noOfCluster=max(cluster_assignments)
    for i in range(noOfCluster+1):
        cluster_documents = kM.X[cluster_assignments == i]
        cluster_centroid = order_centroids[i]
        similarities = cosine_similarity(cluster_documents, cluster_centroid.reshape(1,-1))
        indices = [j for j in range(len(cluster_assignments)) if cluster_assignments[j] == i]
        plt.scatter(range(len(similarities)), similarities, label=f"Cluster {i}")
    plt.title("Cosine Similarities within Clusters")
    plt.xlabel("Document Index")
    plt.ylabel("Cosine Similarity")
    plt.legend()
    plt.show()

if __name__=="__main__":
    title=input("enter the title: ")
    topTitle=documentsSimilarityFinder(title)
    print(f"Most similar document : {topTitle}")
    cosineGraph()
    