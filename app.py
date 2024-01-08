from flask import Flask, render_template, jasonify, request
app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Python Developer',
        'location': 'remote',
    },
    { 'id': 2,
      'title': 'java developer',
      'location': 'remote',
    },
  {
    'id': 3,
    'title': 'AI engineer',
    'location': 'remote',
  }
]
@app.route("/")
def hello_world():
    return render_template("home.html", jobs = JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

@app.route("/api/jobs")
def list_jobs():
  return jasonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)