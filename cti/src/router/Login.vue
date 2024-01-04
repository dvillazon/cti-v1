<template>
  <div class="hero">
    <div class="form-box">
      <div class="b-box">
        <img src="../assets/uc_logo.png" alt="escudo">
        <h1>CTI</h1>
      </div>
      <form id="login" class="input-group">
        <label for="user" class="label-field">Usuario:</label>
        <input id="user" v-model="user" type="text" class="input-field" placeholder="Usuario" required />
        <label for="password" class="label-field">Contraseña:</label>
        <input v-model="password" type="password" class="input-field" placeholder="Contraseña" required />
        <div class="button-container">
          <button type="button" class="submit-btn" @click="login">Acceder</button>
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
      user: '',
      password: '',
      users: [],
    };
  },
  async created() {
    // Cargar los usuarios al iniciar el componente
    try {
      const response = await axios.get('http://localhost:3000/users');
      this.users = response.data;
      console.log('Usuarios cargados:', this.users);
    } catch (error) {
      console.error('Error al cargar usuarios:', error);
    }
  },
  methods: {
    async login() {
      console.log('Intento de inicio de sesión');
      console.log('Usuario ingresado:', this.user);
      console.log('Contraseña ingresada:', this.password);

      try {
        const user = this.users.find(u => u.username === this.user);
        if (user) {
          // Verificar si la contraseña coincide
          if (user.password === this.password) {
            // Almacenar el objeto completo del usuario en el almacenamiento local
            localStorage.setItem('userData', JSON.stringify(user));
            const userData = JSON.parse(localStorage.getItem('userData'));
            const userName = userData.username;
            console.log('userData:', userData);
            console.log('userName:', userName);
            console.log(user);
            this.redirectUser(user.role);
          } else {
            alert('Credenciales inválidas');
          }
        } else {
          // Si el usuario no existe, crea un usuario investigador con las credenciales proporcionadas
          const newUser = {
            username: this.user,
            password: this.password,
            role: '5',
            // Otros datos del usuario
          };
          const newInvest = {
            nivel: '5',
            nombre: '',
            apellidos: '',
            correo: '',
            departamento: '',
            nombreUsuario: this.user,
            // Otros datos del usuario
          };
          // Persistir el nuevo usuario en la base de datos
          await axios.post('http://localhost:3000/users', newUser); //usuario del json
          await axios.post('http://127.0.0.1:8000/api/v1.0/usuario/', newInvest);// crea usuario en el modelo BD
          localStorage.setItem('userData', JSON.stringify(newUser));
          console.log(newUser);
          // Al completar el registro, redirigir al usuario a la ruta /usuario
          this.$router.push('/usuario');
        }
      } catch (error) {
        console.error('Error en el proceso de inicio de sesión:', error);
        alert('Error en el proceso de inicio de sesión');
      }
    }
    ,
    redirectUser(role) {
      switch (role) {
        case '5':
          this.$router.push('/home');
          break;
        case '4':
        case '3':
        case '2':
          this.$router.push('/home_trab');
          break;
        case '1':
          this.$router.push('/admin');
          break;
        default:
          this.$router.push('/');
      }
    },
  },
};
</script>



<style scoped>
.hero {
  background: url("../assets/uni_cienfuegos.jpg");
  background-size: cover;
  height: 100%;
  width: 100%;
  position: absolute;
  top: 0;
  left: 0;
}

.form-box {
  width: 24rem;
  height: 30rem;
  position: relative;
  margin: 6% auto;
  background: rgba(200, 252, 252, 0.6);
  padding: 5px;
  border-radius: 50px;
}

.b-box {
  width: 100px;
  height: 50px;
  margin-top: 4rem;
  position: center;
  border-radius: 30px;
}

.b-box img {
  width: 200px;
  height: 130px;
  background-size: cover;
  margin-top: -2rem;
  margin-left: 5rem;
}

h1 {
  width: 200px;
  height: 130px;
  text-align: center;

  margin-left: 5rem;
}

.input-group {
  top: 200px;
  position: absolute;
  width: 280px;
  transition: 0.5s;
}
.input-field {
  width: 100%;
  padding: 10px 0;
  margin: 10px 0;
  border-left: 0;
  border-top: 0;
  border-right: 0;
  border-bottom: 1px solid #999;
  outline: none;
  background: transparent;
  font-size: 1.3rem;
}

.label-field {
  width: 100%;
  padding: 10px 0;
  margin: 10px 0;
  border: 0;
  font-size: 1.4rem;
}

.button-container {
  display: flex;
  justify-content: center;
}

.submit-btn {
  width: 85%;
  padding: 10px 30px;
  font-size: 1rem;
  margin-top: 1.5rem;
  margin-left: 2rem;
  text-transform: uppercase;
  background: #007bff;
  color: #111;
  border: 0;
  outline: none;
  font-weight: 600;
  cursor: pointer;
  border-radius: 13px;
  text-decoration: none;
  color: inherit;
}

.submit-btn:hover {
  background: rgba(255, 255, 255, 0.2);
  color: rgba(0, 0, 0, 1);
  transition: 0.3s;
}

#login {
  margin-left: 10%;
  margin-right: 10%;
}
</style>