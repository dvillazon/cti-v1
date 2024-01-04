<script>
import NavBar from '../components/NavBar.vue';
import Aside from '../components/Aside.vue';
import Carrusel from '../components/Carrusel.vue';
import Footer from '../components/Footer.vue';

export default {
    components: {

        Aside,
        NavBar,
        Carrusel,
        Footer,
    }
}
</script>

<template>
    <div class="contenedor">

        <Aside />
        <div class="con">
            <NavBar />
            <Carrusel />
            <Footer />
        </div>

    </div>
</template>

<style>
.contenedor {
    display: flex;
}

.con {
    display: block;
    margin-left: 15rem;
}
</style>