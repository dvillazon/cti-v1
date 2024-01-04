<template>
    <div class="monografia-list">
      <div class="header">
        <img src="../assets/Articulo.png" alt="Icono" class="icon" />
        <h1>Monografías</h1>
      </div>
      <hr />
      <div class="monografia-list-header">
        <button  @click="navigate" class="new-monografia-button">
          +Nuevo
        </button>
        <div class="monografia-info">Título</div>
        <div class="monografia-info2">Estado</div>
        
      </div>
      <hr />
      <div class="monografia" v-for="(monografia, index) in monografias" :key="index">
        <div class="monografia-info">{{ monografia.titulo }}</div>
        <div class="monografia-info">{{ monografia.estado }}</div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';

  export default {
    props: {
      navigate: Function, // Prop para recibir la función de envío
  },
    data() {
      return {
        monografias: [],
      };
    },
    methods: {
      async obtenerMonografia() {
      try {
        const userData = JSON.parse(localStorage.getItem('userData'));
        const userName = userData.username;
        const getUSER = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/?nombreUsuario=${userName}`);
        const response = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/${getUSER.data[0].id}/write_monografia/`); // Reemplaza esto con tu ruta real
        this.monografias = response.data; // Suponiendo que la respuesta es un array de objetos con títulos y estados
      } catch (error) {
        console.error('Error al obtener Monografia:', error);
        // Manejo de errores
      }
    },
},

created() {
    this.obtenerMonografia(); // Llama a la función para obtener las monografias cuando se crea el componente
  },
  };
  </script>
  
  <style scoped>
  .monografia-list {
    display: flex;
    flex-direction: column;
    width: 68rem;
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
    width: 40px;
    height: 40px;
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
  
  .new-monografia-button {
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
  
  .monografia-list-header {
    display: flex;
    justify-content: space-between;
    font-weight: 600;
    margin: 0 10px;
  }
  
  .monografia-info {
    display: flex;
    padding: 5px;
    border:none;
    margin-top: 0.8rem;
    justify-content: space-between;
  }
  .monografia-info2 {
    margin-left: 54rem;
    padding: 5px;
    border:none;
    margin-top: 0.8rem;
  }
  .monografia {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 0 10px;
    margin-left: 6rem;
  }
  </style>
  