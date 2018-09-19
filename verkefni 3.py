
from sys import argv

from bottle import*

@route('/')
def index():
    return """
    <h2<verkefni 3</h1>
    <p><a href="/a">Liður A</a><p>
    <p><a href="/b">Liður B</a><p>
    """

@route("/a")
def index():
    return template("temp-A.tpl")


@route("/page1")
def page(kt):
    return template("temp-kt.tpl")

@route("/sida/<kt>")
def page(kt):
    return template("temp-kt.tpl", kt=kt)

####################################################

# gögn, tvívíður listi
frettir = [["Irma veldur usla á Flórída", "Það er bara ... vesen á Irmu í Flórída.  Milljónir manna hafa þurft að yfirgefa heimili sin vegna yfirvofandi eyðileggingar Irmu...", "irma.jpg", "dsg@frettir.is"],
           ["Veiðin er dræm þetta haustið", "Veiðin hefur heldur verið döpur þetta haustið þrátt fyrir ágætis rigninar upp á síðkastið...", "veidi.png", "est@frettir.is"],
           ["Ólafía stendur sig vel", "Ólafía er komin í 65 sæti peningalistans og hefur því tryggt sér keppnisrétt á LPG mótaröðinni á komandi keppnistimabili...", "golf.jpeg", "htg@frettir.is"],
           ["Ísland dottið úr leik", "Íslenska karlalandsliðið í körfubolta er dottið úr leik a Eurobasket þrátt fyrir ágætis spretti inn a milli.  Ísland spilaði lokaleik sinn á mótinu fyrir troðfullri höll gegn heimamönnum Finnum..", "karfa.jpeg", "dsg@frettir.is"]]

@route("/b")
def index():
    return template("index.tpl")

@route("/page/<id:int>")
def index(id):
        # id vísar á þann undirlista sem við notum í template
        # búum til lýsandi breytur fyrir template (skýrara)
        return template("frett.tpl", fyrirsogn=frettir[id][0], frett=frettir[id][1], mynd = frettir[id][2], hofundur=frettir[id][3])

            # Það hefði líka verið hægt að vísa í lista úr template
            # return template("frett.tpl", frett=frettir[id])

#run(host='localhost',port=8080)

run(host='0.0.0.',port=os.environ.get('PORT'))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
