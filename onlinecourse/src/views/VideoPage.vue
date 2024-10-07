<template>
  <div class="video-page">
    <el-container>
      <el-header>
        <h1>{{ video.title }}</h1>
        <p>{{ video.description }}</p>
      </el-header>
      <el-main>
        <VideoPlayer v-if="videoId" :video-id="videoId" />
        <p v-if="loading">加载视频中...</p>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import axios from 'axios'; // 确保 axios 用于 API 请求
import VideoPlayer from '../components/VideoPlayer.vue'; // 引入 VideoPlayer 组件

export default {
  name: "VideoPage",
  components: {
    VideoPlayer
  },
  data() {
    return {
      videoId: null, // 视频 ID
      video: {
        title: "",
        description: ""
      }, // 视频的详细信息
      loading: false // 用于展示加载状态
    };
  },
  created() {
    this.videoId = this.$route.params.videoId; // 从路由参数中获取 videoId
    this.getVideoDetails(); // 根据 videoId 获取视频详细信息
  },
  methods: {
   getVideoDetails() {
  this.loading = true;
  axios
    .get(`http://127.0.0.1:5000/api/youtube?videoId=${this.videoId}`)
    .then((response) => {
      // 直接从响应中获取视频数据，假设后端返回的是一个对象
      const videoData = response.data;
        console.log(videoData);
      // 直接检查 videoId 是否匹配
      if (videoData.videoId === this.videoId) {
        this.video.title = videoData.title; // 获取视频标题
        this.video.description = videoData.description; // 获取视频描述
      } else {
        console.error("视频 ID 不匹配");
      }

      this.loading = false; // 关闭加载状态
    })
    .catch((error) => {
      console.error("获取视频信息失败:", error); // 记录错误
      this.loading = false; // 关闭加载状态
    });
}

  }
};
</script>

<style scoped>
.video-page {
  padding: 20px;
}

.video-page .el-header {
  padding: 10px;
  background-color: #f5f5f5;
}

.video-page h1 {
  margin-bottom: 10px;
}

.video-page p {
  margin-bottom: 20px;
}
</style>
