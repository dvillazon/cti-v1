<template>
  <div class="article-form">
    <div class="header">
      <img src="../assets/mas.png" alt="Icono" class="icon" />
      <h1>Distinción</h1>
    </div>
    <div class="divider"></div>
    <div class="form-container">
      <form>
        <div class="form-group">
          <label for="distincion">Distinción</label>
          <div class="input-container">
            <img src="../assets/ident.png" alt="Icono Título" class="input-icon" />
            <input type="text" id="distincion" v-model="distincion" />
          </div>
        </div>
        <div class="form-group">
          <label for="denominacion">Denominación</label>
          <div class="input-container">
            <img src="../assets/ident.png" alt="Icono Denominación" class="input-icon" />
            <input type="text" id="denominacion" v-model="denominacion" />
          </div>
        </div>
        <div class="form-group">
          <label for="alcance">Alcance</label>
          <div class="input-container">
            <img src="../assets/ident.png" alt="Icono Alcance" class="input-icon" />
            <input type="text" id="alcance" v-model="alcance" />
          </div>
        </div>
        <div class="form-group">
          <label for="autores">Autores</label>
          <div class="author-list">
            <div v-for="(autor, index) in autores" :key="index" class="author-item">
              <img src="../assets/user2.png" alt="Icono Autor" class="input-icon" />
              <input type="text" v-model="autores[index]" />
              <button class="add-author-button" @click="agregarAutor">+</button>
              <button class="remove-author-button" @click="eliminarAutor(index)">-</button>
            </div>
          </div>
        </div>
        <div class="form-group">
          <label for="evento">Evento</label>
          <div class="input-container">
            <img src="../assets/ident.png" alt="Icono Evento" class="input-icon" />
            <input type="text" id="evento" v-model="evento" />
          </div>
        </div>
        <div class="form-group">
          <label for="otorgadoPor">Otorgado por</label>
          <div class="input-container">
            <img src="../assets/ident.png" alt="Icono Otorgado por" class="input-icon" />
            <input type="text" id="otorgadoPor" v-model="otorgadoPor" />
          </div>
        </div>
        <div class="form-group">
          <label for="causa">Por qué</label>
          <div class="input-container">
            <img src="../assets/ident.png" alt="Icono Causa" class="input-icon" />
            <input type="text" id="causa" v-model="causa" placeholder="Causa del otorgamiento" />
          </div>
        </div>
        <div class="form-group">
          <label for="anoPublicacion">Fecha</label>
          <div class="input-container">
            <img src="../assets/calendario.png" alt="Icono Año de Publicación" class="input-icon" />
            <input type="text" id="anoPublicacion" v-model="anoPublicacion" />
          </div>
        </div>
        <div class="form-group">
          <label for="lugarPublicacion">País</label>
          <div class="input-container">
            <img src="../assets/lugar.png" alt="Icono Lugar de Publicación" class="input-icon" />
            <input type="text" id="lugarPublicacion" v-model="lugarPublicacion" />
          </div>
        </div>
        <button v-if="botonguardar" class="save-button" @click="guardarDistincion">Guardar</button>
        <div v-if=" userRole === 'jefe'">
        <button v-if="esDistincionExistente" class="save-button" @click="aprobarDistincion">Aprobar</button>
        <button v-if="esDistincionExistente"  class="elim-button" @click="eliminarDistincion">Eliminar</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
     distincion: "",
      autores: [""],
      denominacion: "",
      alcance: "",
      otorgadoPor: "",
      causa: "",
      evento: "",
      anoPublicacion: "",
      lugarPublicacion: "",
      esDistincionExistente: false,
      botonguardar: true,
    };
  },
  computed: {
    userRole() {
      return localStorage.getItem('userRole');
    },
  },
  created() {
    const distincionId = this.$route.params.id;
    if (distincionId) {
      this.esDistincionExistente = true;
      this.botonguardar = false;
      this.cargarDatosDistincion(distincionId);
    }
  },
  methods: {
  cargarDatosDistincion(distincionId) {
    axios.get(`/api/distinciones/${distincionId}`)
      .then(response => {
        this.distincion = response.data.distincion;
        this.autores = response.data.autores;
        this.denominacion = response.data.denominacion;
        this.alcance = response.data.alcance;
        this.otorgadoPor = response.data.otorgadoPor;
        this.causa = response.data.causa;
        this.evento = response.data.evento;
        this.anoPublicacion = response.data.anoPublicacion;
        this.lugarPublicacion = response.data.lugarPublicacion;
        // Actualizar otros campos
      })
      .catch(error => {
        alert('Error al cargar datos de la distinción:', error);
        // Manejar errores
      });
  },
  aprobarDistincion() {
    const distincionId = this.$route.params.id;
    axios.put(`/api/aprobar/distinciones/${distincionId}`)
      .then(response => {
        console.log('Distinción aprobada:', response.data);
        // Lógica adicional si es necesario
      })
      .catch(error => {
        console.error('Error al aprobar la distinción:', error);
        // Manejar errores
      });
  },
  eliminarDistincion() {
      const distincionId = this.$route.params.id;
      axios.delete(`/api/distinciones/${distincionId}`)
        .then(response => {
          console.log('Distinción eliminada:', response.data);
          // Lógica adicional si es necesario
        })
        .catch(error => {
          console.error('Error al eliminar la distinción:', error);
          // Manejar errores
        });
    },
  guardarDistincion() {
    const datos = {
      distincion: this.distincion,
      autores: this.autores,
      denominacion: this.denominacion,
      alcance: this.alcance,
      otorgadoPor: this.otorgadoPor,
      causa: this.causa,
      evento: this.evento,
      anoPublicacion: this.anoPublicacion,
      lugarPublicacion: this.lugarPublicacion,
      // Agregar el resto de los campos aquí
    };
    axios.post('URL_DEL_BACKEND/tuRutaDeGuardado', datos)
      .then(response => {
        console.log('Datos enviados al backend:', response.data);
        // Restablecer los campos si es necesario
        this.distincion = '';
        this.autores = [''];
        this.denominacion = '';
        this.alcance = '';
        this.otorgadoPor = '';
        this.causa = '';
        this.evento = '';
        this.anoPublicacion = '';
        this.lugarPublicacion = '';
        // Resto de los campos
      })
      .catch(error => {
        console.error('Error al enviar datos al backend:', error);
      });
  },
  agregarAutor() {
    this.autores.push("");
  },
  eliminarAutor(index) {
    this.autores.splice(index, 1);
  },
},

};
</script>

  
<style scoped>
.article-form {
  display: flex;
  flex-direction: column;
  width: 78rem;
  margin: 10px;
  padding: 20px;
  padding-left: 20rem;
  padding-right: 20rem;
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

p {
  margin-right: 12rem;
}

.header {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.divider {
  height: 1px;
  background-color: black;
  width: 144%;
  margin: 10px;
  margin-left: -9rem;
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

form {
  width: 100%;
}

.form-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
}

.label {
  font-weight: 600;
  font-size: 1rem;
  margin-bottom: 5px;
}

.input-container {
  display: flex;
  align-items: center;
}

input {
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  flex: 4;
}

.input-icon {
  width: 30px;
  height: 30px;
  margin-left: 10px;
}

input[type="checkbox"] {
  margin-right: 10px;
}



.author-list {
  display: flex;
  flex-direction: column;
}

.author-item {
  display: flex;
  align-items: center;
}

.remove-author-button {
  background-color: #dc3545;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 5px 10px;
  cursor: pointer;
  margin-left: 5px;
}

.add-author-button {
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 5px 10px;
  cursor: pointer;
  margin-left: 5px;
}

.save-button {
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 10px;
  padding: 0.5rem 1rem;
  cursor: pointer;
  margin-top: 20px;
  margin: 10px;
}
.elim-button{
  background-color: red;
  color: white;
  border: none;
  border-radius: 10px;
  padding: 0.5rem 1rem;
  cursor: pointer;
  margin-top: 20px;
  margin: 10px;
}
</style>
  