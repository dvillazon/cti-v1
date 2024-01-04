<template>
  <div class="premio-list">

    <div class="filter-box">
      
      <div class="filter">
        <label>Publicaciones:</label>
        <select v-model="selectedCategoryArticulos" @change="selectCategoryArticulos">
          <option value="all">Todo</option>
          <option value="articulo">Artículos</option>
          <option value="libro">Libros</option>
          <option value="monografia">Monografías</option>
        </select>
      </div>
      <div class="filter">
        <label>Condecoraciones:</label>
        <select v-model="selectedCategoryCondecoraciones" @change="selectCategoryCondecoraciones">
          <option value="all">Todo</option>
          <option value="premio">Premios</option>
          <option value="reconocimiento">Reconocimientos</option>
        </select>
      </div>

      <div class="filter">
        <label v-if="userRole === '2'">Filtrar por facultad</label>
        <select v-if="userRole === '2'" v-model="selectedFaculty" @change="obtener" class="select-style">
          <option value="" disabled selected>Filtrar por facultad</option>
          <option v-for="faculty in faculties" :key="faculty.id" :value="faculty.id">
             {{ faculty.nombre }}
          </option>
        </select>
      </div>
      <div class="filter">
        <label v-if="userRole === '3' || userRole === '2'">Filtrar por departamento</label>
        <select v-if="userRole === '3' || userRole === '2'" v-model="selectedDepartment" @change="obtener"
          class="select-style">
          <option value="" disabled selected>Filtrar por departamento</option>
          <option v-for="department in departments" :key="department.id" :value="department.id">
            {{ department.nombre }}
          </option>
        </select>
      </div>
      <div class="filter">
      <label>Año:</label>
      <select v-model="selectedYear" @change="obtener">
        <option value="">Todos</option>
        <option value="2000">2000</option>
        <option value="2001">2001</option>
        <option value="2002">2002</option>
        <option value="2003">2003</option>
        <option value="2004">2004</option>
        <option value="2005">2005</option>
        <option value="2006">2006</option>
        <option value="2007">2007</option>
        <option value="2008">2008</option>
        <option value="2009">2009</option>
        <option value="2010">2010</option>
        <option value="2011">2011</option>
        <option value="2012">2012</option>
        <option value="2013">2013</option>
        <option value="2014">2014</option>
        <option value="2015">2015</option>
        <option value="2016">2016</option>
        <option value="2017">2017</option>
        <option value="2018">2018</option>
        <option value="2019">2019</option>
        <option value="2020">2020</option>
        <option value="2021">2021</option>
        <option value="2022">2022</option>
        <option value="2023">2023</option>
      </select>
    </div>

      <div class="filter">
        <button @click="exportDataToPDF">Exportar Balance</button>
      </div>
    </div>

    <div class="publicaciones">
      <div class="publicacion-usuario">

        <div class="publicacion-nombre">Titulo</div>
        <div class="publicacion-tipo">Estado</div>
      </div>
    </div>

    <div class="publicaciones">
      <router-link v-for="articulo in filteredArticulos" :key="articulo.id"
        :to="{ path: getCategoryPath('articulo', articulo.id) }" class="publicacion-usuario">
        <div class="publicacion-nombre">{{ articulo.titulo }}</div>
        <div class="publicacion-tipo">{{ articulo.estado }}</div>
      </router-link>
    </div>
    <div class="publicaciones">
      <router-link v-for="libro in filteredLibros" :key="libro.id" :to="{ path: getCategoryPath('libro', libro.id) }"
        class="publicacion-usuario">
        <div class="publicacion-nombre">{{ libro.titulo }}</div>
        <div class="publicacion-tipo">{{ libro.estado }}</div>
      </router-link>
    </div>
    <div class="publicaciones">
      <router-link v-for="monografia in filteredMonografias" :key="monografia.id"
        :to="{ path: getCategoryPath('monografia', monografia.id) }" class="publicacion-usuario">
        <div class="publicacion-nombre">{{ monografia.titulo }}</div>
        <div class="publicacion-tipo">{{ monografia.estado }}</div>
      </router-link>
    </div>
    <div class="condecoraciones">
      <router-link v-for="premio in filteredPremios" :key="premio.id" :to="{ path: getCategoryPath('premio', premio.id) }"
        class="condecoracion-usuario">
        <div class="condecoracion-nombre">{{ premio.titulo_resultado }}</div>
        <div class="condecoracion-tipo">{{ premio.estado }}</div>
      </router-link>
    </div>
    <div class="condecoraciones">
      <router-link v-for="reconocimiento in filteredReconocimientos" :key="reconocimiento.id"
        :to="{ path: getCategoryPath('reconocimiento', reconocimiento.id) }" class="condecoracion-usuario">
        <div class="condecoracion-nombre">{{ reconocimiento.nombre_reconocimiento }}</div>
        <div class="condecoracion-tipo">{{ reconocimiento.estado }}</div>
      </router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import jsPDF from 'jspdf'
import 'jspdf-autotable'
export default {
  data() {
    return {
      selectedDepartment: "",
      selectedFaculty: "",
      selectedCategoryArticulos: 'all',
      selectedCategoryCondecoraciones: 'all',
      articulosUsuario: [],
      librosUsuario: [],
      monografiasUsuario: [],
      premiosUsuario: [],
      reconocimientosUsuario: [],
      searchQuery: '', // Propiedad para la búsqueda
      departments: [],
      faculties: [],
      selectedYear: "",
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

    obtener() {
      this.fetchDepartmentsAndFaculties();
      this.obtenerArticulosUsuario();
      this.obtenerLibrosUsuario();
      this.obtenerMonografiasUsuario();
      this.obtenerPremiosUsuario();
      this.obtenerReconocimientosUsuario()

    },
    async obtenerArticulosUsuario() {
  let respuesta;
  try {
    // Obtener la información del usuario desde el almacenamiento local
    const userData = JSON.parse(localStorage.getItem('userData'));
    const userName = userData.username;
    //////////////// OBTENER ID DEPARTAMENTO //////////////////////////////////////////////////
    const departamento = (await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/?nombreUsuario=${userName}`)).data[0].departamento;
    console.log('El departamento del usuario es ', departamento)
    ///////////////////OBTENER ID DE LA FACULTAD DE ESE DEPARTAMENTO /////////////////////////
    const facult = (await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${departamento}/`)).data.facultad
    console.log('El departamento del usuario es ', facult)
    // Verificar el rol del usuario
    if (this.userRole === '4') {
      // Si el usuario tiene el rol '4', obtener el departamento del usuario y luego los artículos del departamento
      respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${departamento}/write_articulod/`);
    } else if (this.userRole === '3') {
      // Si el usuario tiene el rol '3', obtener la facultad del usuario
     // const facultad = (await axios.get(`pedir/facultad/por/${userName}`)).data;

      // Verificar si se ha seleccionado un departamento
      if (this.selectedDepartment) {
        // Si se ha seleccionado un departamento, recuperar artículos del departamento seleccionado
        respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${this.selectedDepartment}/write_articulod/`);
      } else {
        // Si no se ha seleccionado un departamento, obtener todos los artículos de la facultad
        respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/facultad/${facult}/write_articulof/`);
      }
    } else if (this.userRole === '2') {
      // Si el usuario tiene el rol '2', verificar si se ha seleccionado una facultad
      if (this.selectedFaculty) {
        // Si se ha seleccionado una facultad, verificar si también se ha seleccionado un departamento
        if (this.selectedDepartment) {
          // Si se ha seleccionado un departamento, recuperar artículos del departamento seleccionado
          respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${this.selectedDepartment}/write_articulod/`);
        } else {
          // Si no se ha seleccionado un departamento, recuperar todos los artículos de la facultad
          respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/facultad/${this.selectedFaculty}/write_articulof/`);
        }
      } else {
        // Si no se ha seleccionado una facultad, obtener todos los artículos
        respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/articulo/`);
      }
    }
    if (this.selectedYear) {
      this.articulosUsuario = respuesta.data.filter(articulo => articulo.ano == this.selectedYear);
    } else {
      // Si no se selecciona un año, mostrar todos los artículos
      this.articulosUsuario = respuesta.data;
    }

    // Actualizar la propiedad 'articulosUsuario' con los datos obtenidos
    //this.articulosUsuario = respuesta.data;
  } catch (error) {
    // Manejar errores en la consola
    console.error('Error al obtener las publicaciones del usuario', error);
  }
},

async obtenerLibrosUsuario() {
  let respuesta;
  try {
    // Obtener la información del usuario desde el almacenamiento local
    const userData = JSON.parse(localStorage.getItem('userData'));
    const userName = userData.username;
     //////////////// OBTENER ID DEPARTAMENTO //////////////////////////////////////////////////
     const departamento = (await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/?nombreUsuario=${userName}`)).data[0].departamento;
   // console.log('El departamento del usuario es ', departamento)
    ///////////////////OBTENER ID DE LA FACULTAD DE ESE DEPARTAMENTO /////////////////////////
    const facult = (await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${departamento}/`)).data.facultad
    //console.log('El departamento del usuario es ', facult)
    // Verificar el rol del usuario
    if (this.userRole === '4') {
      // Si el usuario tiene el rol '4', obtener el departamento del usuario y luego los libros del departamento
     //const departamento = (await axios.get(`pedir/departamento/por/${userName}`)).data;
      respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${departamento}/write_librod/`);
    } else if (this.userRole === '3') {
      // Si el usuario tiene el rol '3', obtener la facultad del usuario
    //  const facultad = (await axios.get(`pedir/facultad/por/${userName}`)).data;

      // Verificar si se ha seleccionado un departamento
      if (this.selectedDepartment) {
        // Si se ha seleccionado un departamento, recuperar libros del departamento seleccionado
        respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${this.selectedDepartment}/write_librod/`);
      } else {
        // Si no se ha seleccionado un departamento, obtener todos los libros de la facultad
        respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/facultad/${facult}/write_librof/`);
      }
    } else if (this.userRole === '2') {
      // Si el usuario tiene el rol '2', verificar si se ha seleccionado una facultad
      if (this.selectedFaculty) {
        // Si se ha seleccionado una facultad, verificar si también se ha seleccionado un departamento
        if (this.selectedDepartment) {
          // Si se ha seleccionado un departamento, recuperar libros del departamento seleccionado
          respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${this.selectedDepartment}/write_librod/`);
        } else {
          // Si no se ha seleccionado un departamento, recuperar todos los libros de la facultad
          respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/facultad/${this.selectedFaculty}/write_librof/`);
        }
      } else {
        // Si no se ha seleccionado una facultad, obtener todos los libros
        respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/libro/`);
      }
    }
    if (this.selectedYear) {
      this.librosUsuario = respuesta.data.filter(libro => libro.ano == this.selectedYear);
    } else {
      // Si no se selecciona un año, mostrar todos los libros
      this.librosUsuario = respuesta.data;
    }
    // Actualizar la propiedad 'librosUsuario' con los datos obtenidos
    //this.librosUsuario = respuesta.data;
  } catch (error) {
    // Manejar errores en la consola
    console.error('Error al obtener los libros del usuario', error);
  }
},

async obtenerMonografiasUsuario() {
  let respuesta;
  try {
    // Obtener la información del usuario desde el almacenamiento local
    const userData = JSON.parse(localStorage.getItem('userData'));
    const userName = userData.username;
    const departamento = (await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/?nombreUsuario=${userName}`)).data[0].departamento;
    const facult = (await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${departamento}/`)).data.facultad
    // Verificar el rol del usuario
    if (this.userRole === '4') {
      respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${departamento}/write_monografiad/`);
    } else if (this.userRole === '3') {
      // Verificar si se ha seleccionado un departamento
      if (this.selectedDepartment) {
        // Si se ha seleccionado un departamento, recuperar monografías del departamento seleccionado
        respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${this.selectedDepartment}/write_monografiad/`);
      } else {
        // Si no se ha seleccionado un departamento, obtener todas las monografías de la facultad
        respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/facultad/${facult}/write_monografiaf/`);
      }
    } else if (this.userRole === '2') {
      // Si el usuario tiene el rol '2', verificar si se ha seleccionado una facultad
      if (this.selectedFaculty) {
        // Si se ha seleccionado una facultad, verificar si también se ha seleccionado un departamento
        if (this.selectedDepartment) {
          // Si se ha seleccionado un departamento, recuperar monografías del departamento seleccionado
          respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${this.selectedDepartment}/write_monografiad/`);
        } else {
          respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/facultad/${this.selectedFaculty}/write_monografiaf/`);
        }
      } else {
        // Si no se ha seleccionado una facultad, obtener todas las monografías
        respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/monografia/`);
      }
    }
    if (this.selectedYear) {
      this.monografiasUsuario = respuesta.data.filter(monografia => monografia.ano == this.selectedYear);
    } else {
      // Si no se selecciona un año, mostrar todas las monografías
      this.monografiasUsuario = respuesta.data;
    }
    // Actualizar la propiedad 'monografiasUsuario' con los datos obtenidos
    //this.monografiasUsuario = respuesta.data;
  } catch (error) {
    // Manejar errores en la consola
    console.error('Error al obtener las monografías del usuario', error);
  }
},


async obtenerPremiosUsuario() {
  let respuesta;
  try {
    // Obtener la información del usuario desde el almacenamiento local
    const userData = JSON.parse(localStorage.getItem('userData'));
    const userName = userData.username;
    const departamento = (await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/?nombreUsuario=${userName}`)).data[0].departamento;
    const facult = (await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${departamento}/`)).data.facultad
    // Verificar el rol del usuario
    if (this.userRole === '4') {
      // Si el usuario tiene el rol '4', obtener el departamento del usuario y luego los premios del departamento
      respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${departamento}/write_premiod/`);
    } else if (this.userRole === '3') {
      // Verificar si se ha seleccionado un departamento
      if (this.selectedDepartment) {
        // Si se ha seleccionado un departamento, recuperar premios del departamento seleccionado
        respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${this.selectedDepartment}/write_premiod/`);
      } else {
        // Si no se ha seleccionado un departamento, obtener todos los premios de la facultad
        respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/facultad/${facult}/write_premiof/`);
      }
    } else if (this.userRole === '2') {
      // Si el usuario tiene el rol '2', verificar si se ha seleccionado una facultad
      if (this.selectedFaculty) {
        // Si se ha seleccionado una facultad, verificar si también se ha seleccionado un departamento
        if (this.selectedDepartment) {
          // Si se ha seleccionado un departamento, recuperar premios del departamento seleccionado
          respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${this.selectedDepartment}/write_premiod/`);
        } else {
          // Si no se ha seleccionado un departamento, recuperar todos los premios de la facultad
          respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/facultad/${this.selectedFaculty}/write_premiof/`);
        }
      } else {
        // Si no se ha seleccionado una facultad, obtener todos los premios
        respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/premio/`);
      }
    }
    if (this.selectedYear) {
      this.premiosUsuario = respuesta.data.filter(premio => {
        // Obtener el año de la fecha del premio
        const anoPremio = new Date(premio.fecha).getFullYear();
        return anoPremio.toString() == this.selectedYear;
      });
    } else {
      // Si no se selecciona un año, mostrar todos los premios
      this.premiosUsuario = respuesta.data;
    }
    // Actualizar la propiedad 'premiosUsuario' con los datos obtenidos
   // this.premiosUsuario = respuesta.data;
  } catch (error) {
    // Manejar errores en la consola
    console.error('Error al obtener los premios del usuario', error);
  }
},


async obtenerReconocimientosUsuario() {
  let respuesta;
  try {
    // Obtener la información del usuario desde el almacenamiento local
    const userData = JSON.parse(localStorage.getItem('userData'));
    const userName = userData.username;
    const departamento = (await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/?nombreUsuario=${userName}`)).data[0].departamento;
    const facult = (await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${departamento}/`)).data.facultad
    // Verificar el rol del usuario
    if (this.userRole === '4') {
      // Si el usuario tiene el rol '4', obtener el departamento del usuario y luego los reconocimientos del departamento
      respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${departamento}/write_reconocimientod/`);
    } else if (this.userRole === '3') {
      // Verificar si se ha seleccionado un departamento
      if (this.selectedDepartment) {
        // Si se ha seleccionado un departamento, recuperar reconocimientos del departamento seleccionado
        respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${this.selectedDepartment}/write_reconocimientod/`);
      } else {
        // Si no se ha seleccionado un departamento, obtener todos los reconocimientos de la facultad
        respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/facultad/${facult}/write_reconocimientof/`);
      }
    } else if (this.userRole === '2') {
      // Si el usuario tiene el rol '2', verificar si se ha seleccionado una facultad
      if (this.selectedFaculty) {
        // Si se ha seleccionado una facultad, verificar si también se ha seleccionado un departamento
        if (this.selectedDepartment) {
          // Si se ha seleccionado un departamento, recuperar reconocimientos del departamento seleccionado
          respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${this.selectedDepartment}/write_reconocimientod/`);
        } else {
          // Si no se ha seleccionado un departamento, recuperar todos los reconocimientos de la facultad
          respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/facultad/${this.selectedFaculty}/write_reconocimientof/`);
        }
      } else {
        // Si no se ha seleccionado una facultad, obtener todos los reconocimientos
        respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/reconocimiento/`);
      }
    }
    if (this.selectedYear) {
      this.reconocimientosUsuario = respuesta.data.filter(reconocimiento => {
        // Obtener el año de la fecha del premio
        const anoR = new Date(reconocimiento.fecha).getFullYear();
        return anoR.toString() == this.selectedYear;
      });
    } else {
      // Si no se selecciona un año, mostrar todos los premios
      this.reconocimientosUsuario = respuesta.data;
    }
    // Actualizar la propiedad 'reconocimientosUsuario' con los datos obtenidos
   // this.reconocimientosUsuario = respuesta.data;
  } catch (error) {
    // Manejar errores en la consola
    console.error('Error al obtener los reconocimientos del usuario', error);
  }
},

    async fetchDepartmentsAndFaculties() {
      try {
        const userData = JSON.parse(localStorage.getItem('userData'));
        const userName = userData.username;
        const departamento = (await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/?nombreUsuario=${userName}`)).data[0].departamento;
        const facult = (await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${departamento}/`)).data.facultad
        if (this.userRole === '3') {
          const responseDepartments = await axios.get(`http://127.0.0.1:8000/api/v1.0/facultad/${facult}/dep_facultad/`);
          this.departments = responseDepartments.data;
          console.log('los departamentos de mi facultad son', this.departments)

        } else if (this.userRole === '2') {
          const responseFaculties = await axios.get(`http://127.0.0.1:8000/api/v1.0/facultad/`);
          this.faculties = responseFaculties.data;

          if (this.selectedFaculty) {
            console.log(this.selectedFaculty);
            const responseDepartments = await axios.get(`http://127.0.0.1:8000/api/v1.0/facultad/${this.selectedFaculty}/dep_facultad/`);
            this.departments = responseDepartments.data;

          }
        }
      } catch (error) {
        console.error('Error fetching departments or faculties', error);
      }
    },

    getCategoryPath(category, id) {
      const userData = JSON.parse(localStorage.getItem('userData'));
      const userROl = userData.role;
      if (userROl === '5') {
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
    async exportDataToPDF() {
      try {
        const userData = JSON.parse(localStorage.getItem('userData'));
        const userName = userData.username;
        const m = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/?nombreUsuario=${userName}`);
        const d = m.data[0].departamento
        if(this.userRole === '4'){
        const response = await axios.get(`http://localhost:8000/api/v1.0/departamento/${d}/write_articulod/`);
        const articles = response.data; // Supongamos que la respuesta contiene los artículos
        const responseL = await axios.get(`http://localhost:8000/api/v1.0/departamento/${d}/write_librod/`);
        const libro = responseL.data
        const responsem = await axios.get(`http://localhost:8000/api/v1.0/departamento/${d}/write_monografiad/`);
        const monografias = responsem.data
       // const responsep = await axios.get(`http://localhost:8000/api/v1.0/departamento/${d}/write_premiod/`);
        //const premios = responsep.data
       // const responser = await axios.get(`http://localhost:8000/api/v1.0/departamento/${d}/write_reconocimientod/`);
       // const reconocimientos = responser.data
      
        //////////////////////////////OBTENER NOMBRE DE AUTORES /////////////////////////////////////////////////
        const getAuthorName = async (authorId) => {
          try {
            const authorResponse = await axios.get(`http://localhost:8000/api/v1.0/usuario/${authorId}/`);
            return authorResponse.data.nombre; // Suponiendo que el nombre del autor está en 'nombre'
          } catch (error) {
            console.error(`Error al obtener nombre del autor con ID ${authorId}:`, error);
            return 'Nombre no encontrado'; // Manejo de error o mensaje por defecto
          }
        };

        ////////////////////////////////////////////Articulo/////////////////////////////////////////////////////////
        const data = await Promise.all(articles.map(async (article) => {
          let grupo = '';
          if (article.bd_referenciada === 'Scopus') {
            grupo = '1';
          } else if (article.bd_referenciada === 'SciELO' || article.bd_referenciada === 'Emerging Science CitationScielo' || article.bd_referenciada === 'Chemical Abstract (CA)') {
            grupo = '2';
          }else if (article.bd_referenciada === 'REDALYC' || article.bd_referenciada === 'DOAJ (Directory of Open Access Journals)' || article.bd_referenciada === 'PERIÓDICA') {
            grupo = '3';
          }else if (article.bd_referenciada === 'Revistas Nacionales Acreditadas por CITMA' || article.bd_referenciada === 'Revistas Extranjeras Arbitradas') {
            grupo = '4';
          }

          const authors = await Promise.all(article.autores.map(async (authorId) => {
            const authorName = await getAuthorName(authorId);
            return authorName;
          }));

          return [
            grupo,
            article.titulo,
            authors.join(', '),
            article.ano,
            article.bd_referenciada,
            article.pais,
            article.link,
            article.issn,
            article.titulo_revista,
            article.factor_impacto
          ];
        }));

        // Crear un nuevo documento PDF
        const pdf = new jsPDF();
        const header = ['Grupo','Título', 'Autores', 'Año', 'Base de Datos', 'País', 'URL', 'ISSN', 'Revista','Factor Impacto']; // Encabezados de la tabla

        // Configurar el ancho de las columnas
        const columnStyles = {
          0: { columnWidth: 14 }, // Ancho de la quinta columna (Grupo)
          1: { columnWidth: 30 }, // Ancho de la primera columna (Título)
          2: { columnWidth: 25 }, // Ancho de la segunda columna (Autores)
          3: { columnWidth: 15 }, // Ancho de la tercera columna (Año)
          4: { columnWidth: 20 }, // Ancho de la cuarta columna (Base de Datos)
          5: { columnWidth: 15 }, // Ancho de la sexta columna (País)
          6: { columnWidth: 22 }, // Ancho de la séptima columna (URL)
          7: { columnWidth: 20 }, // Ancho de la octava columna (ISSN)
          8: { columnWidth: 20 }, // Ancho de la novena columna (Revista)
          9: { columnWidth: 25 }, // Ancho de la décima columna (Factor de Impacto)
        };

        // Agregar la tabla al PDF
        pdf.setFontSize(18);
        pdf.text('Tabla de Artículos', 14, 15);
        pdf.autoTable({
          startY: 20,
          head: [header],
          body: data,
          startY: 20,
          margin: { top: 20 , left:1 ,right:1},
          columnStyles: columnStyles,
          didDrawCell: (data) => {
            if (data.row.index % 2 === 0) {
              data.cell.styles.fillColor = '#f3f3f3';
            }
          }
        });
        ///////////////////////////////////////////////////////////////////////LIBRO////////////////////
        const dataLibro = await Promise.all(libro.map(async (libros) => {
          let grupo = '';
          if (libros.editorial === 'Book Citacion Index') {
            grupo = '1';
          } else if (libros.editorial === 'Scielo Libros' || libros.editorial === 'SPI' || libros.editorial === 'Publishers Scholar Metrics') {
            grupo = '2';
          }else if (libros.editorial === 'Referencias Nacional') {
            grupo = '3';
          }
          const authors = await Promise.all(libros.autores.map(async (authorId) => {
            const authorName = await getAuthorName(authorId);
            return authorName;
          }));

          return [
            grupo,
            libros.titulo,
            authors.join(', '),
            libros.ano,
            libros.pais,
            libros.link,
            libros.area,
            libros.editorial,
            libros.paginas,
            libros.isbn, 
          ];
        }));
        const headerLibros = ['Grupo','Título', 'Autores', 'Año', 'Pais', 'Url', 'Area', 'Editorial','Páginas','ISBN'];
        const columnStylesLibro = {
          0: { columnWidth: 14 }, // Ancho de la quinta columna (Grupo)
          1: { columnWidth: 30 }, // Ancho de la primera columna (Título)
          2: { columnWidth: 25 }, // Ancho de la segunda columna (Autores)
          3: { columnWidth: 15 }, // Ancho de la tercera columna (Año)
          4: { columnWidth: 20 }, // Ancho de la cuarta columna (Base de Datos)
          5: { columnWidth: 15 }, // Ancho de la sexta columna (País)
          6: { columnWidth: 22 }, // Ancho de la séptima columna (URL)
          7: { columnWidth: 20 }, // Ancho de la octava columna (ISSN)
          8: { columnWidth: 20 }, // Ancho de la novena columna (Revista)
          9: { columnWidth: 25 }, // Ancho de la décima columna (Factor de Impacto)
        };
        pdf.setFontSize(18);
        const finalYArticulos = pdf.autoTable.previous.finalY;
        pdf.text('Tabla de Libros', 14, finalYArticulos + 15);
        // Espacio adicional entre las dos tablas
         const espacioEntreTablas = 20;

        // Calcular la posición inicial Y para la tabla de libros
        const startYLibros = finalYArticulos + espacioEntreTablas;

  // Agregar la tabla de libros al PDF
      pdf.autoTable({
      startY: startYLibros,
      head: [headerLibros],
      body: dataLibro,
      margin: { top: 20, left: 1, right: 1 },
      columnStyles: columnStylesLibro,
      didDrawCell: (data) => {
        if (data.row.index % 2 === 0) {
          data.cell.styles.fillColor = '#f3f3f3';
        }
       }
    });
    //////////////////////////////monografia//////////////////////////////////////////////////////
    const dataMonografia = await Promise.all(monografias.map(async (monografia) => {
      
          const authors = await Promise.all(monografia.autores.map(async (authorId) => {
            const authorName = await getAuthorName(authorId);
            return authorName;
          }));

          return [
            monografia.titulo,
            authors.join(', '),
            monografia.ano,
            monografia.pais,
            monografia.link,
            monografia.area,
            monografia.editorial,
            monografia.paginas,
            monografia.isbn,

            
          ];
        }));
        const headerMonografia = ['Título', 'Autores', 'Año', 'Pais', 'Url', 'Area', 'Editorial','Páginas','ISBN'];
        const columnStylesM = {
          0: { columnWidth: 30 }, // Ancho de la primera columna (Título)
          1: { columnWidth: 25 }, // Ancho de la segunda columna (Autores)
          2: { columnWidth: 15 }, // Ancho de la tercera columna (Año)
          3: { columnWidth: 20 }, // Ancho de la cuarta columna (Base de Datos)
          4: { columnWidth: 15 }, // Ancho de la sexta columna (País)
          5: { columnWidth: 22 }, // Ancho de la séptima columna (URL)
          6: { columnWidth: 20 }, // Ancho de la octava columna (ISSN)
          7: { columnWidth: 20 }, // Ancho de la novena columna (Revista)
          8: { columnWidth: 25 }, // Ancho de la décima columna (Factor de Impacto)
        };
        pdf.setFontSize(18);
        const finallibro = pdf.autoTable.previous.finalY;
        pdf.text('Tabla de Monografías', 14, finallibro + 15);
         const espacioEntret = 20;
        const startYMonog = finallibro + espacioEntret;
      pdf.autoTable({
      startY: startYMonog,
      head: [headerMonografia],
      body: dataMonografia,
      margin: { top: 20, left: 1, right: 1 },
      columnStyles: columnStylesM,
      didDrawCell: (data) => {
        if (data.row.index % 2 === 0) {
          data.cell.styles.fillColor = '#f3f3f3';
        }
       }
    });
        // Guardar el archivo PDF
        pdf.save('Resumen Anexo#1.pdf');
  }else if(this.userRole === '3'){
        const facult = (await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${d}/`)).data.facultad
        const response = await axios.get(`http://localhost:8000/api/v1.0/facultad/${facult}/write_articulof/`);
        const articles = response.data; // Supongamos que la respuesta contiene los artículos
        const responseL = await axios.get(`http://localhost:8000/api/v1.0/facultad/${facult}/write_librof/`);
        const libro = responseL.data
        const responsem = await axios.get(`http://localhost:8000/api/v1.0/facultad/${facult}/write_monografiaf/`);
        const monografias = responsem.data
        //const responsep = await axios.get(`http://localhost:8000/api/v1.0/departamento/${d}/write_premiod/`);
       // const premios = responsep.data
        //const responser = await axios.get(`http://localhost:8000/api/v1.0/departamento/${d}/write_reconocimientod/`);
       // const reconocimientos = responser.data
      
        //////////////////////////////OBTENER NOMBRE DE AUTORES /////////////////////////////////////////////////
        const getAuthorName = async (authorId) => {
          try {
            const authorResponse = await axios.get(`http://localhost:8000/api/v1.0/usuario/${authorId}/`);
            return authorResponse.data.nombre; // Suponiendo que el nombre del autor está en 'nombre'
          } catch (error) {
            console.error(`Error al obtener nombre del autor con ID ${authorId}:`, error);
            return 'Nombre no encontrado'; // Manejo de error o mensaje por defecto
          }
        };

        ////////////////////////////////////////////Articulo/////////////////////////////////////////////////////////
        const data = await Promise.all(articles.map(async (article) => {
          let grupo = '';
          if (article.bd_referenciada === 'Scopus') {
            grupo = '1';
          } else if (article.bd_referenciada === 'SciELO' || article.bd_referenciada === 'Emerging Science CitationScielo' || article.bd_referenciada === 'Chemical Abstract (CA)') {
            grupo = '2';
          }else if (article.bd_referenciada === 'REDALYC' || article.bd_referenciada === 'DOAJ (Directory of Open Access Journals)' || article.bd_referenciada === 'PERIÓDICA') {
            grupo = '3';
          }else if (article.bd_referenciada === 'Revistas Nacionales Acreditadas por CITMA' || article.bd_referenciada === 'Revistas Extranjeras Arbitradas') {
            grupo = '4';
          }

          const authors = await Promise.all(article.autores.map(async (authorId) => {
            const authorName = await getAuthorName(authorId);
            return authorName;
          }));

          return [
            grupo,
            article.titulo,
            authors.join(', '),
            article.ano,
            article.bd_referenciada,
            article.pais,
            article.link,
            article.issn,
            article.titulo_revista,
            article.factor_impacto
          ];
        }));

        // Crear un nuevo documento PDF
        const pdf = new jsPDF();
        const header = ['Grupo','Título', 'Autores', 'Año', 'Base de Datos', 'País', 'URL', 'ISSN', 'Revista','Factor Impacto']; // Encabezados de la tabla

        // Configurar el ancho de las columnas
        const columnStyles = {
          0: { columnWidth: 14 }, // Ancho de la quinta columna (Grupo)
          1: { columnWidth: 30 }, // Ancho de la primera columna (Título)
          2: { columnWidth: 25 }, // Ancho de la segunda columna (Autores)
          3: { columnWidth: 15 }, // Ancho de la tercera columna (Año)
          4: { columnWidth: 20 }, // Ancho de la cuarta columna (Base de Datos)
          5: { columnWidth: 15 }, // Ancho de la sexta columna (País)
          6: { columnWidth: 22 }, // Ancho de la séptima columna (URL)
          7: { columnWidth: 20 }, // Ancho de la octava columna (ISSN)
          8: { columnWidth: 20 }, // Ancho de la novena columna (Revista)
          9: { columnWidth: 25 }, // Ancho de la décima columna (Factor de Impacto)
        };

        // Agregar la tabla al PDF
        pdf.setFontSize(18);
        pdf.text('Tabla de Artículos', 14, 15);
        pdf.autoTable({
          startY: 20,
          head: [header],
          body: data,
          startY: 20,
          margin: { top: 20 , left:1 ,right:1},
          columnStyles: columnStyles,
          didDrawCell: (data) => {
            if (data.row.index % 2 === 0) {
              data.cell.styles.fillColor = '#f3f3f3';
            }
          }
        });
        ///////////////////////////////////////////////////////////////////////LIBRO////////////////////
        const dataLibro = await Promise.all(libro.map(async (libros) => {
          let grupo = '';
          if (libros.editorial === 'Book Citacion Index') {
            grupo = '1';
          } else if (libros.editorial === 'Scielo Libros' || libros.editorial === 'SPI' || libros.editorial === 'Publishers Scholar Metrics') {
            grupo = '2';
          }else if (libros.editorial === 'Referencias Nacional') {
            grupo = '3';
          }
          const authors = await Promise.all(libros.autores.map(async (authorId) => {
            const authorName = await getAuthorName(authorId);
            return authorName;
          }));

          return [
            grupo,
            libros.titulo,
            authors.join(', '),
            libros.ano,
            libros.pais,
            libros.link,
            libros.area,
            libros.editorial,
            libros.paginas,
            libros.isbn, 
          ];
        }));
        const headerLibros = ['Grupo','Título', 'Autores', 'Año', 'Pais', 'Url', 'Area', 'Editorial','Páginas','ISBN'];
        const columnStylesLibro = {
          0: { columnWidth: 14 }, // Ancho de la quinta columna (Grupo)
          1: { columnWidth: 30 }, // Ancho de la primera columna (Título)
          2: { columnWidth: 25 }, // Ancho de la segunda columna (Autores)
          3: { columnWidth: 15 }, // Ancho de la tercera columna (Año)
          4: { columnWidth: 20 }, // Ancho de la cuarta columna (Base de Datos)
          5: { columnWidth: 15 }, // Ancho de la sexta columna (País)
          6: { columnWidth: 22 }, // Ancho de la séptima columna (URL)
          7: { columnWidth: 20 }, // Ancho de la octava columna (ISSN)
          8: { columnWidth: 20 }, // Ancho de la novena columna (Revista)
          9: { columnWidth: 25 }, // Ancho de la décima columna (Factor de Impacto)
        };
        pdf.setFontSize(18);
        const finalYArticulos = pdf.autoTable.previous.finalY;
        pdf.text('Tabla de Libros', 14, finalYArticulos + 15);
        // Espacio adicional entre las dos tablas
         const espacioEntreTablas = 20;

        // Calcular la posición inicial Y para la tabla de libros
        const startYLibros = finalYArticulos + espacioEntreTablas;

  // Agregar la tabla de libros al PDF
      pdf.autoTable({
      startY: startYLibros,
      head: [headerLibros],
      body: dataLibro,
      margin: { top: 20, left: 1, right: 1 },
      columnStyles: columnStylesLibro,
      didDrawCell: (data) => {
        if (data.row.index % 2 === 0) {
          data.cell.styles.fillColor = '#f3f3f3';
        }
       }
    });
    //////////////////////////////monografia//////////////////////////////////////////////////////
    const dataMonografia = await Promise.all(monografias.map(async (monografia) => {
      
          const authors = await Promise.all(monografia.autores.map(async (authorId) => {
            const authorName = await getAuthorName(authorId);
            return authorName;
          }));

          return [
            monografia.titulo,
            authors.join(', '),
            monografia.ano,
            monografia.pais,
            monografia.link,
            monografia.area,
            monografia.editorial,
            monografia.paginas,
            monografia.isbn,

            
          ];
        }));
        const headerMonografia = ['Título', 'Autores', 'Año', 'Pais', 'Url', 'Area', 'Editorial','Páginas','ISBN'];
        const columnStylesM = {
          0: { columnWidth: 30 }, // Ancho de la primera columna (Título)
          1: { columnWidth: 25 }, // Ancho de la segunda columna (Autores)
          2: { columnWidth: 15 }, // Ancho de la tercera columna (Año)
          3: { columnWidth: 20 }, // Ancho de la cuarta columna (Base de Datos)
          4: { columnWidth: 15 }, // Ancho de la sexta columna (País)
          5: { columnWidth: 22 }, // Ancho de la séptima columna (URL)
          6: { columnWidth: 20 }, // Ancho de la octava columna (ISSN)
          7: { columnWidth: 20 }, // Ancho de la novena columna (Revista)
          8: { columnWidth: 25 }, // Ancho de la décima columna (Factor de Impacto)
        };
        pdf.setFontSize(18);
        const finallibro = pdf.autoTable.previous.finalY;
        pdf.text('Tabla de Monografías', 14, finallibro + 15);
         const espacioEntret = 20;
        const startYMonog = finallibro + espacioEntret;
      pdf.autoTable({
      startY: startYMonog,
      head: [headerMonografia],
      body: dataMonografia,
      margin: { top: 20, left: 1, right: 1 },
      columnStyles: columnStylesM,
      didDrawCell: (data) => {
        if (data.row.index % 2 === 0) {
          data.cell.styles.fillColor = '#f3f3f3';
        }
       }
    });
        // Guardar el archivo PDF
        pdf.save('Resumen Anexo#1.pdf');
  }else if(this.userRole === '2'){
       // const facult = (await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${d}/`)).data.facultad
        const response = await axios.get(`http://localhost:8000/api/v1.0/articulo/`);
        const articles = response.data; // Supongamos que la respuesta contiene los artículos
        const responseL = await axios.get(`http://localhost:8000/api/v1.0/libro/`);
        const libro = responseL.data
        const responsem = await axios.get(`http://localhost:8000/api/v1.0/monografia/`);
        const monografias = responsem.data
       // const responsep = await axios.get(`http://localhost:8000/api/v1.0/departamento/${d}/write_premiod/`);
       // const premios = responsep.data
       // const responser = await axios.get(`http://localhost:8000/api/v1.0/departamento/${d}/write_reconocimientod/`);
       // const reconocimientos = responser.data
      
        //////////////////////////////OBTENER NOMBRE DE AUTORES /////////////////////////////////////////////////
        const getAuthorName = async (authorId) => {
          try {
            const authorResponse = await axios.get(`http://localhost:8000/api/v1.0/usuario/${authorId}/`);
            return authorResponse.data.nombre; // Suponiendo que el nombre del autor está en 'nombre'
          } catch (error) {
            console.error(`Error al obtener nombre del autor con ID ${authorId}:`, error);
            return 'Nombre no encontrado'; // Manejo de error o mensaje por defecto
          }
        };

        ////////////////////////////////////////////Articulo/////////////////////////////////////////////////////////
        const data = await Promise.all(articles.map(async (article) => {
          let grupo = '';
          if (article.bd_referenciada === 'Scopus') {
            grupo = '1';
          } else if (article.bd_referenciada === 'SciELO' || article.bd_referenciada === 'Emerging Science CitationScielo' || article.bd_referenciada === 'Chemical Abstract (CA)') {
            grupo = '2';
          }else if (article.bd_referenciada === 'REDALYC' || article.bd_referenciada === 'DOAJ (Directory of Open Access Journals)' || article.bd_referenciada === 'PERIÓDICA') {
            grupo = '3';
          }else if (article.bd_referenciada === 'Revistas Nacionales Acreditadas por CITMA' || article.bd_referenciada === 'Revistas Extranjeras Arbitradas') {
            grupo = '4';
          }

          const authors = await Promise.all(article.autores.map(async (authorId) => {
            const authorName = await getAuthorName(authorId);
            return authorName;
          }));

          return [
            grupo,
            article.titulo,
            authors.join(', '),
            article.ano,
            article.bd_referenciada,
            article.pais,
            article.link,
            article.issn,
            article.titulo_revista,
            article.factor_impacto
          ];
        }));

        // Crear un nuevo documento PDF
        const pdf = new jsPDF();
        const header = ['Grupo','Título', 'Autores', 'Año', 'Base de Datos', 'País', 'URL', 'ISSN', 'Revista','Factor Impacto']; // Encabezados de la tabla

        // Configurar el ancho de las columnas
        const columnStyles = {
          0: { columnWidth: 14 }, // Ancho de la quinta columna (Grupo)
          1: { columnWidth: 30 }, // Ancho de la primera columna (Título)
          2: { columnWidth: 25 }, // Ancho de la segunda columna (Autores)
          3: { columnWidth: 15 }, // Ancho de la tercera columna (Año)
          4: { columnWidth: 20 }, // Ancho de la cuarta columna (Base de Datos)
          5: { columnWidth: 15 }, // Ancho de la sexta columna (País)
          6: { columnWidth: 22 }, // Ancho de la séptima columna (URL)
          7: { columnWidth: 20 }, // Ancho de la octava columna (ISSN)
          8: { columnWidth: 20 }, // Ancho de la novena columna (Revista)
          9: { columnWidth: 25 }, // Ancho de la décima columna (Factor de Impacto)
        };

        // Agregar la tabla al PDF
        pdf.setFontSize(18);
        pdf.text('Tabla de Artículos', 14, 15);
        pdf.autoTable({
          startY: 20,
          head: [header],
          body: data,
          startY: 20,
          margin: { top: 20 , left:1 ,right:1},
          columnStyles: columnStyles,
          didDrawCell: (data) => {
            if (data.row.index % 2 === 0) {
              data.cell.styles.fillColor = '#f3f3f3';
            }
          }
        });
        ///////////////////////////////////////////////////////////////////////LIBRO////////////////////
        const dataLibro = await Promise.all(libro.map(async (libros) => {
          let grupo = '';
          if (libros.editorial === 'Book Citacion Index') {
            grupo = '1';
          } else if (libros.editorial === 'Scielo Libros' || libros.editorial === 'SPI' || libros.editorial === 'Publishers Scholar Metrics') {
            grupo = '2';
          }else if (libros.editorial === 'Referencias Nacional') {
            grupo = '3';
          }
          const authors = await Promise.all(libros.autores.map(async (authorId) => {
            const authorName = await getAuthorName(authorId);
            return authorName;
          }));

          return [
            grupo,
            libros.titulo,
            authors.join(', '),
            libros.ano,
            libros.pais,
            libros.link,
            libros.area,
            libros.editorial,
            libros.paginas,
            libros.isbn, 
          ];
        }));
        const headerLibros = ['Grupo','Título', 'Autores', 'Año', 'Pais', 'Url', 'Area', 'Editorial','Páginas','ISBN'];
        const columnStylesLibro = {
          0: { columnWidth: 14 }, // Ancho de la quinta columna (Grupo)
          1: { columnWidth: 30 }, // Ancho de la primera columna (Título)
          2: { columnWidth: 25 }, // Ancho de la segunda columna (Autores)
          3: { columnWidth: 15 }, // Ancho de la tercera columna (Año)
          4: { columnWidth: 20 }, // Ancho de la cuarta columna (Base de Datos)
          5: { columnWidth: 15 }, // Ancho de la sexta columna (País)
          6: { columnWidth: 22 }, // Ancho de la séptima columna (URL)
          7: { columnWidth: 20 }, // Ancho de la octava columna (ISSN)
          8: { columnWidth: 20 }, // Ancho de la novena columna (Revista)
          9: { columnWidth: 25 }, // Ancho de la décima columna (Factor de Impacto)
        };
        pdf.setFontSize(18);
        const finalYArticulos = pdf.autoTable.previous.finalY;
        pdf.text('Tabla de Libros', 14, finalYArticulos + 15);
        // Espacio adicional entre las dos tablas
         const espacioEntreTablas = 20;

        // Calcular la posición inicial Y para la tabla de libros
        const startYLibros = finalYArticulos + espacioEntreTablas;

  // Agregar la tabla de libros al PDF
      pdf.autoTable({
      startY: startYLibros,
      head: [headerLibros],
      body: dataLibro,
      margin: { top: 20, left: 1, right: 1 },
      columnStyles: columnStylesLibro,
      didDrawCell: (data) => {
        if (data.row.index % 2 === 0) {
          data.cell.styles.fillColor = '#f3f3f3';
        }
       }
    });
    //////////////////////////////monografia//////////////////////////////////////////////////////
    const dataMonografia = await Promise.all(monografias.map(async (monografia) => {
      
          const authors = await Promise.all(monografia.autores.map(async (authorId) => {
            const authorName = await getAuthorName(authorId);
            return authorName;
          }));

          return [
            monografia.titulo,
            authors.join(', '),
            monografia.ano,
            monografia.pais,
            monografia.link,
            monografia.area,
            monografia.editorial,
            monografia.paginas,
            monografia.isbn,

            
          ];
        }));
        const headerMonografia = ['Título', 'Autores', 'Año', 'Pais', 'Url', 'Area', 'Editorial','Páginas','ISBN'];
        const columnStylesM = {
          0: { columnWidth: 30 }, // Ancho de la primera columna (Título)
          1: { columnWidth: 25 }, // Ancho de la segunda columna (Autores)
          2: { columnWidth: 15 }, // Ancho de la tercera columna (Año)
          3: { columnWidth: 20 }, // Ancho de la cuarta columna (Base de Datos)
          4: { columnWidth: 15 }, // Ancho de la sexta columna (País)
          5: { columnWidth: 22 }, // Ancho de la séptima columna (URL)
          6: { columnWidth: 20 }, // Ancho de la octava columna (ISSN)
          7: { columnWidth: 20 }, // Ancho de la novena columna (Revista)
          8: { columnWidth: 25 }, // Ancho de la décima columna (Factor de Impacto)
        };
        pdf.setFontSize(18);
        const finallibro = pdf.autoTable.previous.finalY;
        pdf.text('Tabla de Monografías', 14, finallibro + 15);
         const espacioEntret = 20;
        const startYMonog = finallibro + espacioEntret;
      pdf.autoTable({
      startY: startYMonog,
      head: [headerMonografia],
      body: dataMonografia,
      margin: { top: 20, left: 1, right: 1 },
      columnStyles: columnStylesM,
      didDrawCell: (data) => {
        if (data.row.index % 2 === 0) {
          data.cell.styles.fillColor = '#f3f3f3';
        }
       }
    });
        // Guardar el archivo PDF
        pdf.save('Resumen Anexo#1.pdf');
  }
      } catch (error) {
        alert('No se puede exportar el PDF')
        console.error('Error al exportar a PDF:', error);
      }
    },


    selectCategoryArticulos() {
      this.selectedCategoryCondecoraciones = 'all';
    },
    selectCategoryCondecoraciones() {
      this.selectedCategoryArticulos = 'all';
    },
  },
  computed: {
    filteredArticulos() {
      return (
        (this.selectedCategoryArticulos === 'articulo' || this.selectedCategoryArticulos === 'all') &&
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
        (this.selectedCategoryCondecoraciones === 'premio' || this.selectedCategoryCondecoraciones === 'all') &&
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
    userRole() {
      const userData = JSON.parse(localStorage.getItem('userData'));
      return userData.role;
    },
  },
  mounted() {
    this.fetchDepartmentsAndFaculties()
    this.obtenerArticulosUsuario();
    this.obtenerLibrosUsuario();
    this.obtenerMonografiasUsuario();
    this.obtenerPremiosUsuario();
    this.obtenerReconocimientosUsuario();
  },

};
</script>



<style scoped>
.premio-list {
  margin-top: 1rem;
  width: 68rem;
  margin: 10px;
}

h1 {
  text-align: center;
  font-size: 24px;
  margin-bottom: 1rem;
}

.filters{
  display: flex;
  align-items: center;

}
button {
  padding: 0.5rem;
  width: 100%;
  border: 1px solid #ccc;
  border-radius: 10px;
  margin-top: 1.5rem;
}

select {
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 10px;
  margin-right: 1rem;
}



button:hover {
  cursor: pointer;
}

.premio-list {
  list-style-type: none;
  padding: 0;
}

.premio-list li {
  display: flex;
  justify-content: space-between;
  padding: 0.5rem 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-bottom: 0.5rem;
  background-color: #f0f0f0;
  cursor: pointer;
  /* Cursor de selección */
}

.premio-list li:hover {
  background-color: #e0e0e0;
  /* Cambia el fondo al pasar el cursor */
}

.premio-name {
  font-weight: bold;
}

.premio-tipos {
  color: #666;
}


.user-data {
  width: 78rem;
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
  justify-content: flex-start;
  margin-bottom: 20px;
  padding: 10px;
  border-radius: 10px;
}

.filter,select {
  
  padding-left: 7px;
  border-radius: 5px;

}
.filters,label {
  margin-left: 1px;
}
</style>
  