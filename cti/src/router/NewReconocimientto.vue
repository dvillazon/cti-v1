<script>
import NavBar from '../components/NavBar.vue';
import Aside from '../components/Aside.vue';
import FormAddReconocimiento from '../components/FormAddReconocimiento.vue';

export default {
    components: {

        Aside,
        NavBar,
        FormAddReconocimiento,
        
        
    }
}
</script>

<template>
    <div class="contenedor">

        <Aside />
        <div class="con">
            <NavBar />
            <FormAddReconocimiento />
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