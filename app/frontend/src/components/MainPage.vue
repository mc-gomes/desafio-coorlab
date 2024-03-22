<template>
  <div class="page-header"></div>
  <div class="card">
    <div class="card-header"> 
      <h3 class="title"><b>Calculadora de Viagem</b></h3>
    </div>
    <div class="card-content">
      <div class="form">
        card
        <!-- adicionar um botão aqui -->
      </div>
      <img alt="Vue logo" src="../assets/logo.png" />
    </div>
  </div>

</template>

<script>
export default {
  name: "MainPage",
  props: { },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.page-header {
  height: 50px;
  overflow: hidden;
  background-color: #f1f1f1;
  padding: 20px 10px;
  box-shadow: 0 4px 6px 0 rgba(0, 0, 0, 0.2);
  top: 0;
  position: relative;
}
.card {
  padding: 20px;
  /* justify-items: end; */
  /* transition: 0.3s; */
}

.card-header {
  height: 50px;
  overflow: hidden;
  background-color: #0f2b42;
  color: #f1f1f1;
  /* padding: 20px 10px; */
  /* width: 50%; */
  align-content: flex-start;
  top: 0;
  /* margin-left: 15px; */
  margin-top: 50px;
  position: relative;
  border-radius: 4px 4px 0 0;
}
.card-header title {
  float:left;
  justify-content: start;
}
.card-content {
  width: auto;
  /* margin-top: 50px; */
  justify-self: center;
  box-shadow: 0 5px 15px 5px rgba(0, 0, 0, 0.2);
  border-radius: 4px;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}

.form {
  padding: 5px;
  float: left;
  display: flex;
  flex-direction: column;
}

.title {
  float: left;
  padding-left: 5px;
  margin: 15px 10px 5px;
}
</style>
