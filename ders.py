from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Mustafa/Desktop/Code/ders/ders.db'
db = SQLAlchemy(app)
class ders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dersbaslik = db.Column(db.String(80))
    dersakts = db.Column(db.Integer)
    complete = db.Column(db.Boolean)
@app.route("/")
def index():
    dersler = ders.query.all()
    return render_template("index.html", dersler = dersler)
@app.route("/add",methods=["POST"])
def addDers():
    dersbaslik= request.form.get("dersbaslik")
    dersakts= request.form.get("dersakts")
    yeniDers = ders(dersbaslik=dersbaslik,dersakts=dersakts,complete=False)
    db.session.add(yeniDers)
    db.session.commit()
    return redirect(url_for("index"))
@app.route("/edit/<string:id>")
def editdersler(id):
    dersler = ders.query.filter_by(id=id).first()
    dersler.complete = not dersler.complete
    db.session.commit()
    return redirect(url_for("index"))
@app.route("/delete/<string:id>")
def deletedersler(id):
    dersler = ders.query.filter_by(id=id).first()
    db.session.delete(dersler)
    db.session.commit()
    return redirect(url_for("index"))
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
