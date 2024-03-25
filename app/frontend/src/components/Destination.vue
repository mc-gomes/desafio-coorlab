<template>
  <div id="results">
    <h3>Estas são as melhores alternativas de viagem</h3>
    <div class="grid-container">
      <div v-for="(resultado, index) in destinations" :key="index" class="grid-item">
        <div class="info">
          <p>
            <strong style="font-size: 20px;">{{ resultado.name }}</strong><br>
            Leito: {{ resultado.bed }}<br>
            Tempo estimado: {{ resultado.duration }}
          </p>
        </div>
        <div class="price">
          <p>
            <strong style="font-size: 20px;">Preço</strong><br>
            {{ resultado.price_confort }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Destination",
  props: {
    destinations: Array,
  },
};
</script>

<style>
#results {
  margin: 0 auto;
  padding: 20px;

}

h3 {
  font-size: 18px;
  margin-bottom: 20px;
  text-align: left;
}

.grid-container {
  display: grid;
  grid-template-rows: 1fr 1fr;
  gap: 15px;
}

.grid-item {
  display: flex;
  gap: 10px;
}

.info {
  flex-grow: 1;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 8px;
  text-align: left;
  background-color: #dbd7d7;
  width: 300px;
}

.price {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 8px;
  text-align: left;
  background-color: #dbd7d7;
  width: 150px;
}

</style>
