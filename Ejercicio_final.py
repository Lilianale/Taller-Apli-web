import openai

openai.api_base ="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"
system_init = '''Haz de cuenta que eres un analizador de sentimientos. 
                Yo te paso sentimientos y tu analizas el sentimiento de los mensajes
                y me das una respuesta con almenos un caracter u como máximo 4 caracteres
                SOLO RESPUESTAS NUMÉRICAS. donde -1 es negatividad máxima, 0 es neutral y 1 es positividad máxima.
                pudes ir entre esos rangos, es decir 0.3, -0.5 etc tambien son válidos.
                (podes responder solo con inits o floats)'''

mensajes = [ {"role": "system","content": system_rol}]


class Sentimiento:
    def __init__(self,nombre,color):
        self.nombre = nombre
        self.color = color

    def __str(self):
        return"\x1b[1;{}m{}\x1b[0;37m".format(self.color,self.nombre)]

class AnalizadorDeSentimientos:
    def __init__(self,rangos):
        self.rangos = rangos

        def analizar_sentimientos(self,polaridad):
            for rango, sentimiento in self.rangos:
                if rango[0]< polaridad <= rango[1]:
                    return sentimiento
            ret Sentimiento("Muy negativo", "31")

rangos = [
((-0.6,-0.3), Sentimiento("negativo","31")),
((-0.3,-0.1), Sentimiento("Algo negativo","31")),
((-0.1,0.1), Sentimiento("neutral","33")),
((0.1,0.4), Sentimiento("algo positivo","32")),
((0.4,0.9), Sentimiento("positivo","32")),
((0.9,1), Sentimiento("muy positivo","32")),

]

def analizar_sentimientos (self, polaridad):
    if polaridad > xb-0.8 and polaridad <= -0.3:
        return "\x1b[1;31m"+ "Negativo"+ "\x1b[0;37m"
    elif polaridad >-0.3 and polaridad < 0.1:
        return "\x1b[1;31m"+ "Algo negativo"+ "\x1b[0;37m"
     elif polaridad >= -0.1 and polaridad <= -0.1:
        return "\x1b[1;31m"+ "Neutral"+ "\x1b[0;37m"
    elif polaridad >= 0.1 and polaridad <= 0.4:
        return "\x1b[1;31m"+ "Algo positivo"+ "\x1b[0;37m"
    elif polaridad >= 0.4 and polaridad <= 0.9:
        return "\x1b[1;31m"+ " positivo"+ "\x1b[0;37m"
        elif polaridad > 0.9:
        return "\x1b[1;31m"+ "Muy positivo"+ "\x1b[0;37m"
    else:
        return"\x1b[1;31m"+ "Muy negativo" + "\x1b[0;37m"


analizador = AnalizadorDeSentimientos()

while true:
    user_promt = input ("\x1b[1;31m"+ "\n Decime Algo" + "\x1b[0;37m")
    mensajes.append({"role":"user", "content": user_promt})

    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = mensajes,
        max_tokens = 8
    )

    respuesta = completion.choices[ 0].message[ "content"]
    mensajes.append({"role":"assistant","content": respuesta})

    sentimiento = analizador.analizar_sentimientos(float(respuesta))
    print(sentimiento)