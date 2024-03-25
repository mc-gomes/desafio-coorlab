<template>
  <div class="page-header"></div>
  <div class="card">
    <div class="card-header">
      <h3 class="card-header-title"><b>Calculadora de Viagem</b></h3>
    </div>
    <div class="card-content">
      <div class="card-input-output">
        <div class="card-inputs">
          <h2 class="card-inputs-title">Calcule o valor da viagem</h2>
          <label for="destino">Destino</label>
          <select id="destino" class="fields" name="destino" v-model="selectedCity" placeholder="Selecione o destino"
            @change="changedCity">
            <option v-for="city in citiesList" :key="city.id" :value="city">
              {{ city }}
            </option>
          </select>
          <label for="data">Data</label>
          <input type="date" class="fields" id="data" name="data" placeholder="Selecione uma data" />
          <button type="submit" class="search-btn" v-on:click="searchDestination">
            Buscar
          </button>
        </div>

        <div class="card-output">
          <Destination v-if="selectedCity && botaoClick" :destinations="destinationsByCity" />
          <Destination v-else-if="currentCity" :destinations="destinationsByCity" />
          <div v-else>Nenhum dado encontrado.</div>
          <div
            class="clear"
            v-if="currentCity"
            v-on:click="clear"
          >
            <button class="clear-btn">Limpar</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Api from "@/services/api";
import Destination from "@/components/Destination.vue";
import { ref } from "vue";

const api = new Api();
const citiesList = api.getCitiesList("cities");

let destinationsByCity = ref(Array);

export default {
  name: "MainPage",
  components: { Destination },
  setup() {
    return {
      citiesList,
      destinationsByCity,
    };
  },
  data() {
    return {
      selectedCity: "",
      currentCity: "",
      isCitySelected: false,
      isDateSelected: false,
      botaoClick: false,
      destinations: [],
    };
  },
  methods: {
    cityIndex(city, list) {
      for (const c of list) {
        if (c === city) {
          return list.indexOf(c);
        }
      }
      return undefined;
    },
    searchDestination() {
      this.botaoClick = true;
      this.currentCity = this.selectedCity;
      const cityId = this.cityIndex(this.selectedCity, this.citiesList);
      this.destinationsByCity = api.getDestinationByCity(cityId);
    },
    changedCity() {
      this.isCitySelected = true;
      this.botaoClick = false;
    },
    clear() {
      this.selectedCity = "",
      this.currentCity = "",
      this.botaoClick = false
    }
  },
};
</script>

<style>
.page-header {
  height: 25px;
  overflow: hidden;
  background-color: #f1f1f1;
  padding: 20px 10px;
  box-shadow: 0 4px 6px 0 rgba(0, 0, 0, 0.2);
  top: 0;
}

.card {
  padding: 20px;
}
.card-header {
  height: 50px;
  overflow: hidden;
  background-color: #0f2b42;
  color: #f1f1f1;
  align-content: flex-start;
  top: 0;
  margin-top: 50px;
  position: relative;
  border-radius: 4px 4px 0 0;
}
.card-header-title {
  float: left;
  justify-content: start;
  padding-left: 5px;
  margin: 15px 10px 5px;
}
.card-content {
  justify-content: space-between;
}
.card-input-output {
  width: 100%;
  margin-bottom: 20px;
  box-shadow: 0 5px 15px 5px rgba(0, 0, 0, 0.2);
  border-radius: 4px;
  display: flex;
  flex-direction: row;
  justify-items: start;
}

.card-inputs {
  width: 300px;
  height: 400px;
  margin: 50px;
  padding: 20px;
  background-color: #cbcdcf;
  border-radius: 5px;
  justify-content: start;
}
.card-inputs-title {
  text-align: center;
  font-size: 24px;
  margin-bottom: 40px;
  margin-top: 30px;
}

.card-output {
  margin-bottom: 20px;
  margin-left: 50px;
  padding: 50px;
  display: grid;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

label {
  display: block;
  margin-bottom: 5px;
  text-align: left;
}

select,
input[type="date"] {
  width: calc(100% - 20px);
  padding: 8px;
  margin-bottom: 50px;
  border: 1px solid #ccc;
  border-radius: 3px;
}

.fields {
  align-items: start;
}

.search-btn {
  width: 50%;
  padding: 10px;
  bottom: 0;
  color: #222121;
  background-color: #0f557e;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}
.search-btn:hover {
  background-color: #0056b3;
}

.clear {
  justify-self: end;
  position: relative;
  padding-right: 20px;
}

.clear-btn {
  width: 150px;
  padding: 10px 0;
  background-color: #e9b91c;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}
</style>
