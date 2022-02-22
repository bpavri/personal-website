<template>
  <div id="root" class="container px-0 min-vh-100 shadow-lg">
    <NavBar class="mb-5"/>
    <img class="rounded-circle img-fluid" style="max-width: 15em" alt="Portrait" src="../../assets/portrait.png">
    <QuickLinks msg="Welcome to Burjiss' website!" class="mt-5"/>
  </div>
</template>

<script>
import QuickLinks from '../../components/QuickLinks.vue'
import NavBar from '../../components/NavBar.vue'

export default {
  name: 'App',
  components: {
    QuickLinks,
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
  color: #2c3e50;
  /* margin-top: 60px; */
  background-color: white;
}
</style>
