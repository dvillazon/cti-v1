<template>
    <div class="article-form">
      <div class="header">
        <img src="../assets/mas.png" alt="Icono" class="icon" />
        <h1>Premio</h1>
      </div>
      <div class="divider"></div>
      <div class="form-container">
        <form>
          <div class="form-group">
          <label for="denominacion">Denominación</label>
          <div class="input-container">
            <img src="../assets/ident.png" alt="Icono Denominación" class="input-icon" />
            <select id="denominacion" v-model="denominacion">
              <option value="Premio de la ACC">Premio de la ACC </option>
              <option value="Premio de la Innovacion Nacional">Premio de la Innovacion Nacional</option>
              <option value="Premio CITMA Provincial">Premio CITMA Provincial</option>
              <option value="Premio CITMA Provincial de Innovacion">Premio CITMA Provincial de Innovacion</option>
              <option value="Premio CITMA Joven Investigador">Premio CITMA Joven Investigador</option>
              <option value="Premio Ramal">Premio Ramal</option>
              <option value="Premio del Forum de Ciencia y Tecnologia">Premio del Forum de Ciencia y Tecnologia</option>
              <option value="Premio anual al Joven Investigador">Premio anual a Joven Investigador</option>
              <option value="Premio anual al Joven Tecnologo Investigador">Premio anual al Joven Tecnologo Investigador
              </option>
              <option value="Otro">Otro</option>
              <!-- Agrega más opciones según sea necesario -->
            </select>
          </div>
        </div>
          <div class="form-group">
            <label for="titulo">Resultado</label>
            <div class="input-container">
              <img src="../assets/ident.png" alt="Icono Título" class="input-icon" />
              <input type="text" id="titulo" v-model="resultado" placeholder="Indique el título del resultado que obtiene el premio" />
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
            <label for="titulo">Sectores Estratégico</label>
            <div class="input-container">
              <img src="../assets/ident.png" alt="Icono Título" class="input-icon" />
              <input type="text" id="titulo" v-model="sectoresEstrategicos" />
            </div>
          </div>
          <div class="form-group">
            <label for="titulo">Otorgado por</label>
            <div class="input-container">
              <img src="../assets/ident.png" alt="Icono Título" class="input-icon" />
              <input type="text" id="titulo" v-model="otorgadoPor" placeholder="Indique la organización o institución q otorgó el premio" />
            </div>
          </div>
          <div class="form-group">
            <label for="titulo">Evento</label>
            <div class="input-container">
              <img src="../assets/ident.png" alt="Icono Título" class="input-icon" />
              <input type="text" id="titulo" v-model="evento" placeholder="Indique el nombre del evento, concurso o competición" />
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
          
          <button v-if="botonguardar" class="save-button" @click="guardarPremio">Guardar</button>
          <div v-if="esPremioExistente">
          <button v-if="mostrarBotonAprobar" class="save-button" @click="aprobarPremio">Aprobar</button>
          <button v-if="mostrarBotonEliminar" class="elim-button" @click="eliminarPremio">Desaprobar</button>
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
        denominacion:"",
        resultado: "",
        autores: [""],
        autoresList: [],
        estadoPremio:'Pendiente',
        alcance:"",
        fecha: "",
        revista: "",
        pais: "",
        evento: "",
        otorgadoPor: "",
        sectoresEstrategicos: "",
        esPremioExistente: false,
        botonguardar: true,
      };
    },
    created() {
    const premioId = this.$route.params.id;
    const userData = JSON.parse(localStorage.getItem('userData'));
    const rol = userData.role;
    if(premioId && rol !='4'){
      this.esPremioExistente = false;
      this.botonguardar = false;
      this.cargarDatosPremio(premioId);
    }
     else if (premioId) {
      this.esPremioExistente = true;
      this.botonguardar = false;
      this.cargarDatosPremio(premioId);
    }
    this.obtenerAutoresDesdeBackend()
  },
    computed:{
      mostrarBotonAprobar() {
      return this.esPremioExistente && this.estadoPremio !== 'Aprobado';
    },
    mostrarBotonEliminar() {
      return this.esPremioExistente && this.estadoPremio !== 'Aprobado';
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
        async cargarDatosPremio(premioId) {
        try{
         const response = await axios.get(`http://127.0.0.1:8000/api/v1.0/premio/${premioId}/`);
         const premio = response.data
         const responseAutores = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/`);
            const autoresList = responseAutores.data;

         // Mapear los IDs de autores a nombres
           const nameAutores = premio.autores.map(id => {
           const autor = autoresList.find(a => a.id === id);
          console.log('ID:', id, 'Autor:', autor);
          return autor ;
        });
          this.resultado = premio.titulo_resultado;
          this.alcance = premio.alcance;
          this.sectoresEstrategicos = premio.sector_estrategico;
          this.otorgadoPor = premio.otorgado_por;
          this.evento = premio.nombre_evento;
          this.fecha = premio.fecha;
          this.estadoPremio= premio.estado 
          this.pais = premio.pais;
          this.autores = nameAutores
          this.denominacion = premio.denominacion
        }
        catch(error) {
          alert('Error al cargar datos del premio:', error);
          // Manejar errores
        };
    },
    aprobarPremio() {
      const premioId = this.$route.params.id; // Obtener el ID del premio desde la ruta

      axios.put(`http://127.0.0.1:8000/api/v1.0/premio/${premioId}/`,{ estado: 'Aprobado' })
        .then(response => {
          // Lógica para manejar la aprobación exitosa
          alert('Premio aprobado con éxito')
          console.log('Premio aprobado:', response.data);
          // Podrías hacer una redirección o actualizar la vista si es necesario
        })
        .catch(error => {
          console.error('Error al aprobar el premio:', error);
          // Manejar errores
        });
    },

    async guardarPremio() {
    // Aquí deberías enviar los datos ingresados al componente padre (emitir un evento)
    const idsAutores = this.autores.map(autor => autor.id);
    const data = {
      autores: idsAutores,
      alcance:this.alcance,
      otorgado_por:this.otorgadoPor,
      fecha : this.fecha,
      pais : this.pais,
      denominacion: this.denominacion,
      titulo_resultado: this.resultado,
      sector_estrategico: this.sectoresEstrategicos,
      nombre_evento: this.evento,
      estado:"pendiente",
    };
    try {
      // Aquí envías los datos usando Axios 
      //const userData = JSON.parse(localStorage.getItem('userData'));
      //const userName = userData.username;
      const response = await axios.post(`http://127.0.0.1:8000/api/v1.0/premio/`, data);
      console.log('Datos enviados:', response.data);
      // Realizar lógica después de enviar los datos si es necesario
      alert('Premio guardado con éxito')
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
      
      eliminarPremio() {
        const premioId = this.$route.params.id; // Obtener el ID del premio desde la ruta

    axios.put(`http://127.0.0.1:8000/api/v1.0/premio/${premioId}/`,{ estado: 'Desaprobado' })
    .then(response => {
      alert('Premio desaprobado con éxito')
    // Lógica para manejar la aprobación exitosa
    console.log('Premio aprobado:', response.data);
    // Podrías hacer una redirección o actualizar la vista si es necesario
  })
  .catch(error => {
    alert('Error al desaprobar el premio')
    console.error('Error al aprobar el premio:', error);
    // Manejar errores
  });
    },
  }
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
  
  input,select {
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
  .elim-button{
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
  </style>
  