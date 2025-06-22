from flask import Flask, render_template, request, send_file
import os
import subprocess
import uuid

app = Flask(__name__)
os.makedirs("downloads", exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        start = request.form["start"]
        end = request.form["end"]

        video_id = str(uuid.uuid4())
        raw_video = f"downloads/{video_id}_raw.mp4"
        clipped_video = f"downloads/{video_id}_clip.mp4"

        subprocess.run([
            "yt-dlp", "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
            "-o", raw_video, url
        ])

        subprocess.run([
    "ffmpeg", "-y", "-i", raw_video,
    "-ss", start, "-to", end,
    "-c:v", "libx264", "-preset", "ultrafast",
    "-c:a", "aac", "-b:a", "128k",
    clipped_video
])


        os.remove(raw_video)
        return send_file(clipped_video, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
