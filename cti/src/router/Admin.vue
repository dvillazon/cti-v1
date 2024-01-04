
<template>
  <div class="todo">
    <div class="component-left">
      <img src="../assets/uc_logo.png" alt="Logo" class="logo">
      <button @click="showUsersList" :class="{ active: activeTab === 'usersList' }">Lista de Usuarios</button>
      <button @click="navigateToLogin">Salir</button>
    </div>
    <div class="component-rigth">
      <div v-if="activeTab === 'usersList'" class="users-list">
        <h2>Listado de Usuarios</h2>
        <div class="search-filters">
          <input type="text" v-model="searchQuery" placeholder="Buscar por nombre" @input="searchUserByName" />
          <label class="fil">Filtrar por Rol</label>
          <select v-model="roleFilter" @change="filterByRole">
            <option>Filtrar por Rol</option>
            <option value='5'>Investigador</option>
            <option value="4">Jefe de Departamento</option>
            <option value="3">Vicedecano</option>
            <option value="2">Dirección de CTI</option>
            <option value="1">Administrador</option>
          </select>
        </div>
        <div class="table-row header-row">
          <div class="table-cell">Nombre</div>
          <div class="table-cell">Apellidos</div>
          <div class="table-cell">Correo</div>
          <div class="table-cell">Rol</div>
        </div>
        <ul class="user-list">
          <li v-for="usuario in userList" :key="usuario.id"
            :class="{ 'user-item': true, 'active-user': usuario === userToEdit }" @click="editUser(usuario)">
            <div class="user-logo">
              <img src="../assets/user-icon.png" alt="Usuario">
            </div>
            <div class="user-details">
              <div class="table-cell user-name">{{ usuario.nombre }}</div>
              <div class="table-cell user-apellid">{{ usuario.apellidos }}</div>
              <div class="table-cell user-info">{{ usuario.correo }}</div>
              <div class="table-cell user-role">{{ usuario.nivel }}</div>
            </div>

          </li>
        </ul>
      </div>
      <div v-if="activeTab === 'createUser'" class="create-user-form">
        <h2>{{ editingUser ? 'Modificar Usuario' : 'Crear Usuario' }}</h2>
        <form @submit.prevent="editingUser ? updateUser() : createUser()">
          <div class="form-row">
            <div class="form-group">
              <label for="nombre">Nombre Completo:</label>
              <input type="text" id="nombre" v-model="newUser.nombre" required :disabled="editingUser">
            </div>
            <div class="form-group full-width">
              <label for="nivel">Rol:</label>
              <select id="nivel" v-model="newUser.nivel">
                <option value="5">Investigador</option>
                <option value="4">Jefe de Departamento</option>
                <option value="3">Vicedecano</option>
                <option value="2">Dirección de CTI</option>
                <option value="1">Administrador</option>
              </select>
            </div>
          </div>
          <div class="form-row">
           
            <div class="form-group">
              <label for="departamento">Departamento:</label>
              <input type="text" id="departamento" v-model="newUser.departamento" required :disabled="editingUser">
            </div>
          </div>

          <div class="form-row">

          </div>
          <div class="form-row">
            <div class="form-group">
              <button type="submit">{{ 'Modificar Usuario' }}</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
  
<script>
import axios from 'axios';

export default {
  data() {
    return {
      activeTab: 'usersList',
      userList: [], // Lista de usuarios cargada desde la base de datos
      newUser: {
        nombre: '',
        departamento: '',
        nivel: ''
      },
      editingUser: false,
      userToEdit: null,
      searchQuery: '',
      roleFilter: 'Filtrar por Rol',
      originalUserList: [],
    };
  },
  computed: {
    filteredUsers() {
      let filtered = this.userList;
if (this.searchQuery) {
        filtered = filtered.filter(user =>
          user.nombre.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
      }

      if (this.roleFilter !== 'Filtrar por Rol') {
        filtered = filtered.filter(user => user.nivel === this.roleFilter);
      }

      return filtered;
    },
  },
  methods: {
    async fetchUserList() {
      try {
        const response = await axios.get( `http://localhost:8000/api/v1.0/usuario/`);
        console.log('Datos de usuarios recibidos:', response.data);
        this.userList = response.data;
        this.originalUserList = [...this.userList];
      } catch (error) {
        console.error('Error al obtener la lista de usuarios:', error);
      }
    },
    showUsersList() {
      this.activeTab = 'usersList';
      this.editingUser = false;

    },
    showCreateUserForm() {
      this.activeTab = 'createUser';
    },
    navigateToLogin() {
      this.$router.push('/');
    },

    editUser(usuario) {
      this.userToEdit = usuario;
     this.newUser = { ...usuario };
    
      this.editingUser = true;
      this.activeTab = 'createUser';
    },
    async updateUser() {
  try {
    // Obtén los datos del usuario mediante una solicitud GET
    const response = await axios.get(`http://localhost:3000/users/`);
    const datosUsuario = response.data;

    // Obtén el nombre de usuario asociado al ID seleccionado
    const usuarioSeleccionado = this.userList.find(user => user.id === this.userToEdit.id);
    const username = usuarioSeleccionado ? usuarioSeleccionado.nombreUsuario : '';

    // Encuentra los datos del usuario que coinciden con el username
    const usuarioDatos = datosUsuario.find(user => user.username === username);

    if (usuarioDatos) {
      // Realiza la solicitud PUT usando los datos del usuario
      const response1 = await axios.put(`http://localhost:3000/users/${usuarioDatos.id}/`, {
        username: username,
        password: usuarioDatos.password, 
        role: this.newUser.nivel
      });

      
        const response2 = await axios.put(`http://localhost:8000/api/v1.0/usuario/${this.userToEdit.id}/`, {
        nivel: this.newUser.nivel 
      });

      // Verifica si ambas solicitudes fueron exitosas
      if (response1.status === 200 && response2.status === 200) {
        alert('Usuario actualizado con éxito en ambas direcciones');
        this.fetchUserList();
        this.userToEdit = null;
        this.editingUser = false;
        this.activeTab = 'usersList';
      } else {
        console.error('Error en la respuesta del servidor:', response1, response2);
        alert('Hubo un problema al actualizar el usuario en al menos una de las direcciones');
      }
    } else {
      alert('No se encontraron datos para el usuario seleccionado');
    }
  } catch (error) {
    console.error('Error:', error);
    alert('Hubo un error al actualizar el usuario');
  }
},

    searchUserByName() {
      let userListCopy = [...this.originalUserList];
      if (this.searchQuery) {
        this.userList = userListCopy.filter(user =>
          user.nombre.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
      } else {
        this.userList = userListCopy;
      }
    },
    filterByRole() {
      let userListCopy = [...this.originalUserList];
      if (String(this.roleFilter) != 'Filtrar por Rol') {
        this.userList = userListCopy.filter(user => user.nivel == String(this.roleFilter));
      } else {
        this.userList = userListCopy;
      }
    },
    obb(){
      for(let i = 0 ; i < this.userList.length ; i++){
        const idD = this.userList[i].departamento
        console.log('El id del departamento es ',idD)
        this.obtenerNombreD(idD)
    }
    }
  },
  created() {
    this.fetchUserList();
  },
};
</script>
  

  
<style scoped>
.todo {
  display: flex;
  height: 100%;
  background-color: #3e5e7d;
}

.component-left {

  margin-top: 5rem;
  width: 200px;
  background-color: #3e5e7d;
  padding: 20px;
  position: fixed;
  left: 0;
  top: 0;
  bottom: 0;
  display: flex;
  flex-direction: column;

}

.component-left .logo {
  margin-top: -3rem;
  max-width: 80%;
  margin-left: 1rem;
  margin-bottom: 20px;
}

.component-left button {
  width: 11.5rem;
  margin-bottom: 10px;
  padding: 10px;
  border: none;
  background-color: transparent;
  color: white;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
  border-top-left-radius: 20px;
  border-bottom-left-radius: 20px;

}

.component-left button.active {
  background-color: aliceblue;
  color: #3e5e7d;
}

.component-rigth {
  min-height: 40rem;
  height: 100%;
  max-height: 100%;
  margin-top: 2rem;
  margin-left: 200px;
  margin-right: 20px;
  background-color: aliceblue;
  padding: 20px;
  flex: 1;
  border-radius: 20px;
  margin-bottom: 4.5rem;
}

.user-list {
  list-style-type: none;
  padding: 0;
}

.user-item {
  margin-top: 1rem;
  padding: 1rem;
  height: 4rem;


margin-bottom: 1rem;
  display: flex;
  /* Mostrar elementos internos en fila */
  position: relative;
  align-items: center;
  /* Alinear verticalmente al centro */
  border-bottom: 1px solid #ccc;
  padding: 10px;
  margin-left: 0.5rem;
}

.user-logo img {
  width: 40px;
  height: 40px;
  object-fit: contain;
  margin-right: 10px;

}

.user-details {
  flex: 1;
  /* Ocupar el espacio restante */
  display: flex;
  /* Mostrar elementos internos en fila */
  flex-direction: row;
  /* Alinear elementos internos en columna */
  margin-left: -2rem;

}

.user-name {
  font-weight: bold;

}

.user-info {
  color: #666;
  padding-left: 1rem;

  margin-right: 1rem;
  margin-bottom: 1rem;
}
.user-delete button {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
  color: red;
}

h2 {
  text-align: center;
}

.fil {
  margin: 10px;
}

.create-user-form form {
  display: flex;
  flex-direction: column;
  gap: 10px;
  max-width: 300px;
  height: 31rem;
  margin: 0 auto;
}

.create-user-form label {
  font-size: 16px;
}

.create-user-form input,
.create-user-form select {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.selfac {
  width: 12rem;
}

.create-user-form button {
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

.create-user-form button:hover {
  background-color: #0056b3;
}


.create-user-form .form-row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}

.create-user-form .form-group {
  flex: 1;
  margin-right: 10px;
  margin-top: 1rem;
}

.create-user-form .form-group.full-width {
  flex: 2;
  margin-right: 0;
}

.create-user-form .form-group:last-child {
  margin-right: 0;
}

.user-item :hover {
  cursor: pointer;
}

.table-row {
  display: flex;
  align-items: center;
  margin-top: 1rem;
  margin-right: 0.6rem;
}

.table-cell {
  flex: 1;
  padding: 0.3rem;
  text-align: center;
}

.header-row {
  font-weight: bold;
}

.search-filters {
  margin-top: 1rem;
  margin-bottom: 20px;
}

.search-filters input[type="text"],
.search-filters select {
  padding: 8px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 10px;
  margin-right: 10px;
}
</style>

    