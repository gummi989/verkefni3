
from sys import argv

import bottle

from bottle import*



@route('/')




def a():

    return"""

    <h2<verkefni 3</h1>

    <a href="/sida/1">LiðurA</a>

    <a href="/sida/2">LiðurB</a>

    

    """

@route("/sida/<id>")
def index():
    return template("temp-A.tpl")


@route("/page1")
def page(id):
    return template("temp-A.tpl")
@route("/sida/<kt<")
def page(kt):
    return template("temp-kt.tpl", kt=kt)






#run(host='localhost',port=8080)
run(host='0.0.0.',port=os.environ.get('PORT'))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
