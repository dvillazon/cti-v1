
<template>
  <div class="user-data">
    <div class="header">
      <img src="../assets/lista.png" alt="Logo" />
      <h1>Lista de Publicaciones y Condecoraciones</h1>
    </div>
    <div class="filter-box">   
    <div class="filter">
        <label>Filtrar por Publicaciones:</label>
        <select v-model="selectedCategoryArticulos" @change="selectCategoryArticulos">
          <option value="all">Todo</option>
          <option value="articulo">Artículos</option>
          <option value="libro">Libros</option>
          <option value="monografia">Monografías</option>
        </select>
      </div>
      <div class="filter">
        <label>Filtrar por Condecoraciones:</label>
        <select v-model="selectedCategoryCondecoraciones" @change="selectCategoryCondecoraciones">
          <option value="all">Todo</option>
          <option value="premio">Premios</option>
          <option value="reconocimiento">Reconocimientos</option>
        </select>
      </div>
    </div>

    <div class="publicaciones">
        <div class="publicacion-usuario">

          <div class="publicacion-nombre">Título</div>
        <div class="publicacion-tipo">Estado</div>
        </div>
        
      
    </div>

    <div class="publicaciones">
      <router-link
        v-for="articulo in filteredArticulos"
        :key="articulo.id"
        :to="{ path: getCategoryPath('articulo', articulo.id) }"
        class="publicacion-usuario"
      >
        <div class="publicacion-nombre">{{ articulo.titulo }}</div>
        <div class="publicacion-tipo">{{ articulo.estado }}</div>
      </router-link>
    </div>
    <div class="publicaciones">
      <router-link
        v-for="libro in filteredLibros"
        :key="libro.id"
        :to="{ path: getCategoryPath('libro', libro.id) }"
        class="publicacion-usuario"
      >
        <div class="publicacion-nombre">{{ libro.titulo }}</div>
        <div class="publicacion-tipo">{{ libro.estado }}</div>
      </router-link>
    </div>
    <div class="publicaciones">
      <router-link
        v-for="monografia in filteredMonografias"
        :key="monografia.id"
        :to="{ path: getCategoryPath('monografia', monografia.id) }"
        class="publicacion-usuario"
      >
        <div class="publicacion-nombre">{{ monografia.titulo }}</div>
        <div class="publicacion-tipo">{{ monografia.estado }}</div>
      </router-link>
    </div>
    <div class="condecoraciones">
      <router-link
        v-for="premio in filteredPremios"
        :key="premio.id"
        :to="{ path: getCategoryPath('premio', premio.id) }"
        class="condecoracion-usuario"
      >
        <div class="condecoracion-nombre">{{ premio.titulo_resultado }}</div>
        <div class="condecoracion-tipo">{{ premio.estado }}</div>
      </router-link>
    </div>
    <div class="condecoraciones">
      <router-link
        v-for="reconocimiento in filteredReconocimientos"
        :key="reconocimiento.id"
        :to="{ path: getCategoryPath('reconocimiento', reconocimiento.id) }"
        class="condecoracion-usuario"
      >
        <div class="condecoracion-nombre">{{ reconocimiento.nombre_reconocimiento }}</div>
        <div class="condecoracion-tipo">{{ reconocimiento.estado }}</div>
      </router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      selectedCategoryArticulos: 'all',
      selectedCategoryCondecoraciones: 'all',
      articulosUsuario: [],
      librosUsuario: [],
      monografiasUsuario: [],
      premiosUsuario: [],
      reconocimientosUsuario: [],
      searchQuery: '', // Propiedad para la búsqueda
    };
  },
  created() {
    this.obtenerArticulosUsuario();
    this.obtenerLibrosUsuario();
    this.obtenerMonografiasUsuario();
    this.obtenerPremiosUsuario();
    this.obtenerReconocimientosUsuario();
  },
  methods: {
    async obtenerArticulosUsuario() {
      try {
        const userData = JSON.parse(localStorage.getItem('userData'));
        const userName = userData.username;
        const getUSER = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/?nombreUsuario=${userName}`);
        const respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/${getUSER.data[0].id}/write_articulo/`);
        this.articulosUsuario = respuesta.data;
      } catch (error) {
        console.error('Error al obtener las publicaciones del usuario', error);
      }
    },
    async obtenerLibrosUsuario() {
      try {
        const userData = JSON.parse(localStorage.getItem('userData'));
        const userName = userData.username;
        const getUSER = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/?nombreUsuario=${userName}`);
        const respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/${getUSER.data[0].id}/write_libro/`);
        this.librosUsuario = respuesta.data;
      } catch (error) {
        console.error('Error al obtener las condecoraciones del usuario', error);
      }
    },
    async obtenerMonografiasUsuario() {
      try {
        const userData = JSON.parse(localStorage.getItem('userData'));
        const userName = userData.username;
        const getUSER = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/?nombreUsuario=${userName}`);
        const respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/${getUSER.data[0].id}/write_monografia/`);
        this.monografiasUsuario = respuesta.data;
      } catch (error) {
        console.error('Error al obtener las publicaciones del usuario', error);
      }
    },
    async obtenerPremiosUsuario() {
      try {
        const userData = JSON.parse(localStorage.getItem('userData'));
        const userName = userData.username;
        const getUSER = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/?nombreUsuario=${userName}`);
        const respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/${getUSER.data[0].id}/write_premio/`);
        this.premiosUsuario = respuesta.data;
      } catch (error) {
        console.error('Error al obtener las condecoraciones del usuario', error);
      }
    },
    async obtenerReconocimientosUsuario() {
      try {
        const userData = JSON.parse(localStorage.getItem('userData'));
        const userName = userData.username;
        const getUSER = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/?nombreUsuario=${userName}`);
        const respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/${getUSER.data[0].id}/write_reconocimiento/`);
        this.reconocimientosUsuario = respuesta.data;
      } catch (error) {
        console.error('Error al obtener las publicaciones del usuario', error);
      }
    },
    selectCategoryArticulos() {
      this.selectedCategoryCondecoraciones = 'all';
    },
    selectCategoryCondecoraciones() {
      this.selectedCategoryArticulos = 'all';
    },
    getCategoryPath(category, id) {
      const userData = JSON.parse(localStorage.getItem('userData'));
      const userROl = userData.role;
      if (userROl === '5'){
        switch (category) {
        case 'articulo':
          return `/add_articulo/${id}`;
        case 'libro':
          return `/add_libro/${id}`;
        case 'monografia':
          return `/add_monografia/${id}`;
        case 'premio':
          return `/add_premio/${id}`;
        case 'reconocimiento':
          return `/add_reconocimiento/${id}`;
        default:
          return '/';
      }
      } else {
        switch (category) {
        case 'articulo':
          return `/add_articulo2/${id}`;
        case 'libro':
          return `/add_libro2/${id}`;
        case 'monografia':
          return `/add_monografia2/${id}`;
        case 'premio':
          return `/add_premio2/${id}`;
        case 'reconocimiento':
          return `/add_reconocimiento2/${id}`;
        default:
          return '/';
      }
      }
      
    },
  },
  computed: {
    filteredArticulos() {
      return (
        (this.selectedCategoryArticulos === 'articulo'  || this.selectedCategoryArticulos === 'all') &&
        this.selectedCategoryArticulos !== 'libro' &&
        this.selectedCategoryArticulos !== 'monografia' &&
        this.selectedCategoryCondecoraciones !== 'premio' &&
        this.selectedCategoryCondecoraciones !== 'reconocimiento'
      )
        ? this.articulosUsuario
        : [];
    },
    filteredLibros() {
      return (
        (this.selectedCategoryArticulos === 'libro' || this.selectedCategoryArticulos === 'all') &&
        this.selectedCategoryArticulos !== 'articulo' &&
        this.selectedCategoryArticulos !== 'monografia' &&
        this.selectedCategoryCondecoraciones !== 'premio' &&
        this.selectedCategoryCondecoraciones !== 'reconocimiento'
      )
        ? this.librosUsuario
        : [];
    },
    filteredMonografias() {
      return (
        (this.selectedCategoryArticulos === 'monografia' || this.selectedCategoryArticulos === 'all') &&
        this.selectedCategoryArticulos !== 'articulo' &&
        this.selectedCategoryArticulos !== 'libro' &&
        this.selectedCategoryCondecoraciones !== 'premio' &&
        this.selectedCategoryCondecoraciones !== 'reconocimiento'
      )
        ? this.monografiasUsuario
        : [];
    },
    filteredPremios() {
      return (
        (this.selectedCategoryCondecoraciones === 'premio'  || this.selectedCategoryCondecoraciones === 'all') &&
        this.selectedCategoryArticulos !== 'articulo' &&
        this.selectedCategoryArticulos !== 'libro' &&
        this.selectedCategoryArticulos !== 'monografia' &&
        this.selectedCategoryCondecoraciones !== 'reconocimiento'
      )
        ? this.premiosUsuario
        : [];
    },
    filteredReconocimientos() {
      return (
        (this.selectedCategoryCondecoraciones === 'reconocimiento' || this.selectedCategoryCondecoraciones === 'all') &&
        this.selectedCategoryArticulos !== 'articulo' &&
        this.selectedCategoryArticulos !== 'libro' &&
        this.selectedCategoryArticulos !== 'monografia' &&
        this.selectedCategoryCondecoraciones !== 'premio'
      )
        ? this.reconocimientosUsuario
        : [];
    },
  },
};
</script>

<style scoped>
.user-data {
  width: 68rem;
  text-align: center;
  padding: 0 5rem 0 5rem;
  border: 1px solid #afafc7;
  margin: 10px;
  border-radius: 10px;

}

.header {
  display: flex;
}

.header img {
  max-width: 100px;
}

.header h1 {
  font-size: 2rem;
  margin: 20px 0;
}

.publicaciones,
.condecoraciones {
  margin-top: 20px;
}

/* Estilos para elementos de la lista de publicaciones y condecoraciones del usuario */
.publicacion-usuario,
.condecoracion-usuario {
  padding: 0.5rem 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-bottom: 0.5rem;
  background-color: #f0f0f0;
  display: flex;
  justify-content: space-between;
  text-align: left;
  color: black;
}

.publicacion-nombre,
.condecoracion-nombre {
  font-weight: bold;
}

.publicacion-tipo,
.condecoracion-tipo {
  color: #666;
}

.filter-box {
  display: flex;
  justify-content: none;
  margin-bottom: 20px;
  padding: 20px;
  border-radius: 10px;
}

.filter,
select {
  margin: 15px;
  padding-left: 20px;
  border-radius: 5px;

}

</style>
