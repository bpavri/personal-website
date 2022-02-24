<template>
  <div class="quick-links">
    <h1 class="mb-4">{{ msg }}</h1>
    <h5 class="mb-5">
      Burjiss is a Senior Software Engineer out of Seattle, Washington<br>
    </h5>
    <!-- For some spacing -->
    <div class="mt-5 mb-5" style="color: white;"><p>.</p></div>

    <div class="container mt-5 mb-3">
      <div class="row">
        <div class="col"><img class="img-fluid" width="70em" src="../assets/python.svg" /></div>
        <div class="col"><img class="img-fluid" width="85em" src="../assets/flask.png" /></div>
        <div class="col"><img class="img-fluid" width="90em" src="../assets/php.png" /></div>
        <div class="col"><img class="img-fluid" width="90em" src="../assets/laravel.png" /></div>
        <div class="col"><img class="img-fluid" width="90em" src="../assets/drupal.png" /></div>  
      </div>

  <div class="row mt-4">
        <div class="col"><img class="img-fluid" width="80em" src="../assets/docker.png" /></div>
        <div class="col"><img class="img-fluid" width="85em" src="../assets/kubernetes.png" /></div>
        <div class="col"><img class="img-fluid" width="80em" src="../assets/vuejs.png" /></div>
        <div class="col"><img class="img-fluid" width="100em" src="../assets/salesforce.png" /></div>
      </div>

    </div>
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
<style>
.quick-links h3 {
  margin: 40px 0 0;
}
.quick-links ul {
  list-style-type: none;
  padding: 0;
}
.quick-links li {
  display: inline-block;
  margin: 0 10px;
}
.quick-links a {
  color: #42b983;
}
</style>
