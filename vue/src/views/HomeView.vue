<script>
import { signOut } from "firebase/auth";
import { auth } from "../firebase/firebaseConfig";

export default {
  methods: {
    async logout() {           
      await signOut(auth);
      this.$router.push("/login");  
    }
  }
};
</script>

<template>
  <div class="container">
    <h1>Bem-vindo!</h1>

     <button @click="logout">Sair</button>  
  </div>
</template>