from flask import Flask, render_template, request, flash
from download_video import download_video

app = Flask(__name__)
app.config["SECRET_KEY"] = "hello"

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        link = request.form.get("link")
        print(link)
        if not link:
            flash("Please fill the link fiels !", category="error")
        result = download_video(link)
        if not result:
            flash("Error with the link !", category="error")
        flash("Video downloaded !", category="success")
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
