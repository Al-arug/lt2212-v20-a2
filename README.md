# LT2212 V20 Assignment 2

    part1: 

Tokenized: outputs a nested list of all the documents where words are splitted, lowered and of length more than 2. >2 is to exclude non-content word such as "a" and "an". 

words: A dictionary to save all the words in the corpus and they are in dict form to avoid the repetetions of the word.

corpus: is a list of dictionaries where each dictionary represent a document with words as keys and their counts as values. Counting using collection library.

f: Initiating a numpy zero array of shape of the length of the documents where each array has a shape of the length of the words. 

fillling the empty array:
Next... Is a for loop that itterates through each array by the index (i) then the second index points to a specific postion in the given array, the postion is taken using the word and it's location in words_index so that all the words get their count in straight column in the right order.. The count of the word is taken from the counts-dicts in corpus. 

Removing low frequency features: 
l: is a single array of the sum of all the columns. 
X: Removing all the columns that theire count represented in "l" is lower than 20.


    part4:  

Reduction with SVD:

    LDA:

             Accuracy:           precesion           recall              F1_score 
 
         0.6920424403183024 0.710919551681664, 0.6895392252573298, 0.6952536826403733      

    50%: 0.7883289124668436 0.8151132761875491, 0.7859479409625572, 0.7937498802536053
    24%:0.7572944297082228 0.7954088304406971, 0.7538596725784339, 0.7660748766395539 
    10%:0.6840848806366048 0.7600036878216532, 0.6803675295070122, 0.7047798930296965
    5%:0.6257294429708223  0.7012585632275532, 0.6221519816375604, 0.6418251182611727


    SVC:

        0.776657824933687   0.7765943884906583  0.774286902256094   0.7746973931989858
 

    50%: 0.7570291777188329 0.756645288299024, 0.7540988599469443, 0.7544686475621637
    24%:0.7482758620689656 0.7457904271271141, 0.7432400945354651, 0.7429840515679411
    10%:0.7214854111405835 0.7218303587172135, 0.7171314612919233, 0.7167263861129671
    5%:0.6904509283819629 0.6879071464563085, 0.6841769340320545, 0.6845032338855815


 The clear observation to draw from this diminstionality reduction of features is that the less features we have the lower the results of our evaluation becomes.However, It would not be very accurate to draw the same conclusion about LDA as it looks like that the 50% reduction scored higher than the evaluation when the whole features been trained. But it's only that, as the 50% remianed higher comparing to the more reduced features of 25% etc, meaning that I connot neither assume that the lower the features in LDA the higher the score would become, although it did get lower starting at below 50%. The better score in 50% in LDA can be interpreted as a reason that LDA fits for data that is placed in a linear form and it hapened to be more linear at the 50% percent features. 



    Bonus_part:


Reduction with PCA:

    LDA:

             Accuracy           precesion           recall              F1_score 
     
     
     
    50%:0.7787798408488064 0.8058193282458868, 0.7777623930207113, 0.786638785248339
    25%:0.7594164456233422 0.8075742219924564, 0.7569993185241428, 0.7712077148815523
    10%:0.6880636604774536 0.7507914683363812, 0.6832390676057468, 0.7041439535022321
    5&:0.6294429708222812  0.6991957216411007, 0.6239712721382221, 0.6453246006107012
      
    SVC:
    
    
         
    50%:0.7671087533156499 0.7690135136146057, 0.7643333149248576, 0.765343863999767
    25%:0.746419098143236 0.7455525602506164, 0.7424409870697742, 0.7423688356712098
    10%:0.7220159151193634 0.7241408746258522, 0.7197207470489675, 0.7200191044394741
    5&:0.7042440318302388 0.7029239937643335, 0.6998786439019418, 0.7000704925847543
    
 
    
    
    
    
    
    
