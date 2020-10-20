import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():
    
    fim = 100
    
    a = 1
    b = 1
    numero = 3
    
    primos = "2,"

    while b < fim:
        ehprimo = 1
        for i in range(2,numero):
            if numero % i == 0:
                ehprimo = 0
                break
        if (ehprimo):
            primos = primos + str(numero) + ','
            p+=1
    return primos 


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

