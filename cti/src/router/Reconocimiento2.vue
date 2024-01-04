<script>
import NavBar2 from '../components/NavBar2.vue';
import Aside2 from '../components/Aside2.vue';
import AddReconocimiento from '../components/AddReconocimiento.vue';

export default {
    components: {

        Aside2,
        NavBar2,
        AddReconocimiento,
        
    },
    methods: {
        navigate_ruta() {
        this.$router.push('/add_reconocimiento2');  
    },
},
}
</script>

<template>
    <div class="contenedor">

        <Aside2 />
        <div class="con">
            <NavBar2 />
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