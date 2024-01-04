<script>
import NavBar2 from '../components/NavBar2.vue';
import Aside2 from '../components/Aside2.vue';
import FroomAddMongrafia from '../components/FroomAddMongrafia.vue';

export default {
    components: {

        Aside2,
        NavBar2,
        FroomAddMongrafia,
        
        
    }
}
</script>

<template>
    <div class="contenedor">

        <Aside2 />
        <div class="con">
            <NavBar2 />
            <FroomAddMongrafia />
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