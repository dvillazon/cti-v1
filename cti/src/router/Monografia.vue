<script>
import NavBar from '../components/NavBar.vue';
import Aside from '../components/Aside.vue';
import AddMonografia from '../components/AddMonografia.vue';

export default {
    components: {

        Aside,
        NavBar,
        AddMonografia,
    },
    methods: {
        navigate_ruta() {
            this.$router.push('/add_monografia');
        },
    },
}
</script>

<template>
    <div class="contenedor">

        <Aside />
        <div class="con">
            <NavBar />
            <AddMonografia :navigate="navigate_ruta" />
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