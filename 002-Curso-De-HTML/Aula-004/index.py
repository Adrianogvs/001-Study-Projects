from flask import Flask

app = Flask(__name__)

# Criar a primeira pagina do site
# route -> meusite.com/caminho
# função -> o que vc quer exibir naquela pagina

@app.rout("/")
def homepage():
    return "Hello, World!"


# Colocar o site no ar
app.run()
