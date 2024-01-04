import './assets/main.css'
import { createApp } from 'vue'
import { createRouter, createWebHashHistory } from "vue-router";
import App from './App.vue'
import Login from './router/Login.vue'
import Home from './router/Home.vue'
import HomeJDpto from './router/HomeJDpto.vue'
//import HomeVicedecano from './router/HomeVicedecano.vue'
//import HomeDireccionCTI from './router/HomeDireccionCTI.vue'
import Curriculo from './router/Curriculo.vue'
import Curriculo2 from './router/Curriculo2.vue'
import Usuario from './router/Usuario.vue'
import Usuario2 from './router/Usuario2.vue'
import Articulos from './router/Articulos.vue'
import Articulos2 from './router/Articulos2.vue'
import NewArticulo from './router/NewArticulo.vue'
import NewArticulo2 from './router/NewArticulo2.vue'
import Libro from './router/Libro.vue'
import Libro2 from './router/Libro2.vue'
import NewLibro from './router/NewLibro.vue'
import NewLibro2 from './router/NewLibro2.vue'
import Monografia from './router/Monografia.vue'
import NewMonografia from './router/NewMonografia.vue'
import Monografia2 from './router/Monografia2.vue'
import NewMonografia2 from './router/NewMonografia2.vue'
import Premios from './router/Premios.vue'
import NewPremio from './router/NewPremio.vue'
import Premios2 from './router/Premios2.vue'
import NewPremio2 from './router/NewPremio2.vue'
import Reconocimiento from './router/Reconocimiento.vue'
import Reconocimiento2 from './router/Reconocimiento2.vue'
import Distinciones from './router/Distinciones.vue'
import Distinciones2 from './router/Distinciones2.vue'
import NewReconocimientto from './router/NewReconocimientto.vue'
import NewReconocimientto2 from './router/NewReconocimientto2.vue'
import NewDistincion from './router/NewDistincion.vue'
import NewDistincion2 from './router/NewDistincion2.vue'
import Listar from './router/Listar.vue'
import TrabajosInvestigador from './router/TrabajosInvestigador.vue'
import Balances from './router/Balances.vue'
import Admin from './router/Admin.vue'

const routes = [
    { path: '/', component: Login },
    { path: '/home', component: Home },
    { path: '/home_trab', component: HomeJDpto},
    //{ path: '/home_vicedecano', component: HomeVicedecano},
    //{ path: '/home_dirct', component: HomeDireccionCTI},
    { path: '/curriculo', component: Curriculo },
    { path: '/curriculo2', component: Curriculo2 },
    { path: '/usuario', component: Usuario },
    { path: '/usuario2', component: Usuario2 },
    { path: '/articulo', component: Articulos },
    { path: '/articulo2', component: Articulos2 },
    { path: '/libro', component: Libro },
    { path: '/libro2', component: Libro2 },
    { path: '/add_articulo/:id?', component: NewArticulo },
    { path: '/add_articulo2/:id?', component: NewArticulo2 },
    
    { path: '/add_libro/:id?', component: NewLibro },
    { path: '/add_libro2/:id?', component: NewLibro2 },
    { path: '/monografia', component: Monografia},
    { path: '/add_monografia/:id?', component: NewMonografia},
    { path: '/monografia2', component: Monografia2},
    { path: '/add_monografia2/:id?', component: NewMonografia2},
    { path: '/premios', component: Premios },
    { path: '/add_premio/:id?', component: NewPremio},
    { path: '/premios2', component: Premios2 },
    { path: '/add_premio2/:id?', component: NewPremio2},
    { path: '/reconocimiento', component: Reconocimiento},   
    { path: '/distincon', component: Distinciones},
    { path: '/add_reconocimiento/:id?', component:NewReconocimientto },
    { path: '/add_distincion', component: NewDistincion},
    { path: '/reconocimiento2', component: Reconocimiento2},   
    { path: '/distincon2', component: Distinciones2},
    { path: '/add_reconocimiento2/:id?', component:NewReconocimientto2 },
    { path: '/add_distincion2/:id?', component: NewDistincion2},
    { path: '/listar', component: Listar},
    { path: '/trabajos/:id',
    name: 'trabajos', component: TrabajosInvestigador },
    { path: '/balances', component: Balances},
    { path: '/admin', component: Admin},
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

const app = createApp(App)

app.use(router)

app.mount('#app')
