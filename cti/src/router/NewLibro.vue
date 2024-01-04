<script>
import NavBar from '../components/NavBar.vue';
import Aside from '../components/Aside.vue';
import FromAddLibro from '../components/FromAddLibro.vue';

export default {
    components: {

        Aside,
        NavBar,
        FromAddLibro,
        
        
    }
}
</script>

<template>
    <div class="contenedor">

        <Aside />
        <div class="con">
            <NavBar />
           <FromAddLibro />
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