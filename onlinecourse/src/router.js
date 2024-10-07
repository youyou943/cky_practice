import { createRouter, createWebHistory } from 'vue-router';
import Home from './Home.vue'; // 主页
import Courses from './views/Courses.vue'; // 课程页面
import About from './views/About.vue'; // 关于页面
import VideoPage from './views/VideoPage.vue';
import ResultPage from '@/views/ResultPage.vue';  // 显示搜索结果页面
const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
        path: '/courses',
        name: 'Courses',
        component: Courses,
    },
    {
        path: '/about',
        name: 'About',
        component: About,
    },
    {
        path: '/video/:videoId', // 使用路由参数
        name: 'VideoPage',
        component: VideoPage,
    },
    {
        path: '/results',
        name: 'ResultPage',
        component: ResultPage,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
