<script>
import NavBar from '../components/NavBar.vue';
import Aside from '../components/Aside.vue';
import AddPremio from '../components/AddPremio.vue';

export default {
    components: {

        Aside,
        NavBar,
        AddPremio,
        
    },
    methods: {
        navigate_ruta() {
        this.$router.push('/add_premio');  
    },
},
}
</script>

<template>
    <div class="contenedor">

        <Aside />
        <div class="con">
            <NavBar />
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