<template>
    <div class="distincion-list">
      <div class="header">
        <img src="../assets/con.png" alt="Icono" class="icon" />
        <h1>Distinción</h1>
      </div>
      <hr />
      <div class="distincion-list-header">
        <button  @click="navigate" class="new-distincion-button">
          
          +Nuevo
        </button>
        <div class="distincion-info">Distinción</div>
        <div class="distincion-info">Estado del la distinción</div>
        
      </div>
      <hr />
      <div class="distincion" v-for="(distincion, index) in distinciones" :key="index">
        <div class="distincion-info">{{ distincion.title }}</div>
        <div class="distincion-info">{{ distincion.status }}</div>
      </div>
    </div>
  </template>
  
  <script>
import axios from 'axios';

export default {
  props: {
    navigate: Function,
  },
  data() {
    return {
      distinciones: [],
    };
  },
  methods: {
    fetchDistinciones() {
      // Realizar una solicitud GET al backend para obtener las distinciones
      axios.get('URL_DEL_BACKEND/tuRutaDeDistinciones')
        .then(response => {
          // Asignar la respuesta de las distinciones al arreglo de distinciones
          this.distinciones = response.data;
        })
        .catch(error => {
          console.error('Error al obtener las distinciones:', error);
        });
    },
    // Resto de tus métodos
  },
  created() {
    // Llamar a fetchDistinciones al cargar el componente para obtener las distinciones
    this.fetchDistinciones();
  },
};
</script>
  
  <style scoped>
  .distincion-list {
    display: flex;
    flex-direction: column;
    width: 79rem;
    margin: 10px;
    padding: 20px;
    background-color: #f7f7f7;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
  }
  
  .header {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }
  
  .icon {
    width: 50px;
    height: 50px;
    margin-right: 10px;
  }
  
  h1 {
    font-size: 1.5rem;
    margin: 0;
  }
  
  hr {
    border: 1px solid #ddd;
    margin: 10px 0;
  }
  
  .new-distincion-button {
    display: flex;
    align-items: center;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 5px 10px;
    cursor: pointer;
    margin-top: 10px; /* Alineado con los encabezados */
  }
  
  .button-icon {
    width: 20px;
    height: 20px;
    margin-right: 5px;
  }
  
  .distincion-list-header {
    display: flex;
    justify-content: space-between;
    font-weight: 600;
    margin: 0 10px;
  }
  
  .distincion-info {
    flex: 1;
    padding: 5px;
    border:none;
    margin-top: 0.8rem;
  }
  
  .distincion {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 0 10px;
    margin-left: 6rem;
  }
  </style>
  