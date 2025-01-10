from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    data = {"title": "Projekt DevOps", "content": "Jakub Szwej - 14657"}
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)