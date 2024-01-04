<script>
import NavBar from '../components/NavBar.vue';
import Aside from '../components/Aside.vue';
import AddLibro from '../components/addlibro.vue';

export default {
    components: {

        Aside,
        NavBar,
        AddLibro,
    },
    methods: {
        navigate_ruta() {
        this.$router.push('/add_libro');  
    },
},
}
</script>

<template>
    <div class="contenedor">

        <Aside />
        <div class="con">
            <NavBar />
            <AddLibro :navigate="navigate_ruta" />
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