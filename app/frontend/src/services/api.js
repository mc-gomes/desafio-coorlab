import api from "@/axios/axios";
import { ref } from "vue";

export default class Api {
    constructor() { }

    getCitiesList() {
        const resposta = ref(Array);
        api
            .get("cities")
            .then((response) => {
                resposta.value = response.data;
            })
            .catch((error) => {
                console.log(error);
            });

        return resposta;
    }

    getDestinationByCity(endpoint){
        const resposta = ref(Array);
        api
            .get(`cities/${endpoint}`)
            .then((response) => {
                resposta.value = response.data;
            })
            .catch((error) => {
                console.log(error);
            });

        return resposta;
    }
}
