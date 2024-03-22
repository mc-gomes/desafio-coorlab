<template>
  <div class="geral">
    <Sidebar />
    <router-view class="page" />
  </div>
</template>

<script>
import Sidebar from "@/components/Sidebar.vue";

export default {
  components: { Sidebar },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.geral {
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  position: fixed;
  display: flex;
  justify-items: center;
  flex-direction: row;
}

.page {
  width: 100%;
  justify-content: space-around;
  /* padding: 10px; */
  /* height: 100%; */
  /* margin: 0; */
  /* top: 0; */
  /* left: 0; */
}
</style>
