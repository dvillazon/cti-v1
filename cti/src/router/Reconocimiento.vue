<script>
import NavBar from '../components/NavBar.vue';
import Aside from '../components/Aside.vue';
import AddReconocimiento from '../components/AddReconocimiento.vue';

export default {
    components: {

        Aside,
        NavBar,
        AddReconocimiento,
        
    },
    methods: {
        navigate_ruta() {
        this.$router.push('/add_reconocimiento');  
    },
},
}
</script>

<template>
    <div class="contenedor">

        <Aside />
        <div class="con">
            <NavBar />
            <AddReconocimiento :navigate="navigate_ruta" />
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