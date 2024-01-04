<script>
import NavBar from '../components/NavBar.vue';
import Aside from '../components/Aside.vue';
import AddArticulo from '../components/AddArticulo.vue';

export default {
    components: {

        Aside,
        NavBar,
        AddArticulo,
        
        
    },
    methods: {
        navigate_ruta() {

            this.$router.push('/add_articulo');
        },
    },
}
</script>

<template>
    <div class="contenedor">

        <Aside />
        <div class="con">
            <NavBar />
            <AddArticulo :navigate="navigate_ruta" />
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