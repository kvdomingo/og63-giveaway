import axios from "axios";
import Pizzly from "pizzly-js";

const baseURL = "/api/v1.0/";

const axiosInstance = axios.create({ baseURL });

const api = {
  data: {
    giveaway() {
      return axiosInstance.get("/giveaway");
    },
    participant(data) {
      return axiosInstance.post("/participant", data);
    },
    winner() {
      return axiosInstance.get("/winner");
    },
    getDraw(data) {
      return axiosInstance.post("/draw", data);
    },
    publishDraw(data) {
      return axiosInstance.post("/publish", data);
    },
  },
};

const pizzly = new Pizzly({ host: "https://pizzly-central.herokuapp.com" });

const auth = pizzly.integration("discord");

export default api;

export { auth };
