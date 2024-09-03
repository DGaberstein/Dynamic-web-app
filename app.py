from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///checklists.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class SwapBodyChecklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    arrival_date = db.Column(db.String(10))
    arrival_time = db.Column(db.String(5))
    truck_reg = db.Column(db.String(50))
    trailer_reg = db.Column(db.String(50))
    wb_reg_1 = db.Column(db.String(50))
    wb_reg_2 = db.Column(db.String(50))
    seal_no_1 = db.Column(db.String(50))
    seal_no_2 = db.Column(db.String(50))
    om_no = db.Column(db.String(50))
    q1 = db.Column(db.String(3))
    q2 = db.Column(db.String(3))
    q3 = db.Column(db.String(3))
    q4 = db.Column(db.String(3))
    q5 = db.Column(db.String(3))
    q6 = db.Column(db.String(3))

class DropTrailerChecklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    arrival_date = db.Column(db.String(10))
    arrival_time = db.Column(db.String(5))
    forwarding_agent = db.Column(db.String(50))
    trailer_reg = db.Column(db.String(50))
    om_no = db.Column(db.String(50))
    q1 = db.Column(db.String(3))
    q2 = db.Column(db.String(3))
    q3 = db.Column(db.String(3))
    q4 = db.Column(db.String(3))
    q5 = db.Column(db.String(3))
    q6 = db.Column(db.String(3))
    q7 = db.Column(db.String(3))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/swap_body', methods=['GET', 'POST'])
def swap_body():
    if request.method == 'POST':
        checklist = SwapBodyChecklist(
            arrival_date=request.form['arrival_date'],
            arrival_time=request.form['arrival_time'],
            truck_reg=request.form['truck_reg'],
            trailer_reg=request.form['trailer_reg'],
            wb_reg_1=request.form['wb_reg_1'],
            wb_reg_2=request.form['wb_reg_2'],
            seal_no_1=request.form['seal_no_1'],
            seal_no_2=request.form['seal_no_2'],
            om_no=request.form['om_no'],
            q1=request.form.get('q1'),
            q2=request.form.get('q2'),
            q3=request.form.get('q3'),
            q4=request.form.get('q4'),
            q5=request.form.get('q5'),
            q6=request.form.get('q6'),
        )
        db.session.add(checklist)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('swap_body.html')

@app.route('/drop_trailer', methods=['GET', 'POST'])
def drop_trailer():
    if request.method == 'POST':
        checklist = DropTrailerChecklist(
            arrival_date=request.form['arrival_date'],
            arrival_time=request.form['arrival_time'],
            forwarding_agent=request.form['forwarding_agent'],
            trailer_reg=request.form['trailer_reg'],
            om_no=request.form['om_no'],
            q1=request.form.get('q1'),
            q2=request.form.get('q2'),
            q3=request.form.get('q3'),
            q4=request.form.get('q4'),
            q5=request.form.get('q5'),
            q6=request.form.get('q6'),
            q7=request.form.get('q7'),
        )
        db.session.add(checklist)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('drop_trailer.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
