<template>
  <div class="quick-links">
    <h1>{{ msg }}</h1>
    <p>
      Burjiss is a Senior Software Engineer out of Seattle, Washington<br>
    </p>
    <!-- <h3>Quick Links</h3>
    <ul>
      <li><a href="/resume" target="_blank" rel="noopener">Resume</a></li>
      <li><a href="/projects" target="_blank" rel="noopener">Projects</a></li>
    </ul> -->

    <img src="../assets/seattle.jpg" style="position: relative;
    left: 0;
    width: 100%;
    bottom: -8em;
    height: auto" loading="lazy" />
  </div>
</template>

<script>

export default {
  name: 'QuickLinks', 
  props: {
  msg: String
}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
