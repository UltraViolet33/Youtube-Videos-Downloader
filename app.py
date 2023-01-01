from flask import Flask, render_template, request, flash, redirect
from download_video import download_video, delete_mp4_audio_files

app = Flask(__name__)
app.config["SECRET_KEY"] = "hello"


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        link = request.form.get("link")
        file_type = request.form.get("file_type")
        if not link or not file_type:
            flash("Please fill all fields !", category="error")
            return redirect("/")

        result = download_video(link, file_type)
        if not result:
            flash("Error with the link !", category="error")
            return redirect("/")

        flash("Video downloaded !", category="success")
        return redirect("/")
    return render_template('index.html')


@app.route('/delete-mp4', methods=["POST"])
def method_name():
    delete_mp4_audio_files()
    flash("OK", category="success")
    return redirect("/")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
