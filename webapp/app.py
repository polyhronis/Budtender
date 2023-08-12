```python
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webapp.db'
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start_webapp', methods=['POST'])
def start_webapp():
    message = request.form.get('message')
    new_message = Message(content=message)
    db.session.add(new_message)
    db.session.commit()
    flash('Webapp started successfully!', 'success')
    return redirect('/')

@app.route('/correct_errors', methods=['POST'])
def correct_errors():
    errors = request.form.get('errors')
    if errors:
        flash('Errors corrected successfully!', 'success')
    else:
        flash('No errors found.', 'info')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
```