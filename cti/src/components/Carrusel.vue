<template>
    <div class="carousel-container">
        <div class="header">
            <div class="header-left">
                <img src="../assets/home.png" alt="Logo" />
                <h1>Sistema de Ciencia, Tecnología e Innovación</h1>
            </div>
            <div class="divider"></div>
        </div>
        
        <div class="carousel">
            <div class="slide" :class="{ active: currentIndex === 0 }">
                <img src="../assets/ciencia.jpg" alt="Ciencia" />
                <div class="slide-content">
                    <h2>Ciencia</h2>
                    <h4>Nombre genérico de las distintas ramas del saber humano, en especial las que tienen el mundo natural
                        o físico o la tecnología como materias de estudio.</h4>
                </div>
            </div>
            <div class="slide" :class="{ active: currentIndex === 1 }">
                <img src="../assets/tecnologia.jpg" alt="Tecnología" />
                <div class="slide-content">
                    <h2>Tecnología</h2>
                    <h4>Conjunto de instrumentos, recursos técnicos o procedimientos empleados en un determinado campo o
                        sector.</h4>
                </div>
            </div>
            <div class="slide" :class="{ active: currentIndex === 2 }">
                <img src="../assets/innovacion.jpg" alt="Innovación" />
                <div class="slide-content">
                    <h2>Innovación</h2>
                    <h4>Cambio que se introduce en algo y que supone una novedad.</h4>
                </div>
            </div>
        </div>
        <button class="prev" @click="prevSlide">❮</button>
        <button class="next" @click="nextSlide">❯</button>
    </div>
</template>
  
  
<script>
export default {
    data() {
        return {
            currentIndex: 0,
            totalSlides: 3, // Total de diapositivas
        };
    },
    methods: {
        prevSlide() {
            this.currentIndex = (this.currentIndex - 1 + this.totalSlides) % this.totalSlides;
        },
        nextSlide() {
            this.currentIndex = (this.currentIndex + 1) % this.totalSlides;
        },
        autoNextSlide() {
            setInterval(this.nextSlide, 5000); // Cambiar la imagen cada 5 segundos
        },
    },
    created() {
        this.autoNextSlide();
    },
};
</script>
  
<style scoped>
.carousel-container {
    border: 1px solid #afafc7;
    margin: 10px;
    text-align: center;
    padding: 20px;
    padding-left: 10rem;
    padding-right: 15rem;
    position: relative;
    background-color: #dedef6;
    border-radius: 10px;
}

.header {
    margin-bottom: 20px;
}

.header-left {
    display: flex;
    margin-left: -12em;
    align-items: center;
}

.header img {
    max-width: 60px;
    margin-right: 20px;
}

.carousel {
    display: flex;
    overflow: hidden;
    width: 100%;
    margin: 0 auto;
    position: relative;
    
}
.divider {
    height: 1px;
    background-color: black;
    width: 144%;
    margin: 10px;
    margin-left: -9rem;
  }
  
.slide {
    flex: 0 0 100%;
    text-align: center;
    padding: 20px;
    display: none;
    opacity: 0;
    transition: opacity 0.5s;
    align-items: center;
    position: relative;
    background-color: #dedef6;
}

.slide.active {
    display: flex;
    opacity: 1;
}

img {
    max-width: 100%;
    height: auto;
    align-items: center;
    margin-left: 3rem;
}

.slide-content {
    position: absolute;
    top: 37%;
    left: 50%;
    transform: translate(-50%, -50%);

    
}

h2,
p {
    margin-top: 8em;
    
    padding: 0;
    font-size: 2rem;
    color: aliceblue;
}
h2{
    margin-left: 5rem;
}
h4{
    color: aliceblue;
    margin-left: 5rem;
}
h1 {
    font-size: 2rem;
}

p {
    font-size: 1rem;
    color: #333;
    margin-top: 10px;
}

.prev,
.next {
    position: absolute;
    top: 50%;
    width: auto;
    padding: 16px;
    margin-top: -22px;
    font-weight: bold;
    font-size: 18px;
    user-select: none;
    background-color: rgba(0, 0, 0, 0.308);
    color: white;
    border: none;
    cursor: pointer;
    
}

.prev {
    left: 0;
    border-radius: 3px 0 0 3px;
}

.next {
    right: 0;
    border-radius: 0 3px 3px 0;
}

</style>
