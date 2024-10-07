iCoursera

主要内容：计算机在线学习平台，调用YouTube API实现跨平台视频观看

主要技术思路：前端   vue框架，webpack脚手架，element plus组件   （onlinecourse）

后端 python flask框架 (FlaskBack )

API调用YouTube ：
https://console.cloud.google.com/apis/credentials?project=onlinecourse-437805
获取apI密钥
主要界面 ：
1.首页  
功能：主要是推荐相关课程，有考虑过通过用户的观看需求个性化推荐但目前还在研发阶段，放的是静态ID

交互：点击立即报名，可以跳转到播放页面

2.课程界面
主要由搜索框和推荐列表组成
点击搜索框可以通过关键词搜索跳转到相关界面，点击下面卡片中的立刻观看也可以跳转到相关的视频界面





前端关键部分代码：
VideoPlayer.vue
<template>
  <div class="video-player">
    <iframe
      width="80%"
      height="700"
      :src="videoSrc"
      frameborder="0"
      allowfullscreen
    ></iframe>
  </div>
</template>

<script>
export default {
  props: {
    videoId: {
      type: String,
      required: true
    }
  },
  computed: {
    videoSrc() {
      return `https://www.youtube.com/embed/${this.videoId}`; 
      //return `https://www.youtube.com/embed?listType=search&list=前端`;      
    }
  }
};
</script>
这是我每个播放视频界面内嵌的视频播放组件，主要是通过调用视频的ID来实现调用youtube上面的视频的

后端关键代码：
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
 主要是两个思路一个是调用videoId直接显示视频，还有一个是通过关键词搜索 https://developers.google.com/youtube/player_parameters?hl=zh-cn#Parameters



开发阶段用到的工具分享（个人觉得很有用）
radiovisual/get-video-id：从 url 或嵌入字符串中获取 YouTube、Vimeo、Vine、VideoPress、TikTok、Microsoft Stream、Loom 或 Dailymotion 视频 ID。 (github.com)
项目简介
get-video-id是一个简洁高效且开源的JavaScript库，旨在帮助开发者和用户快速识别并提取来自YouTube、Vimeo、Vine、VideoPress、TikTok、Microsoft Stream及Dailymotion等平台视频的唯一ID。无论是进行数据分析、内容聚合还是简单的分享功能开发，这个小工具都是你的得力助手。

项目技术分析
get-video-id通过灵活的模式匹配算法，能够解析上述各平台的多种URL格式，包括直接链接、嵌入代码、短链接乃至通过Google重定向的复杂链接。该库支持Node.js环境以及现代浏览器，提供 CommonJS 和 ES2015 模块导入方式，甚至可直接通过CDN引入到网页中，方便快捷。它的API设计极为直观，只需传入视频链接或嵌入代码，即可返回一个包含视频ID和服务名称的对象。

项目及技术应用场景
在实际应用中，get-video-id几乎是多场景的万金油。对于社交媒体分析者，它可以帮助自动整理和分类跨平台的视频数据；对开发者而言，构建视频集锦、实现视频分享按钮、或是优化第三方视频加载逻辑都离不开它。比如，在制作一个多平台视频播放列表时，仅需调用一次该库，就能无缝整合不同来源的视频内容。

本系统的用法：我初步的想法是利用这个在搜索阶段直接找出视频的id

本次作业的瓶颈：
由于第一次初步尝试web开发，对本人来说是个考验，由于学习能力问题，做出来的成果不太尽如人意，但是确实是有把前端框架学习了，并且对本次项目进行独立思考了的。
1.就是关于视频的来源我认为是最大的难点，我的疑问是是否要搞一个用户提交视频的功能呢？？因为我的视频来源都是通过调用YouTube的，运行环境肯定是有要求的，而且调用难度还是很大的。如果搞提交视频的功能就可以参考哔哩哔哩但是需要一个强大的云服务器吧
2.关于搜索功能的代码，在运行过程中发现    "error": "[WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。"  
我尝试用
curl "https://www.googleapis.com/youtube/v3/search?part=snippet&q=前端&type=video&key=YOUR_API_KEY"
使用 curl 测试 API，但是结果是
curl: (28) Failed to connect to www.googleapis.com port 443 after 84312 ms: Couldn't connect to server
我想的是是不是因为我的代理不太稳定导致不太能实现呢，所以我就想直接通过工具找出ID，因为调用ID是可以实现的。


这是我用浏览器搜索https://www.googleapis.com/youtube/v3/search?part=snippet&q=前端&type=video&key=YOUR_API_KEY 得到的结果，发现就是每个视频的相关信息，所以我想借助get-video-id直接找出每个信息的ID，但是由于开发时间限制目前还在初步探索阶段。