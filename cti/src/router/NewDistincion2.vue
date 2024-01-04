<script>
import NavBar2 from '../components/NavBar2.vue';
import Aside2 from '../components/Aside2.vue';
import FromAddDistinciion from '../components/FromAddDistinciion.vue';

export default {
    components: {

        Aside2,
        NavBar2,
       FromAddDistinciion,
        
    }
}
</script>

<template>
    <div class="contenedor">

        <Aside2 />
        <div class="con">
            <NavBar2 />
            <FromAddDistinciion />
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