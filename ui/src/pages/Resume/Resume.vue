<template>
  <div id="root" class="container px-0 min-vh-100 shadow-lg">
    <NavBar class="mb-5"/>
Resume
  </div>
</template>

<script>

import NavBar from '../../components/NavBar.vue'

export default {
  name: 'Resume',
  components: {
    NavBar
  }
}
</script>

<style>
#root {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;;
  /* margin-top: 60px; */
  background-color: white;
}
</style>
