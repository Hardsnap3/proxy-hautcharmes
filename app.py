from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/rss')
def proxy_rss():
    url = "https://www.tourismecorreze.com/fr/rss-agenda-correze.html"
    r = requests.get(url)
    return Response(r.content, content_type=r.headers['Content-Type'])

@app.route('/')
def hello():
    return "Proxy RSS Haut Charmes OK !"

if __name__ == '__main__':
    app.run()
