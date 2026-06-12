from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Aditya Gaming Hub</title>

<style>
body{
    margin:0;
    font-family:Arial;
    background:#111;
    color:white;
}

header{
    background:linear-gradient(to right,#ff6600,#ff0000);
    padding:30px;
    text-align:center;
}

.banner{
    width:100%;
    height:300px;
    background:url('https://picsum.photos/1200/600');
    background-size:cover;
    background-position:center;
}

.card{
    background:#222;
    margin:20px;
    padding:20px;
    border-radius:15px;
    box-shadow:0 0 15px orange;
}

button{
    background:orange;
    color:white;
    border:none;
    padding:12px 20px;
    border-radius:10px;
    font-size:18px;
}

video{
    width:100%;
    border-radius:15px;
}

footer{
    text-align:center;
    padding:20px;
    background:black;
}
</style>

</head>
<body>

<header>
<h1>🎮 ADITYA GAMING HUB</h1>
<p>Roblox Games • Videos • Updates</p>
</header>

<div class="banner"></div>

<div class="card">
<h2>🔥 NEW GAME RELEASED!</h2>
<p>Bike Obby For Brainrots is available now.</p>
<button>Play Now</button>
</div>

<div class="card">
<h2>⭐ Featured Video</h2>
<video controls>
<source src="" type="video/mp4">
</video>
</div>

<div class="card">
<h2>🏆 Top Update</h2>
<p>New bikes, new brainrots and exciting rewards!</p>
</div>

<div class="card">
<h2>📢 Announcement</h2>
<p>Subscribe for more Roblox content.</p>
</div>

<footer>
© 2026 Aditya Gaming Hub
</footer>

</body>
</html>
"""

app.run(host="0.0.0.0", port=5000)
