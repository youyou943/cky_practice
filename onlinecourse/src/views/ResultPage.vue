<template>
  <div class="result-container">
    <h2>搜索结果: "{{ searchQuery }}"</h2>

    <div v-if="errorMessage" class="error-message">
      <p>{{ errorMessage }}</p>
    </div>

    <div v-else-if="videoResults.length">
      <h3>找到的结果：</h3>
      <ul>
        <li v-for="video in videoResults" :key="video.videoId" @click="playVideo(video.videoId)">
          {{ video.title }}
        </li>
      </ul>
    </div>

    <div v-if="youtubeUrl" class="video-container">
      <iframe
        width="560"
        height="315"
        :src="youtubeUrl"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
      ></iframe>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      searchQuery: this.$route.query.q, // 从路由获取搜索查询
      videoResults: [],
      youtubeUrl: '',
      errorMessage: '',
    };
  },
  mounted() {
    this.fetchSearchResults();
  },
  methods: {
    async fetchSearchResults() {
      if (this.searchQuery) {
        try {
            const response = await axios.get(`http://127.0.0.1:5000/api/search?q=${encodeURIComponent(this.searchQuery)}`);
            console.log("API Response:", response.data); // 添加这一行以调试
          this.videoResults = response.data;
          this.errorMessage = '';
        } catch (error) {
          this.errorMessage = '搜索失败，请重试';
        }
      }
    },
    playVideo(videoId) {
      this.youtubeUrl = `https://www.youtube.com/embed/${videoId}`;
    }
  },
};
</script>

<style scoped>
.result-container {
  text-align: center;
  margin-top: 20px;
}

.error-message {
  color: red;
  font-size: 18px;
  margin-top: 20px;
}

.video-container {
  margin-top: 20px;
}
</style>
