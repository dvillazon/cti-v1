<script>
import NavBar2 from '../components/NavBar2.vue';
import Aside2 from '../components/Aside2.vue';
import FormAddArticulo from '../components/FormAddArticulo.vue';

export default {
    components: {

        Aside2,
        NavBar2,
        FormAddArticulo,
        
        
    }
}
</script>

<template>
    <div class="contenedor">

        <Aside2 />
        <div class="con">
            <NavBar2 />
           <FormAddArticulo />
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