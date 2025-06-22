

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