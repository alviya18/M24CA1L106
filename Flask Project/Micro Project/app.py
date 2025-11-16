from flask import Flask, render_template, url_for

app = Flask(__name__)

SOUNDS = [
    {
        "id": 1,
        "title": "துளி துளி ",
        "album": "Movie",
        "file": "assets/songs/song1.mp3",
        "cover": "assets/images/cover1.jpg"
    },
    {
        "id": 2,
        "title": "ജ്യൂപ്പിറ്റർ മഴ",
        "album": "Album",
        "file": "assets/songs/song2.mp3",
        "cover": "assets/images/cover2.jpg"
    },
    {
        "id": 3,
        "title": "அவள் குழல்",
        "album": "Movie",
        "file": "assets/songs/song3.mp3",
        "cover": "assets/images/cover3.jpg"
    },
    {
        "id": 4,
        "title": "IDFC",
        "album": "Album",
        "file": "assets/songs/song4.mp3",
        "cover": "assets/images/cover4.jpeg"
    }
]

@app.route('/')
def index():
    # Build full URLs for HTML
    for s in SOUNDS:
       s['url'] = url_for('static', filename=s['file'])
       s['img'] = url_for('static', filename=s['cover'])

    return render_template("index.html", sounds=SOUNDS)

if __name__ == "__main__":
    app.run( debug=True)

