import { createRouter, createWebHashHistory } from "vue-router";
import MainPageView from "../views/MainPageView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: MainPageView,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
