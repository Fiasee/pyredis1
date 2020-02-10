from flask import Flask
from redis import Redis

app = Flask(__name__)
#redis = Redis(host="localhost", port=6379, db=0)

@app.route("/")
def hello():
    #visits = redis.incr('counter')
    html = "<h3>Welcome Brother!</h3>" \
           #"<b>Visits:</b> {visits}" \
           #"<br/>"
    #return html.format(visits=visits)
    return html
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082)