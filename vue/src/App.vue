<template>
  <div>
    <nav style="padding: 20px; background: #eee;">
      <router-link to="/">Home</router-link> |
      <router-link to="/login">Login</router-link> |
      <router-link to="/register">Cadastro</router-link>
    </nav>

    <router-view />
  </div>
</template>

<script>
export default {};
</script>

<style>
nav a {
  margin: 0 10px;
  text-decoration: none;
  font-weight: bold;
}
</style>

