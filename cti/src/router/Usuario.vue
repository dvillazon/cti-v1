<script>
import NavBar from '../components/NavBar.vue';
import Aside from '../components/Aside.vue';
import DatosUsuario from '../components/DatosUsuario.vue';

export default {
    components: {

        Aside,
        NavBar,
        DatosUsuario,
        
        
    }
}
</script>

<template>
    <div class="contenedor">

        <Aside />
        <div class="con">
            <NavBar />
            <DatosUsuario />
        </div>

    </div>
</template>

<style>
.contenedor {
    display: flex;
}

.con {
    display: block;
}
</style>