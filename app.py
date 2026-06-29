from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cuenta Regresiva 16:00 + 9 minutos</title>

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Segoe UI',sans-serif;
}

body{
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    overflow:hidden;
    background:linear-gradient(-45deg,#0f172a,#1e3a8a,#312e81,#0f172a);
    background-size:400% 400%;
    animation:gradient 15s ease infinite;
}

@keyframes gradient{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

.card{
    width:90%;
    max-width:750px;
    padding:50px;
    border-radius:25px;
    text-align:center;
    background:rgba(255,255,255,.08);
    backdrop-filter:blur(15px);
    border:1px solid rgba(255,255,255,.2);
    box-shadow:0 10px 35px rgba(0,0,0,.35);
}

h1{
    color:white;
    font-size:2.7rem;
    margin-bottom:25px;
}

#timer{
    font-size:6rem;
    font-weight:bold;
    color:#00E5FF;
    text-shadow:0 0 20px rgba(0,229,255,.8);
    margin:25px 0;
}

#message{
    color:white;
    font-size:1.6rem;
}

.subtitle{
    margin-top:25px;
    color:#CBD5E1;
    font-size:1.1rem;
}

.circle{
    position:absolute;
    border-radius:50%;
    background:rgba(255,255,255,.08);
    animation:float 10s ease-in-out infinite;
}

.circle:nth-child(1){
    width:220px;
    height:220px;
    top:10%;
    left:10%;
}

.circle:nth-child(2){
    width:300px;
    height:300px;
    bottom:5%;
    right:5%;
    animation-duration:15s;
}

.circle:nth-child(3){
    width:150px;
    height:150px;
    bottom:15%;
    left:20%;
    animation-duration:12s;
}

@keyframes float{
    0%,100%{transform:translateY(0);}
    50%{transform:translateY(-30px);}
}

@media(max-width:768px){

    h1{
        font-size:2rem;
    }

    #timer{
        font-size:3.5rem;
    }

    #message{
        font-size:1.2rem;
    }

}
</style>
</head>

<body>

<div class="circle"></div>
<div class="circle"></div>
<div class="circle"></div>

<div class="card">

    <h1>⏳ CUENTA REGRESIVA</h1>

    <div id="timer">00:00:00</div>

    <div id="message">Esperando...</div>

    <div class="subtitle">
        Cuenta hasta las 16:00 + 9 minutos de tiempo adicional.
    </div>

</div>

<script>

function actualizarCuenta(){

    const ahora = new Date();

    // Objetivo principal (16:00)
    let objetivo = new Date();
    objetivo.setHours(16,0,0,0);

    // Si ya pasó el tiempo extra, reiniciar para el día siguiente
    if(ahora >= new Date(objetivo.getTime() + 9*60*1000)){
        objetivo.setDate(objetivo.getDate()+1);
    }

    const inicioExtra = objetivo;
    const finExtra = new Date(objetivo.getTime() + 9*60*1000);

    let diferencia;

    if(ahora < inicioExtra){

        // Cuenta normal
        diferencia = inicioExtra - ahora;

        document.getElementById("message").innerHTML =
            "⏳ Tiempo restante hasta las 16:00";

        document.getElementById("timer").style.color="#00E5FF";

    }
    else if(ahora < finExtra){

        // Tiempo adicional
        diferencia = finExtra - ahora;

        document.getElementById("message").innerHTML =
            "🟡 TIEMPO ADICIONAL";

        document.getElementById("timer").style.color="#FFD700";

    }
    else{

        diferencia = 0;

        document.getElementById("message").innerHTML =
            "✅ TIEMPO FINALIZADO";

        document.getElementById("timer").style.color="#00FF7F";

    }

    const horas = Math.floor(diferencia/(1000*60*60));
    const minutos = Math.floor((diferencia%(1000*60*60))/(1000*60));
    const segundos = Math.floor((diferencia%(1000*60))/1000);

    document.getElementById("timer").innerHTML =
        String(horas).padStart(2,'0') + ":" +
        String(minutos).padStart(2,'0') + ":" +
        String(segundos).padStart(2,'0');

}

actualizarCuenta();

setInterval(actualizarCuenta,1000);

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)