<template>
  <div class="investigadores-list">
    <h1>Lista de Investigadores</h1>
    <div class="filters">
      <label v-if="userRole === '2'">Filtrar por facultad</label>
      <select v-if="userRole === '2'" v-model="selectedFaculty" @change="obtener" class="select-style">
        <option value="" disabled selected>Filtrar por facultad</option>
        <option v-for="faculty in faculties" :key="faculty.id" :value="faculty.id">
          Filtrar por facultad - {{ faculty.nombre }}
        </option>
      </select>
      
      <label v-if="userRole === '3' || userRole === '2'">Filtrar por departamento</label>
      <select v-if="userRole === '3' || userRole === '2'" v-model="selectedDepartment" @change="fetchUsers" class="select-style">
        <option value="" disabled selected>Filtrar por departamento</option>
        <option v-for="department in departments" :key="department.id" :value="department.id">
          {{ department.nombre }}
        </option>
      </select>

    </div>
    <ul class="investigador-list">
      <li v-for="investigador in filteredInvestigadores" :key="investigador.id"
        @click="seleccionarInvestigador(investigador.id)">
        <div class="investigador-name">{{ investigador.nombre}}</div>
        <div class="investigador-apellido">{{ investigador.apellidos}}</div>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      searchQuery: '',
      selectedDepartment: "",
      selectedFaculty: "",
      selectedFacultyDepartment: "",
      investigadores: [],
      departments: [],
      faculties: [],
    };
  },
  computed: {
    filteredInvestigadores() {
      let filtered = this.investigadores;

      if (this.searchQuery) {
        filtered = filtered.filter(investigador =>
          investigador.nombre.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
      }

      return filtered;
    },
    userRole() {
      const userData = JSON.parse(localStorage.getItem('userData'))
      return userData.role
    },
  },
  
  methods: {
    obtener(){
      this.fetchUsers()
      this.fetchDepartmentsAndFaculties()
      
    },
    async fetchUsers() {
      try {
        console.log(this.selectedDepartment);
        let response;
        const userData = JSON.parse(localStorage.getItem('userData'));
        const userName = userData.username;

        if (this.userRole === '4') {
          const m = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/?nombreUsuario=${userName}`);
          // Recuperar investigadores del departamento del usuario
          response = await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${m.data[0].departamento}/write_usuariod/`);
          console.log(response);
        } else if (this.userRole === '3') {
          const m = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/?nombreUsuario=${userName}`);
          const dataD = await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${m.data[0].departamento}/`);
          const idFacult = dataD.data.facultad;
          console.log('el id de mi facultad es', idFacult);
          // Verificar si se ha seleccionado un departamento
          if (this.selectedDepartment) {
            // Recuperar investigadores del departamento seleccionado
            response = await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${this.selectedDepartment}/write_usuariod/`);
          } else {
            // Si no se ha seleccionado un departamento, obtener todos los usuarios de la facultad
            response = await axios.get(`http://127.0.0.1:8000/api/v1.0/facultad/${idFacult}/write_userf/`);
          }
        } else if (this.userRole === '2') {
          if (this.selectedFaculty) {
            // Recuperar todos los investigadores
            response = await axios.get(`http://127.0.0.1:8000/api/v1.0/facultad/${this.selectedFaculty}/write_userf/`);
            if (this.selectedDepartment) {
              response = await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${this.selectedDepartment}/write_usuariod/`);
            }
          } else {
            // Si no se ha seleccionado un departamento, obtener todos los usuarios
            response = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/`);
          }
        }

        this.investigadores = response.data;
      } catch (error) {
        console.error('Error al fetching users', error);
      }
    },
async fetchDepartmentsAndFaculties() {
      try {
        const userData = JSON.parse(localStorage.getItem('userData'));
        const userName = userData.username;
        if (this.userRole === '3') {
          const m = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/?nombreUsuario=${userName}`);
         const dataD = await axios.get(`http://127.0.0.1:8000/api/v1.0/departamento/${m.data[0].departamento}/`);
           const idFacult = dataD.data.facultad;
          const responseDepartments = await axios.get(`http://127.0.0.1:8000/api/v1.0/facultad/${idFacult}/dep_facultad/`);
          this.departments = responseDepartments.data;
        } else if (this.userRole === '2') {
          const responseFaculties = await axios.get(`http://127.0.0.1:8000/api/v1.0/facultad/`);
          this.faculties = responseFaculties.data;
          console.log('El id de la facultad seleccionada es',this.selectedFaculty)
          if (this.selectedFaculty) {
            const responseDepartments = await axios.get(`http://127.0.0.1:8000/api/v1.0/facultad/${this.selectedFaculty}/dep_facultad/`);
            this.departments = responseDepartments.data;
          }
        }
      } catch (error) {
        console.error('Error fetching departments or faculties', error);
      }
    },
    async seleccionarInvestigador(investigadorId) {
      this.$router.push({ name: 'trabajos', params: { id: investigadorId } });
    },
  },
  
  mounted() {
    this.fetchUsers();
    this.fetchDepartmentsAndFaculties();
  },
};
</script>


<style scoped>
.investigadores-list {
  margin-top: 1rem;
  width: 68rem;
  margin: 10px;
}

h1 {
  text-align: center;
  font-size: 24px;
  margin-bottom: 1rem;
}

.filters {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
}

input {
  padding: 0.5rem;
  width: 20rem;
  border: 1px solid #ccc;
  border-radius: 10px;
  margin-right: 1rem;
}

.investigador-list {
  list-style-type: none;
  padding: 0;
}

.investigador-list li {
  display: flex;
  justify-content: none;
  padding: 0.5rem 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-bottom: 0.5rem;
  background-color: #f0f0f0;
  cursor: pointer;
  
  /* Cursor de selección */
}

.investigador-list li:hover {
  background-color: #e0e0e0;
  /* Cambia el fondo al pasar el cursor */
}

.investigador-name {
  font-weight: bold;
  margin-right: 6px;
}
.investigador-apellido {
  font-weight: bold;
}
.investigador-tipos {
  color: #666;
}

.select-style {
  width: 200px;
  margin: 10px;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 10px;
}
</style>
