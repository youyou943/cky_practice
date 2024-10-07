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

<style scoped>
.video-player {
  margin-top: 20px;
}
</style>
