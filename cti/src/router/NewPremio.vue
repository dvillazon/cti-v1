<script>
import NavBar from '../components/NavBar.vue';
import Aside from '../components/Aside.vue';
import FromAddPremio from '../components/FromAddPremio.vue'

export default {
    components: {

        Aside,
        NavBar,
        FromAddPremio,
        
        
    }
}
</script>

<template>
    <div class="contenedor">

        <Aside />
        <div class="con">
            <NavBar />
            <FromAddPremio />
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