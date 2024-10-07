<template>
  <el-header>
    <div class="navbar">
      <el-menu
        :default-active="activeMenu"
        class="el-menu"
        mode="horizontal" 
        @select="handleSelect"
      >
        <el-menu-item index="/">
          <router-link to="/">在线学习平台</router-link>
        </el-menu-item>
        <el-menu-item index="/courses">
          <router-link to="/courses">课程</router-link>
        </el-menu-item>
        <el-menu-item index="/about">
          <router-link to="/about">关于我们</router-link>
        </el-menu-item>
      </el-menu>
    </div>
  </el-header>
</template>

<script>
export default {
  name: "NavBarComponent", // 修改为多词名称
  data() {
    return {
      activeMenu: this.$route.path
    };
  },
  methods: {
    handleSelect(index) {
      this.$router.push(index);
    }
  },
  watch: {
    '$route'(to) {
      this.activeMenu = to.path;
    }
  }
};
</script>


<style scoped>
.navbar {
  display: flex;
  justify-content: center; /* 中心对齐 */
}

.el-menu {
  width: 100%; /* 使菜单宽度占满父容器 */
}
</style>

