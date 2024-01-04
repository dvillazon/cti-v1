<template>
  <div class="article-form">
    <div class="header">
      <img src="../assets/mas.png" alt="Icono" class="icon" />
      <h1> Mongrafía</h1>
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
          <label for="url">URL de la Monografía Electrónica</label>
          <div class="input-container">
            <img src="../assets/url.png" alt="Icono URL" class="input-icon" />
            <input type="text" id="url" v-model="url" :disabled="!formatoElectronico" placeholder="URL de la monografía" />
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
            <input type="text" id="paginas" v-model="paginas" placeholder="30" />
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
        <div class="form-group">
          <label for="anoPublicacion">Año de Publicación*</label>
          <div class="input-container">
            <img src="../assets/calendario.png" alt="Icono Año de Publicación" class="input-icon" />
            <input type="number" id="anoPublicacion" v-model="anoPublicacion" placeholder="2023" required min="1800" />
          </div>
        </div>

        <button v-if="botonguardar" class="save-button" @click="guardarMonografia">Guardar</button>
        <div v-if="esMonografiaExistente">
        <button v-if="mostrarBotonAprobar" class="save-button" @click="aprobarMonografia">Aprobar</button>
        <button v-if="mostrarBotonEliminar" class="elim-button" @click="eliminarMonografia">Desaprobar</button>
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
      estadoMonografia:'Pendiente',
      formato: "",
      formatoElectronico: false,
      url: "",
      editorial: "",
      anoPublicacion: "",
      paginas: "",
      isbn: "",
      paisPublicacion: "",
      areaUCF: "",
      esMonografiaExistente: false,
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
    // Comprobar si se accede a través de una monografía específica
    const monografiaId = this.$route.params.id;
    const userData = JSON.parse(localStorage.getItem('userData'));
    const rol = userData.role;
    if(monografiaId && rol !='4'){
      this.esMonografiaExistente = false;
      this.botonguardar = false;
      // Lógica para cargar la información de la monografía seleccionada
      this.cargarDatosMonografia(monografiaId);
    }
    else if (monografiaId) {
      this.esMonografiaExistente = true;
      this.botonguardar = false;
      // Lógica para cargar la información de la monografía seleccionada
      this.cargarDatosMonografia(monografiaId);
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
      return this.esMonografiaExistente && this.estadoMonografia !== 'Aprobado';
    },
    mostrarBotonEliminar() {
      return this.esMonografiaExistente && this.estadoMonografia !== 'Aprobado';
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
    async cargarDatosMonografia(monografiaId) {
      try{
         const response = await axios.get( `http://127.0.0.1:8000/api/v1.0/monografia/${monografiaId}/`);
         const monografia = response.data;
         const responseAutores = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/`);
            const autoresList = responseAutores.data;

         // Mapear los IDs de autores a nombres
           const nameAutores = monografia.autores.map(id => {
           const autor = autoresList.find(a => a.id === id);
          console.log('ID:', id, 'Autor:', autor);
          return autor ;
        });
          // Actualizar los campos de la monografía con los datos obtenidos
          this.titulo = monografia.titulo;
          this.autores = nameAutores;
          if (monografia.formato == 1){
            this.formato = 0;
          }
          this.formatoElectronico = monografia.formato
          this.url = monografia.link;
          this.isbn = monografia.isbn
          this.estadoMonografia = monografia.estado
          this.areaUCF = monografia.area
          this.editorial = monografia.editorial
          this.paginas=monografia.paginas
          this.paisPublicacion = monografia.pais
          this.anoPublicacion = monografia.ano

      }
     catch(error) {
          alert('Error al cargar los datos de la monografía:', error);
          
          // Manejar errores
        };
    },
    
    async aprobarMonografia() {
      try {
        // Obtener el ID de la monografía desde la ruta
        const mId = this.$route.params.id;

        // Obtener los valores actuales de los campos relevantes
        const editorial = this.editorial;
        const isbn = this.isbn;
        const paginas = this.paginas;

        // Enviar los datos junto con el cambio de estado a 'Aprobado'
        const response = await axios.put(`http://127.0.0.1:8000/api/v1.0/monografia/${mId}/`, {
          estado: 'Aprobado',
          editorial: editorial,
          isbn: isbn,
          paginas: paginas,
          // Agrega otros campos relevantes según sea necesario
        });

        console.log('Monografía aprobada:', response.data);
        // Lógica adicional si es necesario
        alert('Monografía aprobada con éxito');
      } catch (error) {
        console.error('Error al aprobar la monografía:', error);
        // Manejar errores
        alert('Error al aprobar la monografía');
      }
    },
    async guardarMonografia() {
    // Aquí deberías enviar los datos ingresados al componente padre (emitir un evento)
    const idsAutores = this.autores.map(autor => autor.id);
    const data = {
      titulo: this.titulo,
      autores: idsAutores,
      formato: true,
      link: this.url,
      editorial : this.editorial,
      paginas: this.paginas,
      isbn: this.isbn,
      area: this.areaUCF,
      pais: this.paisPublicacion,
      ano: this.anoPublicacion,
      estado:"pendiente",
    };
    try {
      // Aquí envías los datos usando Axios 
      //const userData = JSON.parse(localStorage.getItem('userData'));
      //const userName = userData.username;
      const response = await axios.post(`http://127.0.0.1:8000/api/v1.0/monografia/`, data);
      console.log('Datos enviados:', response.data);
      // Realizar lógica después de enviar los datos si es necesario
      alert('Monografia guardada con éxito')
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
      // Agregar lógica para guardar el artículo
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
    async eliminarMonografia() {
      try {
        // Obtener el ID de la monografía desde la ruta
        const mId = this.$route.params.id;

        // Obtener los valores actuales de los campos relevantes
        const editorial = this.editorial;
        const isbn = this.isbn;
        const paginas = this.paginas;

        // Enviar los datos junto con el cambio de estado a 'Aprobado'
        const response = await axios.put(`http://127.0.0.1:8000/api/v1.0/monografia/${mId}/`, {
          estado: 'Desaprobado',
          editorial: editorial,
          isbn: isbn,
          paginas: paginas,
          // Agrega otros campos relevantes según sea necesario
        });

        console.log('Monografía desaprobada:', response.data);
        // Lógica adicional si es necesario
        alert('Monografía desaprobada  con éxito');
      } catch (error) {
        console.error('Error al desaprobar la monografía:', error);
        // Manejar errores
        alert('Error al desaprobar la monografía');
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

.elim-button{
  background-color: red;
  color: white;
  border: none;
  border-radius: 10px;
  padding: 0.5rem 1rem;
  cursor: pointer;
  margin-top: 20px;
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
  