from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reloj Digital</title>

    <style>
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
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
            background:rgba(255,255,255,0.08);
            backdrop-filter:blur(15px);
            -webkit-backdrop-filter:blur(15px);
            border:1px solid rgba(255,255,255,0.2);
            border-radius:25px;
            padding:50px;
            text-align:center;
            box-shadow:0 8px 32px rgba(0,0,0,0.3);
            width:90%;
            max-width:700px;
        }

        h1{
            color:white;
            font-size:2.5rem;
            margin-bottom:20px;
            letter-spacing:2px;
        }

        .clock{
            color:#00e5ff;
            font-size:5rem;
            font-weight:bold;
            text-shadow:0 0 20px rgba(0,229,255,0.7);
            margin:20px 0;
        }

        .date{
            color:white;
            font-size:1.6rem;
            margin-top:10px;
        }

        .subtitle{
            color:#cbd5e1;
            margin-top:20px;
            font-size:1.1rem;
        }

        .circle{
            position:absolute;
            border-radius:50%;
            background:rgba(255,255,255,0.08);
            animation:float 10s infinite ease-in-out;
        }

        .circle:nth-child(1){
            width:200px;
            height:200px;
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
            top:70%;
            left:20%;
            animation-duration:12s;
        }

        @keyframes float{
            0%,100%{
                transform:translateY(0px);
            }
            50%{
                transform:translateY(-30px);
            }
        }

        @media(max-width:768px){
            .clock{
                font-size:3rem;
            }

            .date{
                font-size:1.2rem;
            }

            h1{
                font-size:2rem;
            }
        }
    </style>
</head>
<body>

<div class="circle"></div>
<div class="circle"></div>
<div class="circle"></div>

<div class="card">
    <h1>🕒 RELOJ DIGITAL</h1>

    <div id="clock" class="clock">00:00:00</div>

    <div id="date" class="date"></div>

    <div class="subtitle">
        Landing Page desarrollada con Flask
    </div>
</div>

<script>

function actualizarReloj(){

    const ahora = new Date();

    const hora = String(ahora.getHours()).padStart(2,'0');
    const minuto = String(ahora.getMinutes()).padStart(2,'0');
    const segundo = String(ahora.getSeconds()).padStart(2,'0');

    document.getElementById("clock").innerHTML =
        `${hora}:${minuto}:${segundo}`;

    const opciones = {
        weekday:'long',
        year:'numeric',
        month:'long',
        day:'numeric'
    };

    document.getElementById("date").innerHTML =
        ahora.toLocaleDateString('es-ES', opciones);
}

actualizarReloj();
setInterval(actualizarReloj,1000);

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)