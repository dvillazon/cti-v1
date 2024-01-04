<script>
import NavBar2 from '../components/NavBar2.vue';
import Aside2 from '../components/Aside2.vue';
import AddMonografia from '../components/AddMonografia.vue';

export default {
    components: {

        Aside2,
        NavBar2,
       AddMonografia,
        
        
    },
    methods: {
        navigate_ruta() {
       this.$router.push('/add_monografia2');  
   },
},
}
</script>

<template>
    <div class="contenedor">

        <Aside2 />
        <div class="con">
            <NavBar2 />
            <AddMonografia :navigate="navigate_ruta" />
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