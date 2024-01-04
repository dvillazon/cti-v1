<template>
    <div class="navbar">
      <div class="logo">
        <img src="../assets/uc_logo.png" alt="logo" />
        <h2>CTI</h2>
      </div>
  
      <div class="nav-menu">
        <button @click="navigateTo('mi-usuario')" class="user-button">
          <i class="fas fa-user"></i> Mi Usuario
        </button>
        <button @click="navigateTo('salir')" class="user-button">
          <i class="fas fa-sign-out-alt"></i> Salir
        </button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      navigateTo(route) {
        // Agregar la lógica para redirigir a la ruta específica
        if (route === 'mi-usuario') {
        this.$router.push('/usuario2');
      } else if (route === 'salir') {
        this.$router.push('/');
      }

      else {
        console.log(`Navegar a ${section}`);
      }
      },
    },
  };
  </script>
  
  <style scoped>
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    margin: 10px;
    height: 70px;
    background: #dedef6;
    border: 1px solid #afafc7;
    border-radius: 10px;
  }
  
  .logo {
    display: flex;
    width: 2rem;
    height: 2rem;
    margin-left: -1rem;
    margin-top: -1rem;
  }
  
  .logo img {
    width: 5rem;
    height: 3rem;
    background-size: contain;
  }
  
  h2 {
    font-size: 2rem;
  }
  
  .nav-menu {
    display: flex;
    align-items: center;
  }
  
  .user-button {
    font-size: 1.2rem;
    font-weight: 500;
    text-decoration: none;
    color: inherit;
    background-color: #dedef6;
    padding: 0.3rem 1rem;
    border-radius: 10px;
    display: flex;
    align-items: center;
    margin: 0 0.5rem;
    cursor: pointer;
    transition: background 1s;
    border: none;

  }
  
  .user-button i {
    margin-right: 0.5rem;
  }
  
  .user-button:hover {
    background: #007bff;
    color: white;
  }
  </style>
  