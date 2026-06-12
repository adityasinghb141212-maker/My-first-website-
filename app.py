from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Aditya's Website</title>
        <style>
            body{
                background:#111;
                color:white;
                text-align:center;
                font-family:Arial;
                margin-top:50px;
            }
            h1{
                color:gold;
            }
            img{
                width:90%;
                max-width:600px;
                border-radius:15px;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to Aditya's Website</h1>
        <p>This website is hosted from GitHub.</p>

        <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb">

        <h2>My First Website</h2>
        <p>More content coming soon!</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
<header>
