import argparse
import random
from sklearn.datasets import fetch_20newsgroups
from sklearn.base import is_classifier
import numpy as np
from collections import Counter
from sklearn.decomposition import TruncatedSVD
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import precision_recall_fscore_support
from sklearn.preprocessing import StandardScaler
random.seed(42)
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import PCA

###### PART 1
#DONT CHANGE THIS FUNCTION
def part1(samples):
    #extract features
    X = extract_features(samples)
    assert type(X) == np.ndarray
    print("Example sample feature vec: ", X[0])
    print("Data shape: ", X.shape)
    return X


def extract_features(samples):
    print("Extracting features ...")
   
    tokenized=[[word.lower() for word in document.split() if word.isalpha() if len(word)>2]for document in samples]
    words={word for document in tokenized for word in document} # a dict to get only 1 token of each unique word/feature
    words_index={x:y for y,x in enumerate(words)}
   
    corpus=[]
    for document in tokenized:
        v = dict(Counter(document))       
        corpus.append(v)
        
    f= np.zeros((len(samples),len(words)),dtype=int) 
    i=0
    for doc in corpus:
        for word in doc:
            f[i][words_index[word]]=doc[word]
        i+=1
        
    l= np.sum(f,axis=0)          
    x=f[:,(l>20)]

    return  x
  
##### PART 2
#DONT CHANGE THIS FUNCTION
def part2(X, n_dim):
    #Reduce Dimension
    print("Reducing dimensions ... ")
    X_dr = reduce_dim(X, n=n_dim)
    assert X_dr.shape != X.shape
    assert X_dr.shape[1] == n_dim
    print("Example sample dim. reduced feature vec: ", X[0])
    print("Dim reduced data shape: ", X_dr.shape)
    return X_dr


def reduce_dim(X,n):
   
    svd = TruncatedSVD(n_components=n)
    return svd.fit_transform(X)




##### PART 3
#DONT CHANGE THIS FUNCTION EXCEPT WHERE INSTRUCTED
def get_classifier(clf_id):
    if clf_id == 1:
        clf = LDA() # <--- REPLACE THIS WITH A SKLEARN MODEL
    elif clf_id == 2:
        clf = SVC(kernel='linear') # <--- REPLACE THIS WITH A SKLEARN MODEL
    else:
        raise KeyError("No clf with id {}".format(clf_id))

    assert is_classifier(clf)
    print("Getting clf {} ...".format(clf.__class__.__name__))
    return clf

#DONT CHANGE THIS FUNCTION
def part3(X, y, clf_id):
    #PART 3
    X_train, X_test, y_train, y_test = shuffle_split(X,y)
    

    #get the model
    clf = get_classifier(clf_id)

    #printing some stats
    print()
    print("Train example: ", X_train[0])
    print("Test example: ", X_test[0])
    print("Train label example: ",y_train[0])
    print("Test label example: ",y_test[0])
    print()


    #train model
    print("Training classifier ...")
    train_classifer(clf, X_train, y_train)
    

    # evalute model
    print("Evaluating classcifier ...")
    evalute_classifier(clf, X_test, y_test)
    

def shuffle_split(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,shuffle=True)
   # scaler = StandardScaler()  #Normalizing data to adjust in a scale 1 to -1 of which the mean is 0 
    #scaler.fit(X_train)
    #X_train = scaler.transform(X_train)
    #X_test = scaler.transform(X_test)
    
    return X_train, X_test, y_train, y_test



def train_classifer(clf, X, y):
    assert is_classifier(clf)
    
    model=clf.fit(X,y)
    return model

        

def evalute_classifier(clf, X, y):
    assert is_classifier(clf)
    y_predict=clf.predict(X)
    accuracy=metrics.accuracy_score(y, y_predict)
    precesion_recall_f1score=precision_recall_fscore_support(y, y_predict, average='macro')
    print(accuracy)
    print(precesion_recall_f1score)
 
    return (accuracy, precesion_recall_f1score)

######
#DONT CHANGE THIS FUNCTION
def load_data():
    print("------------Loading Data-----------")
    data = fetch_20newsgroups(subset='all', shuffle=True, random_state=42)
    print("Example data sample:\n\n", data.data[0])
    print("Example label id: ", data.target[0])
    print("Example label name: ", data.target_names[data.target[0]])
    print("Number of possible labels: ", len(data.target_names))
    return data.data, data.target, data.target_names


#DONT CHANGE THIS FUNCTION
def main(model_id=None, n_dim=False):

    # load data
    samples, labels, label_names = load_data()
    
    
    


    #PART 1
    print("\n------------PART 1-----------")
    X = part1(samples)
    print(X)

    #part 2
    if n_dim:
        print("\n------------PART 2-----------")
        X = part2(X, n_dim)

    #part 3
    if model_id:
        print("\n------------PART 3-----------")
        part3(X, labels, model_id)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-n_dim",
                        "--number_dim_reduce",
                        default=False,
                        type=int,
                        required=False,
                        help="int for number of dimension you want to reduce the features for")

    parser.add_argument("-m",
                        "--model_id",
                        default=False,
                        type=int,
                        required=False,
                        help="id of the classifier you want to use")

    args = parser.parse_args()
    main(   
            model_id=args.model_id, 
            n_dim=args.number_dim_reduce
            )
