<template>
    <footer class="footer">
        <div class="footer-container">
            <div class="left">
                <p>Expertos de la Dirección de Ciencia, Tecnología e Innovación de la Universidad son los encargados de
                    velar por la correcta realización del proceso.</p>
            </div>
            <div class="center">
                <h4>Enlaces de Interés</h4>
                <a href="https://www.ucf.edu.cu/">Portal Universidad de Cienfuegos</a>
                <a href="https://correo.ucf.edu.cu/">Correo UCF</a>
                <a href="https://www.cienfuegos.gob.cu/es/inicio">Portal de Ciudadano Cienfuegos</a>

            </div>
            <div class="right">
                <a href="">
                    <img class="social-icon" src="../assets/facebook.jpg" alt="Facebook">
                </a>
                <a href="#">
                    <img class="social-icon" src="../assets/twiter.jpg" alt="Twitter">
                </a>
                <a href="#">
                    <img class="social-icon" src="../assets/youtube.jpg" alt="YouTube">
                </a>
            </div>
        </div>
        <div class="copy">
            &copy; 2023 Universidad de Cienfuegos. Todos Los derechos reservados
        </div>

    </footer>
</template>
  
<script>
export default {
    // No es necesario importar ninguna biblioteca para los iconos
};
</script>
  
<style scoped>
.footer {
    background-color: #dedef6;
    padding: 20px;
    margin: 10px;
    border-radius: 10px;
    border: 1px solid #afafc7;
}

.copy {
    padding: 1.5em;
    font-weight: 600;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}

.footer-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.left {
    flex: 1;
    width: 3em;
    padding: 2em;
    font-weight: 600;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}

.center {
    height: 100%;
    display: flex;
    flex-direction: column;
    margin-left: 1em;
}

.right {
    flex: 1;
    display: flex;
    justify-content: flex-end;
    padding: 3em;
    margin-left: 1em;
}

a {
    margin-top: 1em;
    margin-right: 10px;
    font-weight: 600;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}

p {
    margin-bottom: 0;
}

.social-icon {
    width: 24px;
    height: 24px;
}
</style>
  