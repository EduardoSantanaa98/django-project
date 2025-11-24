<template>
  <div class="container">
    <h1>Login</h1>

    <form @submit.prevent="login">
      <input v-model="email" type="email" placeholder="Email" required />
      <input v-model="password" type="password" placeholder="Senha" required />
      <button type="submit">Login</button>
    </form>

    <p>
      Não tem conta?
      <router-link to="/register">Criar conta</router-link>
    </p>

    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script>
import { signInWithEmailAndPassword } from "firebase/auth";
import { auth } from "../firebase/firebaseConfig";

export default {
  data() {
    return {
      email: "",
      password: "",
      error: ""
    };
  },
  methods: {
    async login() {
      try {
        await signInWithEmailAndPassword(auth, this.email, this.password);
        this.$router.push("/home");
      } catch (err) {
        this.error = err.message;
      }
    }
  }
};
</script>

<style>
.container {
  max-width: 400px;
  margin: auto;
  text-align: center;
}
input {
  display: block;
  margin: 10px auto;
  padding: 10px;
  width: 80%;
}
button {
  padding: 10px;
  width: 80%;
}
.error {
  color: red;
}
</style>
