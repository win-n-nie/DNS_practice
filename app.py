from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/memorial')
def bootstrap():
    return render_template('memorial.html')
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
