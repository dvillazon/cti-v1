<template>
  <div class="article-form">
    <div class="header">
      <img src="../assets/mas.png" alt="Icono" class="icon" />
      <h1>Reconocimiento</h1>
    </div>
    <div class="divider"></div>
    <div class="form-container">
      <form>
        <div class="form-group">
          <label for="reconocimiento">Reconocimiento</label>
          <div class="input-container">
            <img src="../assets/ident.png" alt="Icono Título" class="input-icon" />
            <select id="nombre_reconocimiento" v-model="reconocimiento" >
              <option value="Reconocimiento">Reconocimiento</option>
              <option value="Reconocimiento como revisor">Reconocimiento como revisor</option>
              <option value="Reconocimiento nacional">Reconocimiento nacional</option>
              <option value="Reconocimiento especial">Reconocimiento especial</option>
              <option value="Reconocimiento al mejor">Reconocimiento al mejor</option>
            </select>
          </div>
        </div>
        <div class="form-group">
          <label for="autores">Autores*</label>
          <div class="author-list">
            <div v-for="(autor, index) in autores" :key="index" class="author-item">
              <img src="../assets/user2.png" alt="Icono Autor" class="input-icon" />
              <select v-model="autores[index]" required>
                <option value="" disabled hidden>Seleccione un autor</option>
                <option v-for="autor in autoresList" :key="autor" :value="autor">{{ autor.nombre }}</option>
              </select>
              <button class="add-author-button" @click="agregarAutor">+</button>
              <button class="remove-author-button" @click="eliminarAutor(index)">-</button>
            </div>
          </div>
        </div>
        <div class="form-group">
          <label for="alcance">Alcance</label>
          <div class="input-container">
            <img src="../assets/ident.png" alt="Icono Alcance" class="input-icon" />
            <select id="alcance" v-model="alcance">
              <option value="Internacional">Internacional</option>
              <option value="Nacional">Nacional</option>
              <option value="Provincial">Provincial</option>
              <option value="Municipal">Municipal</option>
              <option value="Local">Local</option>
            </select>
          </div>
        </div>
        <div class="form-group">
          <label for="otorgadoPor">Otorgado por</label>
          <div class="input-container">
            <img src="../assets/ident.png" alt="Icono Otorgado por" class="input-icon" />
            <input type="text" id="otorgadoPor" v-model="otorgadoPor" placeholder="Indique la organización o institución q otorgó el premio" />
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
            <input type="date" id="anoPublicacion" v-model="fecha" />
          </div>
        </div>
        <div class="form-group">
          <label for="lugarPublicacion">País</label>
          <div class="input-container">
            <img src="../assets/lugar.png" alt="Icono Lugar de Publicación" class="input-icon" />
            <input type="text" id="lugarPublicacion" v-model="pais" />
          </div>
        </div>
        <!-- Agrega otros campos aquí -->
        <button v-if="botonguardar" class="save-button" @click="guardarReconocimiento">Guardar</button>
        <div v-if="esReconocimientoExistente">
        <button v-if="mostrarBotonAprobar" class="save-button" @click="aprobarReconocimiento">Aprobar</button>
        <button v-if="mostrarBotonEliminar" class="elim-button" @click="eliminarReconocimiento">Eliminar</button>
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
        autores: [""],
        autoresList: [],
        reconocimiento: "",
        estadoPremio:'Pendiente',
        alcance: "",
        otorgadoPor: "",
        causa: "",
        fecha: "",
        pais:"",
        esReconocimientoExistente: false,
        botonguardar: true,
        botoneliminar: false,
      };
    },
    created() {
    const reconocimientoId = this.$route.params.id;
    const userData = JSON.parse(localStorage.getItem('userData'));
    const rol = userData.role;
    if(reconocimientoId && rol != '4'){
      this.esReconocimientoExistente = false;
      this.botonguardar = false;
      this.botoneliminar = false;
      this.cargarDatosReconocimiento(reconocimientoId);
    }
      else if (reconocimientoId) {
      this.esReconocimientoExistente = true;
      this.botonguardar = false;
      this.botoneliminar = true;
      this.cargarDatosReconocimiento(reconocimientoId);
    }
    this.obtenerAutoresDesdeBackend()
  }, 
  computed:{
      mostrarBotonAprobar() {
      return this.esReconocimientoExistente && this.estadoPremio !== 'Aprobado';
    },
    mostrarBotonEliminar() {
      return this.esReconocimientoExistente && this.estadoPremio !== 'Aprobado';
    },
    },
    methods: {

      async obtenerAutoresDesdeBackend() {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/`);
        console.log('los usuarios autores :',response.data)
        this.autoresList = response.data; // Suponiendo que la respuesta tiene la estructura correcta
      } catch (error) {
        console.error('Error al obtener la lista de autores desde el backend:', error);
        // Manejo de errores
        console.log('Error al obtener la lista de autores desde el backend');
      }
    },
        async cargarDatosReconocimiento(reconocimientoId) {
        try{
        const response = await axios.get(`http://127.0.0.1:8000/api/v1.0/reconocimiento/${reconocimientoId}/`);
        const rec = response.data;
        //console.log(rec)
        const responseAutores = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/`);
            const autoresList = responseAutores.data;

         // Mapear los IDs de autores a nombres
           const nameAutores = rec.autores.map(id => {
           const autor = autoresList.find(a => a.id === id);
          console.log('ID:', id, 'Autor:', autor);
          return autor ;
        });
        this.reconocimiento = rec.nombre_reconocimiento;
        this.alcance = rec.alcance;
        this.otorgadoPor = rec.otorgado_por;
        this.causa = rec.causa;
        this.fecha = rec.fecha
        this.estadoPremio= rec.estado 
        this.anoPublicacion = rec.ano;
        this.autores = nameAutores
        this.pais = rec.pais
        // Actualizar otros campos
        }catch(error){
          alert('Error al cargar datos del reconocimiento:', error);
          // Manejar errores
        };
    },

    aprobarReconocimiento() {
      const reconocimientoId = this.$route.params.id;

      axios.put(`http://127.0.0.1:8000/api/v1.0/reconocimiento/${reconocimientoId}/`,{ estado: 'Aprobado' })
        .then(response => {
          console.log('Reconocimiento aprobado:', response.data);
          // Lógica adicional si es necesario
          alert('Reconocimiento aprobado con éxio')
        })
        .catch(error => {
          console.error('Error al aprobar el reconocimiento:', error);
          alert('Error al aprobar el reconocimiento')
          // Manejar errores
        });
    },
    eliminarReconocimiento() {
      const reconocimientoId = this.$route.params.id;

    axios.put(`http://127.0.0.1:8000/api/v1.0/reconocimiento/${reconocimientoId}/`,{ estado: 'Desaprobado' })
  .then(response => {
    console.log('Reconocimiento desaprobado:', response.data);
    // Lógica adicional si es necesario
    alert('Reconocimiento Desaprobado con éxio')
  })
  .catch(error => {
    console.error('Error al desaprobar el reconocimiento:', error);
    alert('Error al Desaprobar el reconocimiento')
    // Manejar errores
  });
  },
  async guardarReconocimiento() {
    // Aquí deberías enviar los datos ingresados al componente padre (emitir un evento)
    const idsAutores = this.autores.map(autor => autor.id);
    const data = {
      autores: idsAutores,
      nombre_reconocimiento: this.reconocimiento,
      alcance: this.alcance,
      otorgado_por: this.otorgadoPor,
      causa : this.causa,
      fecha : this.fecha,
      pais : this.pais,
      estado:"pendiente",
    };
    try {
      // Aquí envías los datos usando Axios 
      //const userData = JSON.parse(localStorage.getItem('userData'));
      //const userName = userData.username;
      const response = await axios.post(`http://127.0.0.1:8000/api/v1.0/reconocimiento/`, data);
      console.log('Datos enviados:', response.data);
      // Realizar lógica después de enviar los datos si es necesario
      alert('Reconocimiento guardado con éxito')
    } catch (error) {
      console.error('Error al enviar los datos:', error);
      // Manejo de errores
      alert('Error al enviar los datos');
    }
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
    width: 68rem;
    margin: 10px;
    padding: 20px;
    padding-left: 20rem;
    padding-right: 20rem;
    background-color: #f7f7f7;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  p{
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
  
  input, select {
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
  