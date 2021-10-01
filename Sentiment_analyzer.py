from textblob import TextBlob
sentence=input("Have you watched the Movie? How was it! : ")
edu=TextBlob(sentence)
p=edu.sentiment.polarity
print("The reaction is: ",end=' ')
if p<0:
    print(":( 'Negative'")
elif p>0 and p<1:
    print(":) 'Positive'")
else:
    print(":| 'Neutral'")
