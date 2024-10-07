<template>
  <div class="courses">
    <el-container>
      <el-header>
        <h1>课程列表</h1>
        
      </el-header>
      <el-main>
       <el-row :gutter="20" type="flex" justify="center" align="middle">
    <el-col :span="8">
      <el-input v-model="searchQuery" placeholder="输入搜索关键词"></el-input>
    </el-col>
    <el-col :span="4">
      <el-button type="primary" @click="searchVideos">搜索视频</el-button>
    </el-col>
  </el-row>
        
        <el-row :gutter="30">
          <el-col v-for="course in courses" :key="course.id" :span="6">
            <el-card :body-style="{ padding: '20px' }">
              <h3>{{ course.title }}</h3>
              <p>{{ course.description }}</p>
              <el-button type="primary" @click="playVideo(course.videoId)">观看视频</el-button>
            </el-card>
          </el-col>
        </el-row>
        <VideoPlayer v-if="selectedVideoId" :video-id="selectedVideoId" />
      </el-main>
    </el-container>
  </div>
</template>

<script>
import VideoPlayer from '../components/VideoPlayer.vue'; // 确保正确导入组件

export default {
  name: "CoursesPage", // 修改为多词名称
  components: {
    VideoPlayer // 注册 VideoPlayer 组件
  },
  data() {
    return {
      courses: [
    { id: 1, title: "前端开发基础", description: "学习 HTML、CSS 和 JavaScript", videoId: 'imn7EhGgFqk' },
    { id: 2, title: "Python 数据科学", description: "使用 Python 进行数据分析和可视化", videoId: 'pchico-F7ks' },
    { id: 3, title: "数据结构与算法", description: "理解计算机科学的基础，学习常见的数据结构和算法", videoId: 'hkwi2rQlPak' },
    { id: 4, title: "操作系统原理", description: "探索操作系统的基本概念和功能", videoId: 'ldIqNkEk8h' },
    { id: 5, title: "Web 开发基础", description: "学习构建和设计现代网页的基本技能", videoId: 'OavHD-ni8Bg' },
    { id: 6, title: "数据库管理系统", description: "学习关系型数据库和非关系型数据库的基础", videoId: '-Xu52PHdRfE' },
    { id: 7, title: "机器学习入门", description: "探索机器学习的基础知识和应用", videoId: 'pyU1tjeSGWA' },
    { id: 8, title: "移动应用开发", description: "学习如何为 Android 和 iOS 平台开发移动应用程序", videoId: 'iINAQ2mw08k' },
    { id: 9, title: "网络安全基础", description: "了解网络安全的基本概念", videoId: 'vurmqPYi07s' },
    { id: 10, title: "云计算概论", description: "学习云计算的基本概念和服务模型", videoId: 'j1WKSvd0Je8' },
    { id: 11, title: "人工智能概论", description: "了解人工智能的基本原理和应用", videoId: '71xQxktmm9U' },
    { id: 12, title: "软件工程实践", description: "学习软件开发生命周期和项目管理", videoId: 'XcyxdWIPIeg' },
    // 其他课程
],
      searchQuery: '',
      selectedVideoId: null // 用于存储选中的视频 ID
    };
  },
  methods: {
    playVideo(videoId) {
      console.log(videoId);
    this.$router.push({ name: 'VideoPage', params: { videoId } }); // 确保使用正确的路由名称
    },
    searchVideos(){

      if (this.searchQuery) {
        // 跳转到结果页面并传递搜索关键词
        this.$router.push({ 
          path: '/results', 
          query: { q: this.searchQuery } 
        });
      }
    },

  },
};
</script>

<style scoped>
.courses {
  padding: 20px;
}
</style>
