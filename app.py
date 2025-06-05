from flask import Flask, request, jsonify, send_file
import subprocess, os, requests

app = Flask(__name__)

@app.route("/upload-url", methods=["POST"])
def upload_url():
    try:
        data = request.get_json(force=True)
        video_url = data.get("url")
        if not video_url:
            return jsonify({"error": "Missing URL"}), 400

        response = requests.get(video_url)
        if response.status_code != 200:
            return jsonify({"error": "Failed to download video"}), 400

        with open("video.mp4", "wb") as f:
            f.write(response.content)

        # Dummy video edit
        subprocess.run(["ffmpeg", "-i", "video.mp4", "-t", "00:00:05", "final.mp4"])

        return jsonify({"status": "ok", "download_url": request.url_root + "download"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/download", methods=["GET"])
def download():
    return send_file("final.mp4", as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
