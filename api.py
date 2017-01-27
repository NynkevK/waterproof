from bottle import run, get, post, request


@get("/data")
def return_data():
    # schrijf hier de code om de sensor te lezen
    # return 0 als er geen water is en 1 als er wel water is

    return {"data": data}


@get("/status")
def return_status():
    # schrijf hier de code om de status van de armen terug te geven
    # als de armen open zijn return "open", als de armen dicht zijn return "closed"

    return {"status": status}


@post("/")
def execute_action():
    action = request.json.get("action")

run(reloader=True, debug=True)
# reloader=True zorgt er voor dat als er een verndering in dit script wordt gemaakt dat de server automatische herstart wordt
# de parameters kunnen weggehaald worden al dit script klaar is
