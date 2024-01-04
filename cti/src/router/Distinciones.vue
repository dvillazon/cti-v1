<script>
import NavBar from '../components/NavBar.vue';
import Aside from '../components/Aside.vue';
import AddDistincion from '../components/AddDistincion.vue';

export default {
    components: {

        Aside,
        NavBar,
        AddDistincion,
    },
    methods: {
        navigate_ruta() {
       this.$router.push('/add_distincion');  
   },
},
}
</script>

<template>
    <div class="contenedor">

        <Aside />
        <div class="con">
            <NavBar />
           <AddDistincion :navigate="navigate_ruta" />
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