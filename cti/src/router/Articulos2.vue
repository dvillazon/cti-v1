<script>
import NavBar2 from '../components/NavBar2.vue';
import Aside2 from '../components/Aside2.vue';
import AddArticulo from '../components/AddArticulo.vue';

export default {
    components: {

        Aside2,
        NavBar2,
        AddArticulo,

    },
    methods: {
        navigate_ruta() {

            this.$router.push('/add_articulo2');
        },
    },

}
</script>

<template>
    <div class="contenedor">

        <Aside2 />
        <div class="con">
            <NavBar2 />
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