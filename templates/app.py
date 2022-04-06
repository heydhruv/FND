from flask import Flask,render_template,request 
from flask_sqlalchemy import SQLAlchemy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 
example_sent = """"""
 
stop_words = set(stopwords.words('english'))
 
word_tokens = word_tokenize(example_sent)
 
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
 
filtered_sentence = []
 
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
 
print(word_tokens)
print(filtered_sentence)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///detector.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class detector(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    description=db.Column(db.String(500),nullable=False)

    def __repr__(self) -> str:
        return f"{self.description}"
@app.route("/",methods=["GET", "POST"])
def hello_world():
    if request.method=='POST':
        example_sent=request

    return render_template('index.html')
    #return "<p>Hello, World!</p>"
if __name__ == "__main__":
    app.run(debug=True,port=8000)