from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import Geometry

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin@localhost/project'
db = SQLAlchemy(app)


class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    point = db.Column(Geometry(geometry_type='POINT', srid=4326), nullable=False)
    fill_type = db.Column(db.String(100), nullable=False)
    colors = db.Column(db.ARRAY(db.String), nullable=False)
    angle = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Area %r>' % self.id


@app.route('/', methods=['GET'])
def index():
    areas = Area.query.all()
    return jsonify(areas)


@app.route('/', methods=['POST'])
def index():
    area = Area(id=request.json['id'],
                name=request.json['name'],
                description=request.json['description'],
                point=request.json['point'],
                fill_type=request.json['fill_type'],
                colors=request.json['colors'],
                angle=request.json['angle'])
    return jsonify(area)


if __name__ == "__main__":
    app.run(debug=True)
