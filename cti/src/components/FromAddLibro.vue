<template>
  <div class="article-form">
    <div class="header">
      <img src="../assets/mas.png" alt="Icono" class="icon" />
      <h1>Libro</h1>
    </div>
    <div class="divider"></div>
    <div class="form-container">
      <form>
        <div class="form-group">
          <label for="titulo">Título*</label>
          <div class="input-container">
            <img src="../assets/ident.png" alt="Icono Título" class="input-icon" />
            <input type="text" id="titulo" v-model="titulo" required placeholder="Título del Libro" />
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
          <label for="formato">Formato</label>
          <div class="input-container">
            <img src="../assets/area.png" alt="Icono Formato" class="input-icon" />
            <input type="checkbox" id="formatoImpreso" v-model="formato" />
            <p>Impreso</p>
            <input type="checkbox" id="formatoElectronico" v-model="formatoElectronico" />
            <p>Electrónico</p>
          </div>
        </div>
        <div class="form-group">
          <label for="url">URL del Libro Electrónico</label>
          <div class="input-container">
            <img src="../assets/url.png" alt="Icono URL" class="input-icon" />
            <input type="text" id="url" v-model="url" :disabled="!formatoElectronico" placeholder="URL del libro" />
          </div>
        </div>
        <div class="form-group">
          <label for="anoPublicacion">Año de Publicación*</label>
          <div class="input-container">
            <img src="../assets/calendario.png" alt="Icono Año de Publicación" class="input-icon" />
            <input type="number" id="anoPublicacion" v-model="anoPublicacion" placeholder="2023" required min="1800" />
          </div>
        </div>

        <div class="form-group">
          <label for="editorial">Editorial</label>
          <div class="input-container">
            <img src="../assets/editorial.png" alt="Icono Editorial" class="input-icon" />
            <input type="text" id="editorial" v-model="editorial" placeholder="Nombre de la editorial" />
          </div>
        </div>
        <div class="form-group">
          <label for="paginas">Páginas</label>
          <div class="input-container">
            <img src="../assets/paginas.png" alt="Icono Rango de Páginas" class="input-icon" />
            <input type="text" id="paginas" v-model="paginas" placeholder="23" />
          </div>
        </div>
        <div class="form-group">
          <label for="isbn">ISBN</label>
          <div class="input-container">
            <img src="../assets/ident.png" alt="Icono ISBN" class="input-icon" />
            <input type="text" id="isbn" v-model="isbn" placeholder="####-####" />
          </div>
        </div>
        <div class="form-group">
          <label for="areaUCF">Área de UCF</label>
          <div class="input-container">
            <img src="../assets/area.png" alt="Icono Área de UCF" class="input-icon" />
            <input type="text" id="areaUCF" v-model="areaUCF" @input="filterAreasUCF" @focus="showAreasUCF"
              placeholder="Seleccione área de UCF" />

          </div>
          <div v-if="showAreaUCFList" class="suggestion-list">
            <div v-for="areaUCF in filteredAreasUCF" :key="areaUCF" @click="selectAreaUCF(areaUCF)">
              {{ areaUCF }}
            </div>
          </div>
        </div>
        <div class="form-group">
          <label for="paisPublicacion">País de Publicación*</label>
          <div class="input-container">
            <img src="../assets/lugar.png" alt="Icono País de Publicación" class="input-icon" />
            <input type="text" id="paisPublicacion" v-model="paisPublicacion" @input="filterPaises" @focus="showPaises"
              placeholder="Seleccione un país" required />
            <div v-if="showPaisList" class="suggestion-list">
              <div v-for="pais in filteredPaises" :key="pais" @click="selectPais(pais)">
                {{ pais }}
              </div>
            </div>
          </div>
          <div v-if="showPaisList" class="suggestion-list">
            <div v-for="pais in filteredPaises" :key="pais" @click="selectPais(pais)">
              {{ pais }}
            </div>
          </div>
        </div>

        <button v-if="botonguardar" class="save-button" @click="guardarLibro">Guardar</button>
        <div v-if="esLibroExistente">
        <button v-if="mostrarBotonAprobar" class="save-button" @click="aprobarLibro">Aprobar</button>
        <button v-if="mostrarBotonEliminar" class="elim-button" @click="eliminarLibro">Desaprobar</button>
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
      titulo: "",
      autores: [""],
      autoresList: [],
      estadoLibro:'Pendiente',
      formato: "",
      paginas: "",
      formatoElectronico: false,
      url: "",
      anoPublicacion: "",
      areaUCF: "",
      editorial: "",
      isbn: "",
      paisPublicacion: "",
      esLibroExistente: false,
      botoneliminar: false,
      botonguardar: true,
      paises: [
        'Afganistán',
        'Albania',
        'Alemania',
        'Andorra',
        'Angola',
        'Antigua y Barbuda',
        'Arabia Saudita',
        'Argelia',
        'Argentina',
        'Armenia',
        'Australia',
        'Austria',
        'Azerbaiyán',
        'Bahamas',
        'Bangladés',
        'Barbados',
        'Baréin',
        'Bélgica',
        'Belice',
        'Benín',
        'Bielorrusia',
        'Birmania',
        'Bolivia',
        'Bosnia y Herzegovina',
        'Botsuana',
        'Brasil',
        'Brunéi',
        'Bulgaria',
        'Burkina Faso',
        'Burundi',
        'Bután',
        'Cabo Verde',
        'Camboya',
        'Camerún',
        'Canadá',
        'Catar',
        'Chad',
        'Chile',
        'China',
        'Chipre',
        'Ciudad del Vaticano',
        'Colombia',
        'Comoras',
        'Corea del Norte',
        'Corea del Sur',
        'Costa de Marfil',
        'Costa Rica',
        'Croacia',
        'Cuba',
        'Dinamarca',
        'Dominica',
        'Ecuador',
        'Egipto',
        'El Salvador',
        'Emiratos Árabes Unidos',
        'Eritrea',
        'Eslovaquia',
        'Eslovenia',
        'España',
        'Estados Unidos',
        'Estonia',
        'Etiopía',
        'Filipinas',
        'Finlandia',
        'Fiyi',
        'Francia',
        'Gabón',
        'Gambia',
        'Georgia',
        'Ghana',
        'Granada',
        'Grecia',
        'Guatemala',
        'Guyana',
        'Guinea',
        'Guinea-Bisáu',
        'Guinea Ecuatorial',
        'Haití',
        'Honduras',
        'Hungría',
        'India',
        'Indonesia',
        'Irak',
        'Irán',
        'Irlanda',
        'Islandia',
        'Islas Marshall',
        'Islas Salomón',
        'Israel',
        'Italia',
        'Jamaica',
        'Japón',
        'Jordania',
        'Kazajistán',
        'Kenia',
        'Kirguistán',
        'Kiribati',
        'Kuwait',
        'Laos',
        'Lesoto',
        'Letonia',
        'Líbano',
        'Liberia',
        'Libia',
        'Liechtenstein',
        'Lituania',
        'Luxemburgo',
        'Macedonia del Norte',
        'Madagascar',
        'Malasia',
        'Malaui',
        'Maldivas',
        'Malí',
        'Malta',
        'Marruecos',
        'Mauricio',
        'Mauritania',
        'México',
        'Micronesia',
        'Moldavia',
        'Mónaco',
        'Mongolia',
        'Montenegro',
        'Mozambique',
        'Namibia',
        'Nauru',
        'Nepal',
        'Nicaragua',
        'Níger',
        'Nigeria',
        'Noruega',
        'Nueva Zelanda',
        'Omán',
        'Países Bajos',
        'Pakistán',
        'Palaos',
        'Panamá',
        'Papúa Nueva Guinea',
        'Paraguay',
        'Perú',
        'Polonia',
        'Portugal',
        'Reino Unido',
        'República Centroafricana',
        'República Checa',
        'República del Congo',
        'República Democrática del Congo',
        'República Dominicana',
        'Ruanda',
        'Rumania',
        'Rusia',
        'Samoa',
        'San Cristóbal y Nieves',
        'San Marino',
        'Santa Lucía',
        'Santo Tomé y Príncipe',
        'Senegal',
        'Serbia',
        'Seychelles',
        'Sierra Leona',
        'Singapur',
        'Siria',
        'Somalia',
        'Sri Lanka',
        'Suazilandia',
        'Sudáfrica',
        'Sudán',
        'Sudán del Sur',
        'Suecia',
        'Suiza',
        'Surinam',
        'Tailandia',
        'Taiwán',
        'Tanzania',
        'Tayikistán',
        'Timor Oriental',
        'Togo',
        'Tonga',
        'Trinidad y Tobago',
        'Túnez',
        'Turkmenistán',
        'Turquía',
        'Tuvalu',
        'Ucrania',
        'Uganda',
        'Uruguay',
        'Uzbekistán',
        'Vanuatu',
        'Venezuela',
        'Vietnam',
        'Yemen',
        'Yibuti',
        'Zambia',
        'Zimbabue',
        // Agrega más países según tus necesidades
      ],
      areasUCF: [
        'FING (Facultad de Ingeniería)',
        'FCE (Facultad de Ciencias Económicas)',
        'FCS (Facultad de Ciencias Sociales)',
        'FH (Facultad de Humanidades)',
        'FCF (Facultad de Cultura Física)',
        'FCA (Facultad de Ciencias Agropecuarias)',
        'FE (Facultad de Educación)',
        'CUM Cruces',
        'CUM Rodas',
        'CUM Lajas',
        'CUM Cumanayagua',
        'CUM Aguada',
      ],
      showPaisList: false,
      showAreaUCFList: false,
    };
  },

  created() {
   const libroId = this.$route.params.id; // Obtén el ID del libro de la ruta
   const userData = JSON.parse(localStorage.getItem('userData'));
   const rol = userData.role;
   if(libroId && rol != '4' ){
     this.esLibroExistente = false;
     this.botoneliminar = false,
     this.botonguardar = false;
     // Lógica para cargar la información del libro seleccionado
     this.cargarDatosLibro(libroId);
   }
   else if (libroId) {
     this.esLibroExistente = true;
     this.botoneliminar = true,
     this.botonguardar = false;
     // Lógica para cargar la información del libro seleccionado
     this.cargarDatosLibro(libroId);
   }
   this.obtenerAutoresDesdeBackend()
 },
  computed: {

    filteredPaises() {
      return this.paises.filter((pais) =>
        pais.toLowerCase().includes(this.paisPublicacion.toLowerCase())
      );
    },
    filteredAreasUCF() {
      return this.areasUCF.filter((areaUCF) =>
        areaUCF.toLowerCase().includes(this.areaUCF.toLowerCase())
      );

    },
    mostrarBotonAprobar() {
      return this.esLibroExistente && this.estadoLibro !== 'Aprobado';
    },
    mostrarBotonEliminar() {
      return this.esLibroExistente && this.estadoLibro !== 'Aprobado';
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
    async cargarDatosLibro() {
      const libroId = this.$route.params.id; // Obtener el ID del libro de la ruta
      console.log('el id del libro es :',libroId)
      try{
        // Lógica para cargar los datos del libro desde tu backend usando axios
         const response = await axios.get(`http://127.0.0.1:8000/api/v1.0/libro/${libroId}/`);
            // Rellenar campos con la información del libro
            console.log('Datos del libro',response.data)
            const libro = response.data; // Asumiendo que la respuesta contiene los datos del libro

            const responseAutores = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/`);
            const autoresList = responseAutores.data;

         // Mapear los IDs de autores a nombres
           const nameAutores = libro.autores.map(id => {
           const autor = autoresList.find(a => a.id === id);
          console.log('ID:', id, 'Autor:', autor);
          return autor ;
        });
            this.titulo = libro.titulo;
            this.autores = nameAutores;
            this.anoPublicacion = libro.ano
            this.formatoElectronico = libro.formato
            this.url = libro.link
            this.areaUCF = libro.area
            this.estadoLibro= libro.estado 
            this.editorial = libro.editorial
            this.paginas = libro.paginas
            this.isbn = libro.isbn
            this.paisPublicacion= libro.pais
            // ... restablecer otros campos con la información del libro ...
           // this.esLibroExistente = true; // Marcar como un libro existente
      }
      
          
          catch(error) {
            alert('Error al cargar el libro:', error);
          };
      
    },
    async aprobarLibro() {
      try {
        const libroId = this.$route.params.id;

        // Realizar una petición al backend para marcar el artículo como aprobado
        const response = await axios.put(`http://127.0.0.1:8000/api/v1.0/libro/${libroId}/`, { estado: 'Aprobado' });
        console.log('Artículo aprobado:', response.data);

        // Puedes realizar alguna lógica adicional si es necesario
        alert('Libro aprobado con exito');
      } catch (error) {
        console.error('Error al aprobar el artículo:', error);
        // Manejo de errores
        alert('Error al aprobar el libro');
      }
    },
  
    async guardarLibro() {
    // Aquí deberías enviar los datos ingresados al componente padre (emitir un evento)
    const idsAutores = this.autores.map(autor => autor.id);
    const data = {
      titulo: this.titulo,
      autores: idsAutores,
      formato: true,
      link: this.url,
      paginas:this.paginas,
      ano: this.anoPublicacion,
      editorial : this.editorial,
      isbn: this.isbn,
      pais: this.paisPublicacion,
      area: this.areaUCF,
      estado:"pendiente",
    };
    try {
      // Aquí envías los datos usando Axios 
      //const userData = JSON.parse(localStorage.getItem('userData'));
      //const userName = userData.username;
      const response = await axios.post(`http://127.0.0.1:8000/api/v1.0/libro/`, data);
      console.log('Datos enviados:', response.data);
      // Realizar lógica después de enviar los datos si es necesario
      alert('Libro guardado con éxito')
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
    guardarArticulo() {
      // Agregar lógica para guardar el artículo de libro
    },
    filterPaises() {
      this.showPaisList = true;
    },
    showPaises() {
      if (this.paisPublicacion.length > 0) {
        this.showPaisList = true;
      }
    },
    selectPais(pais) {
      this.paisPublicacion = pais;
      this.showPaisList = false;
    },
    filterAreasUCF() {
      this.showAreaUCFList = true;
    },

    showAreasUCF() {
      if (this.areaUCF.length > 0) {
        this.showAreaUCFList = true;
      }
    },

    selectAreaUCF(areaUCF) {
      this.areaUCF = areaUCF;
      this.showAreaUCFList = false;
    },
    async eliminarLibro() {
      try {
        const libroId = this.$route.params.id;
        // Realizar una petición al backend para marcar el artículo como aprobado
        const response = await axios.put(`http://127.0.0.1:8000/api/v1.0/libro/${libroId}/`, { estado: 'Desaprobado' });
        console.log('Artículo aprobado:', response.data);

        // Puedes realizar alguna lógica adicional si es necesario
        alert('Libro Desaprobado con exito');
      } catch (error) {
        console.error('Error al aprobar el artículo:', error);
        // Manejo de errores
        alert('Error al Desaprobar el libro');
      }
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

input, select{
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

.elim-button {
  background-color: red;
  color: white;
  border: none;
  border-radius: 10px;
  padding: 0.5rem 1rem;
  cursor: pointer;
  margin-top: 20px;
  margin: 10px;
}

.suggestion-list {
  position: absolute;
  border: 1px solid #ccc;
  margin-top: 3.5rem;
  margin-left: 2.5rem;
  background: #fff;
  max-height: 150px;
  overflow-y: auto;
  z-index: 1;
}

.suggestion-list div {
  padding: 5px;
  cursor: pointer;
}

.suggestion-list div:hover {
  background: #f0f0f0;

}
</style>
  