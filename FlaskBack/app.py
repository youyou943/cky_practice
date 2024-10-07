

import requests
from flask import Flask, jsonify, request
from flask_cors import CORS  # 导入 CORS
from googleapiclient.discovery import build
import os

app = Flask(__name__)
CORS(app)  # 启用 CORS

YOUTUBE_API_KEY = 'AIzaSyArnxFmtqMeGiLKt_1WZ_YuVr1sYsaGG8o'
YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'


@app.route('/api/youtube', methods=['GET'])
def get_youtube_info():
    video_id = request.args.get('videoId')
    playlist_id = request.args.get('list')
    index = request.args.get('index')

    # 示例数据，您需要根据实际情况获取视频信息
    video_info = {
        "videoId": video_id,
        "title": "前端开发基础",  # 这里填入实际视频标题
        "description": "学习 HTML、CSS 和 JavaScript"  # 这里填入实际视频描述
    }

    return jsonify(video_info)  # 返回包含视频信息的 JSON 对象


@app.route('/api/search', methods=['GET'])
def search_video():
    query = request.args.get('q')
    if not query:
        return jsonify({'error': 'No query provided'}), 400

    try:
        youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
        search_response = youtube.search().list(
            q=query,
            type='video',
            part='id,snippet',
            maxResults=10
        ).execute()

        video_results = []
        for item in search_response.get('items', []):
            video_results.append({
                'videoId': item['id']['videoId'],
                'title': item['snippet']['title']
            })

        return jsonify(video_results)
    except Exception as e:
        print(f"Error occurred: {str(e)}")  # 打印完整错误
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
