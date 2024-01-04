<script>
import NavBar from '../components/NavBar.vue';
import Aside from '../components/Aside.vue';
import FromAddDistinciion from '../components/FromAddDistinciion.vue';

export default {
    components: {

        Aside,
        NavBar,
       FromAddDistinciion,
        
    }
}
</script>

<template>
    <div class="contenedor">

        <Aside />
        <div class="con">
            <NavBar />
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