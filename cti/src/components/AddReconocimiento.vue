<template>
    <div class="reconocimiento-list">
      <div class="header">
        <img src="../assets/con.png" alt="Icono" class="icon" />
        <h1>Reconocimiento</h1>
      </div>
      <hr />
      <div class="reconocimiento-list-header">
        <button  @click="navigate" class="new-reconocimiento-button">
          
          +Nuevo
        </button>
        <div class="reconocimiento-info">Título</div>
        <div class="reconocimiento-info2">Estado</div>
        
      </div>
      <hr />
      <div class="reconocimiento" v-for="(reconocimiento, index) in reconocimientos" :key="index">
        <div class="reconocimiento-info">{{ reconocimiento.nombre_reconocimiento }}</div>
        <div class="reconocimiento-info">{{ reconocimiento.estado }}</div>
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
        reconocimientos: [],
      };
    },
    mounted() {
    this.obtenerReconocimiento();
  },
  methods: {
      async obtenerReconocimiento() {
      try {
        const userData = JSON.parse(localStorage.getItem('userData'));
        const userName = userData.username;
        const getUSER = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/?nombreUsuario=${userName}`);
        const response = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/${getUSER.data[0].id}/write_reconocimiento/`); // Reemplaza esto con tu ruta real
        this.reconocimientos = response.data; // Suponiendo que la respuesta es un array de objetos con títulos y estados
      } catch (error) {
        console.error('Error al obtener libros:', error);
        // Manejo de errores
      }
    },
},

created() {
    this.obtenerReconocimiento(); // Llama a la función para obtener los libros cuando se crea el componente
  },
  };
  </script>
  
  <style scoped>
  .reconocimiento-list {
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
  
  .new-reconocimiento-button {
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
  
  .reconocimiento-list-header {
    display: flex;
    justify-content: space-between;
    font-weight: 600;
    margin: 0 10px;
  }
  
  .reconocimiento-info {
    display: flex;
    padding: 5px;
    border:none;
    margin-top: 0.8rem;
    justify-content: space-between;
  }
  .reconocimiento-info2 {
    margin-left: 54rem;
    padding: 5px;
    border:none;
    margin-top: 0.8rem;
  }
  .reconocimiento {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 0 10px;
    margin-left: 6rem;
  }
  </style>
  