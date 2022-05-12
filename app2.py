from re import X
from flask import Flask,render_template,request ,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

x="this is the new world"
example_sent = x
 
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
    if request.method =="POST":
        print("post")
        description=request.form['description']
        detector= detector(description=description)

       # db.session.add(detector)
       # db.session.commit()
        user =request.form["nm"]
        return redirect(url_for("user",usr=user))
    else:    
        return render_template('index.html')
#def luser(usr):
    #return f"<h1>{usr}</h1>"       
'''def my_form_post():
    description = request.form['description']
    processed_text = description.upper()
    return processed_text'''
    
if __name__ == "__main__":
    app.run(debug=True)
