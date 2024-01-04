<script>
import NavBar from '../components/NavBar.vue';
import Aside from '../components/Aside.vue';
import FroomAddMongrafia from '../components/FroomAddMongrafia.vue';

export default {
    components: {

        Aside,
        NavBar,
        FroomAddMongrafia,
        
    }
}
</script>

<template>
    <div class="contenedor">

        <Aside />
        <div class="con">
            <NavBar />
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