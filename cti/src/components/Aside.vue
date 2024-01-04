<template>
  <aside class="aside-container">
    <div class="logo">
      <img src="../assets/user.png" alt="Logo" />
    </div>
    <div class="nav">
      <button class="nav-button" @click="navigate('inicio')">
        <img src="../assets/inicio.png" alt="Inicio" class="nav-icon" />
        <span>Inicio</span>
      </button>
      <div class="divider"></div>
      <div class="user-panel">
        <button class="nav-button" @click="navigate('curriculo')">
          <img src="../assets/curriculo.png" alt="Curriculum" class="nav-icon" />
          <span>Curriculum</span>
        </button>
        <button class="nav-button" @click="toggleDropdown('publicaciones')">
          <img src="../assets/publicacion.png" alt="Publicaciones" class="nav-icon" />
          <span>Publicaciones</span>
        </button>
        <div v-if="showPublicaciones" class="dropdown">
          <button @click="navigate('articulos')">Artículos</button>
          <button @click="navigate('libros')">Libros</button>
          <button @click="navigate('monografias')">Monografías</button>
        </div>
        <button class="nav-button" @click="toggleDropdown('condecoraciones')">
          <img src="../assets/condecoracion.png" alt="Condecoraciones" class="nav-icon" />
          <span>Condecoraciones</span>
        </button>
        <div v-if="showCondecoraciones" class="dropdown">
          <button @click="navigate('premios')">Premios</button>
          <button @click="navigate('reconocimientos')">Reconocimientos</button>
        </div>
      </div>
    </div>
  </aside>
</template>

<script>
export default {
  data() {
    return {
      showPublicaciones: false,
      showCondecoraciones: false,
    };
  },
  methods: {
    navigate(section) {
      // Agregar lógica para cambiar de sección o ruta en tu aplicación
      if (section === 'curriculo') {
        this.$router.push('/curriculo');
      } else if (section === 'inicio') {
        this.$router.push('/home');
      }else if (section === 'articulos') {
        this.$router.push('/articulo');
      }else if (section === 'libros') {
        this.$router.push('/libro');
      }else if (section === 'monografias') {
        this.$router.push('/monografia');
      }else if (section === 'premios') {
        this.$router.push('/premios');
      }else if (section === 'reconocimientos') {
        this.$router.push('/reconocimiento');
      }
      else {
        console.log(`Navegar a ${section}`);
      }
    },
    toggleDropdown(dropdown) {
      if (dropdown === 'publicaciones') {
        this.showPublicaciones = !this.showPublicaciones;
        this.showCondecoraciones = false;
      } else if (dropdown === 'condecoraciones') {
        this.showCondecoraciones = !this.showCondecoraciones;
        this.showPublicaciones = false;
      }
    },
  },
};
</script>

<style scoped>
.aside-container {
  width: 100%;
  max-width: 15rem;
  height: 100vh;
  background-color: #3e5e7d;
  padding: 5% 5% 2% 5%;
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: all 1s;
  position: fixed;
}

.logo img {
  margin-top: 5%;
  max-width: 80%;
  margin-bottom: 5%;
}

.nav-button {
  background: none;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  margin: 3% 0;
  color: aliceblue;
  padding: 5%;
  font-size: 1rem;
  width: 100%;
  text-align: left;
  transition: background-color 1s;
  border-radius: 10px;
}

.nav-button:hover {
  background-color: #2a3f5f;
}

.nav-icon {
  width: 24px;
  height: 24px;
  margin-right: 10px;
}

.divider {
  height: 1px;
  background-color: white;
  width: 100%;
  margin: 5% 0;
}

.user-panel button {
  display: flex;
  align-items: center;
}

.dropdown {
  display: flex;
  flex-direction: column;
  width: 100%;
  padding-left: 5%;
}

.dropdown button {
  width: 100%;
  padding: 2% 5%;
  background: none;
  border: none;
  cursor: pointer;
  text-align: left;
  color: aliceblue;
  transition: background-color 1s;
  border-radius: 10px;
}

.dropdown button:hover {
  background-color: #2a3f5f;
}

@media (max-width: 768px) {
  .aside-container {
    max-width: 10rem;
  }
}

@media (max-width: 480px) {
  .aside-container {
    max-width: 8rem;
  }

  .nav-button {
    font-size: 0.8rem;
  }

  .dropdown button {
    padding: 2% 3%;
  }
}
</style>
