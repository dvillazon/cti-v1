<template>
    <div class="user-profile">
        <div class="header">
            <img src="../assets/user2.png" alt="Icono" class="icon" />
            <h1>Mi Usuario</h1>
        </div>
        <div class="form-container">
            <form>
                <div class="form-group">
                    <label for="nombre">Nombre</label>
                    <div class="input-container">
                        <img src="../assets/ident.png" alt="Icono Nombre" class="input-icon" />
                        <input type="text" id="nombre" v-model="nombre" />

                    </div>
                </div>
                
                <div class="form-group">
                    <label for="apellido">Apellido</label>
                    <div class="input-container">
                        <img src="../assets/ident.png" alt="Icono Apellido" class="input-icon" />
                        <input type="text" id="apellidos" v-model="apellidos" />

                    </div>
                </div>
                <div class="form-group">
                    <label>Correo Electrónico</label>
                    <div class="input-container">
                        <img src="../assets/email.png" alt="Icono Correo" class="input-icon" />
                        <input type="email" id="correo" v-model="correo" />

                    </div>
                </div>
                <div class="form-group">
                    <label for="departamento">Departamento</label>
                    <div class="input-container">
                        <img src="../assets/area.png" alt="Icono Departamento" class="input-icon" />
                        <select  id="departamento" v-model="departamento">
                            <option value="">Departamento</option>
                            <option value="1">Informática</option>
                            <option value="2">Humanidades</option>
                            <option value="3">Eléctrica</option>
                            <option value="4">Industrial</option>
                            <option value="5">Cardio</option>
                            <option value="6">Agronomía</option>
                            <option value="7">Psicología</option>
                            <option value="8">Educación Infantil</option>
                            <option value="9">Contabilidad</option>
                            <option value="10">Sociología</option>
                            <option value="11">Finanzas</option>
                        </select>
                    </div>
                </div>
            </form>
        </div>
        <div class="buttons">
            <button class="modify-button" @click="modificarUsuario">Modificar</button>
            
        </div>
    </div>
</template>
  
<script>
import axios from 'axios';
export default {
    data() {
        return {
            nombre: '', 
            apellidos: '',
            correo: '',
            departamento: '',
        };
    },
   
    methods: {
        async obtenerDatosUsuario() {
            try {
                // Recuperar el objeto de usuario del localStorage
                const userData = JSON.parse(localStorage.getItem('userData'));
                // Obtener el nombre de usuario del objeto de usuario
                const userName = userData.username; //cambiar username por el nombre de tu variable de nombre de usuario
                console.log('nombre de usuario :',userData);
                // Realizar una petición al backend para obtener los datos del usuario por su ID
                const respuesta = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/?nombreUsuario=${userName}`);
                let datosUsuario = respuesta.data; // Supongamos que recibimos un objeto con los datos
                console.log(datosUsuario[0].id)
                // Asignar los datos a las variables del usuario
                this.nombre = datosUsuario[0].nombre;
                this.apellidos = datosUsuario[0].apellidos;
                this.correo = datosUsuario[0].correo;
                this.departamento = datosUsuario[0].departamento;

            } catch (error) {
                console.error('Error al obtener los datos del usuario', error);
            }
        },
        async modificarUsuario() {
            try {
                // Recuperar el objeto de usuario del localStorage
                const userData = JSON.parse(localStorage.getItem('userData'));

                // Obtener el nombre de usuario del objeto de usuario
                const userName = userData.username;
                console.log(userName)
                 //cambiar username por el nombre de tu variable de nombre de usuario
                // Suponiendo que tengas un objeto con los datos del usuario a enviar
                const datosModificados = {
                    nombre: this.nombre,
                    apellidos: this.apellidos,
                    correo: this.correo,
                    departamento: this.departamento,

                };
                const getUSER = await axios.get(`http://127.0.0.1:8000/api/v1.0/usuario/?nombreUsuario=${userName}`);
                console.log('Id del usuario :',getUSER.data[0].id)
                const respuesta = await axios.put(`http://127.0.0.1:8000/api/v1.0/usuario/${getUSER.data[0].id}/`, datosModificados);
                // Mensaje de éxito o manejo posterior
                alert('Usuario modificado con Exito ')
                console.log('Usuario modificado con éxito:', respuesta.data);
            } catch (error) {
                console.error('Error al modificar el usuario', error);
                // Manejar errores
            }
        },
    },
    created() {
        this.obtenerDatosUsuario();
    },
};
</script>
  
<style scoped>
.user-profile {
    display: flex;
    flex-direction: column;
    width: 68rem;
    align-items: center;
    padding: 20px;
    background-color: #f7f7f7;
    border: 1px solid #ddd;
    margin: 10px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.header {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
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

.form-container {
    width: 100%;
    max-width: 600px;
}

form {
    width: 100%;
}

.form-group {
    display: flex;
    flex-direction: column;
    margin-bottom: 20px;
}
.divider {
    height: 1px;
    background-color: black;
    width: 118%;
    margin: 10px;
    margin-left: -6rem;
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

.buttons {
    display: flex;
    justify-content: center;
    margin-top: 20px;
}

.modify-button {
    background-color: #007bff;
    color: white;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 10px;
    margin-right: 10px;
    cursor: pointer;
}

.refresh-button {
    background-color: #28a745;
    color: white;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 10px;
    cursor: pointer;
}
</style>
  