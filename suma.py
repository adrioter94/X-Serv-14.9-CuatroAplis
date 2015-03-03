#!/usr/bin/python

import webapp
import aleat
import hola


class sumaApp(webapp.app):

    def parse(self, request, rest):
        recurso = (request.split()[1])
        try:
            numero1 = int(recurso.split("/")[2][0:])
            numero2 = int(recurso.split("/")[3][0:])
            operandos = [numero1, numero2]
            return operandos
        except ValueError:
            return None

    def process(self, parsedRequest):

        if parsedRequest is None:
            resultado = "Operandos no validos"
        else:
            resultado = (parsedRequest[0]) + (parsedRequest[1])

        return ("200 OK", "<html><body>" + str(resultado) + " </body></html>")

if __name__ == "__main__":
    anApp = webapp.app()
    suma = sumaApp()
    hola = hola.holaApp()
    aleat = aleat.aleatApp()
    testWebApp = webapp.webApp("localhost", 1234, {'/app': anApp,
                                                   '/suma': suma,
                                                   '/hola': hola,
                                                   '/adios': hola,
                                                   '/aleat': aleat})
