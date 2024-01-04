<script>
import NavBar from '../components/NavBar.vue';
import Aside from '../components/Aside.vue';
import FormAddArticulo from '../components/FormAddArticulo.vue';

export default {
    components: {

        Aside,
        NavBar,
        FormAddArticulo,
        
        
    }
}
</script>

<template>
    <div class="contenedor">

        <Aside />
        <div class="con">
            <NavBar />
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