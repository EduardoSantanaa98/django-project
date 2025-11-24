import { createRouter, createWebHistory } from "vue-router";
import LoginView from "../views/LoginView.vue";
import RegisterView from "../views/RegisterView.vue";
import HomeView from "../views/HomeView.vue";

import { auth } from "../firebase/firebaseConfig";
import { onAuthStateChanged } from "firebase/auth";

const routes = [
  { path: "/", redirect: "/login" },

  {
    path: "/login",
    name: "login",
    component: LoginView,
    meta: { requiresGuest: true }
  },

  {
    path: "/register",
    name: "register",
    component: RegisterView,
    meta: { requiresGuest: true }
  },

  {
    path: "/home",
    name: "home",
    component: HomeView,
    meta: { requiresAuth: true }
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// proteção de rotas - firebase
let authReady = false;
onAuthStateChanged(auth, () => {
  authReady = true;
});

router.beforeEach((to, from, next) => {
  if (!authReady) {
    const stopWatch = setInterval(() => {
      if (authReady) {
        clearInterval(stopWatch);
        next(to);
      }
    }, 50);
    return;
  }

  const user = auth.currentUser;

  if (to.meta.requiresAuth && !user) return next("/login");
  if (to.meta.requiresGuest && user) return next("/home");

  next();
});

export default router;
