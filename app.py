from pyexpat import model
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///detector.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class detector(db.model):
    sno=db.Column(db.Integer, primary_key=True)
    description=db.Column(db.String(500),nullable=False)

    def __repr__(self) -> str:
        return f"{self.description}"
@app.route("/")
def hello_world():
    return render_template('index.html')
    #return "<p>Hello, World!</p>"
if __name__ == "__main__":
    app.run(debug=True)