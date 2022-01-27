<template>
  <nav class="navbar navbar-expand-sm navbar-light px-5">
  <!-- Brand -->
  <!-- <a class="navbar-brand" href="/">Burjiss Pavri</a> -->

  <!-- Links -->
  <div style="width: 100%;">
  <ul class="navbar-nav justify-content-center">
    <li class="nav-item">
      <a class="nav-link" href="#">Resume</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#">Projects</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#">Reach out</a>
    </li>

    <!-- Dropdown -->
    <!-- <li class="nav-item dropdown">
      <a class="nav-link dropdown-toggle" href="#" id="navbardrop" data-toggle="dropdown">
        Dropdown link
      </a>
      <div class="dropdown-menu">
        <a class="dropdown-item" href="#">Link 1</a>
        <a class="dropdown-item" href="#">Link 2</a>
        <a class="dropdown-item" href="#">Link 3</a>
      </div>
    </li> -->
  </ul>
  </div>
</nav>
</template>

<script>
export default {
  name: "NavBar",
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.navbar {
     background-image: url("../assets/menu-bg.png");
     /* max-height: 6em; */
     /* background-color: rgb(128,201,215); */
}
</style>
