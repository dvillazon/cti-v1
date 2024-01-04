<template>
  <div class="article-list">
    <div class="header">
      <img src="../assets/articulo.png" alt="Icono" class="icon" />
      <h1>Artículos</h1>
    </div>
    
    <hr />
    <div class="article-list-header">
      <button @click="navigate" class="new-article-button">
        + Nuevo
      </button>
      <div class="article-info">Título</div>
      <div class="article-info2">Estado</div>
    </div>
    <hr />
    <div class="article" v-for="(article, index) in articles" :key="index">
      <div class="article-info3">{{ article.titulo }}</div>
      <div class="article-info">{{ article.estado }}</div>
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
      articles: [],
    };
  },

  methods: {
    async obtenerArticulosUsuario() {
      try {
        const userData = JSON.parse(localStorage.getItem('userData'));
        const userName = userData.username;
        // Lógica para obtener los artículos del usuario desde el backend
        const getUSER = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/?nombreUsuario=${userName}`);
        const respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/${getUSER.data[0].id}/write_articulo/`);
        this.articles = respuesta.data;
      } catch (error) {
        console.error('Error al obtener los artículos del usuario', error);
      }
    },
    
  },
  mounted() {
    this.obtenerArticulosUsuario();
  },
};
</script>

<style scoped>
  .article-list {
    display: flex;
    flex-direction: column;
    width: 69rem;
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
    width: 30px;
    height: 30px;
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
  
  .new-article-button {
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
  
  .article-list-header {
  
    display: flex;
    font-weight: 600;
   
  }
  
  .article-info {
    display: flex;
    padding: 5px;
    border:none;
    margin-top: 0.8rem;
    justify-content: space-between;
    
  }
  .article-info2 {
    margin-left: 54rem;
    padding: 5px;
    border:none;
    margin-top: 0.8rem;
  }
  .article-info3 {
    margin-left: -2rem;
    padding: 5px;
    border:none;
    margin-top: 0.8rem;
    
    
  }
  
  .article {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 0 10px;
    margin-left: 6rem;
  }
  </style>


