<template>
  <div class="sidebar">
    <img alt="CB logo" src="../../../../doc/logo.png" />
    <div>
      <span class="submenu"> <b>Calculadora de viagens</b></span>
    </div>
  </div>
</template>

<script>
export default {
  name: "SideBar",
  props: {},
  setup() {},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
:root {
  --sidebar-bg-color: #0f2b42;
  --sidebar-item-hover: #38a169;
  --sidebar-item-active: #276749;
}

img {
  /* height: 500px; */
  width: 150px;
  margin: 15px 15px 20px;
  /* object-fit: fill; */
}

.submenu {
  width: fit-content;
  justify-items: start;
  float: left;
  margin: 50px 5px 0;
}
</style>

<style scoped>
.sidebar {
  color: #fff;
  background-color: var(--sidebar-bg-color);

  /* float: left;
  position: relative; */
  z-index: 1;
  top: 0;
  left: 0;
  bottom: 0;
  padding: 0.5em;

  width: 250px;

  display: flex;
  flex-direction: column;
}
</style>
