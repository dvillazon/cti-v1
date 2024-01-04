<script>
import NavBar2 from '../components/NavBar2.vue';
import Aside2 from '../components/Aside2.vue';
import ListInvest from '../components/ListInvest.vue';


export default {
    components: {

        Aside2,
        NavBar2,
        ListInvest,
       
        
    },
    
}
</script>

<template>
    <div class="contenedor">

        <Aside2 />
        <div class="con">
            <NavBar2 />
            <ListInvest />
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