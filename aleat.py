#!/usr/bin/python

import webapp
import random


class aleatApp(webapp.app):

    def process(self, request):
        x = random.randrange(100000)
        url = "http://localhost:1234/aleat/" + str(x)
        return("200 OK", "<html><body>" + "<a href=" + url + ">Dame otra"
               + "</body></html>")
