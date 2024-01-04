<script>
import NavBar from '../components/NavBar.vue';
import Aside from '../components/Aside.vue';
import Dat_curriculo from '../components/Dat_curriculo.vue';

export default {
    components: {

        Aside,
        NavBar,
        Dat_curriculo,
        
    }
}
</script>

<template>
    <div class="contenedor">

        <Aside />
        <div class="con">
            <NavBar />
            <Dat_curriculo />
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