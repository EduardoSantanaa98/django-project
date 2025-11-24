<template>
  <div class="container">
    <h1>Criar Conta</h1>

    <form @submit.prevent="register">
      <input v-model="email" type="email" placeholder="Email" required />
      <input v-model="password" type="password" placeholder="Senha" required />
      <button type="submit">Cadastrar</button>
    </form>

    <p>
      Já tem conta?
      <router-link to="/login">Entrar</router-link>
    </p>

    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script>
import { createUserWithEmailAndPassword, signOut } from "firebase/auth";
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
    async register() {
      try {
        await createUserWithEmailAndPassword(auth, this.email, this.password);

        
        await signOut(auth);

        
        this.$router.push("/login");
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
