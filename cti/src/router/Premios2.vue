<script>
import NavBar2 from '../components/NavBar2.vue';
import Aside2 from '../components/Aside2.vue';
import AddPremio from '../components/AddPremio.vue';

export default {
    components: {

        Aside2,
        NavBar2,
        AddPremio,
        
    },
    methods: {
        navigate_ruta() {
        this.$router.push('/add_premio2');  
    },
},
}
</script>

<template>
    <div class="contenedor">

        <Aside2 />
        <div class="con">
            <NavBar2 />
            <AddPremio :navigate="navigate_ruta" />
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