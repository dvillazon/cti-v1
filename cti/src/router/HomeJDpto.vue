<script>
import NavBar2 from '../components/NavBar2.vue';
import Aside2 from '../components/Aside2.vue';
import Carrusel from '../components/Carrusel.vue';
import Footer from '../components/Footer.vue';

export default {
    components: {

       Aside2,
        NavBar2,
        Carrusel,
        Footer,
    }
}
</script>

<template>
    <div class="contenedor">
        <Aside2 />
        
        <div class="con">
            <NavBar2 />
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