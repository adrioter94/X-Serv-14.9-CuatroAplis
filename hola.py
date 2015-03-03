#!/usr/bin/python

import webapp


class holaApp(webapp.app):

    def parse(self, request, rest):
        recurso = request.split()[1][1:]
        if recurso[0:4] == "hola":
            recurso = "Hola"
        elif recurso[0:5] == "adios":
            recurso = "Adios"
        return recurso

    def process(self, parsedRequest):
        return("200 OK", "<html><body>"
               + str(parsedRequest) + " </body></html>")
