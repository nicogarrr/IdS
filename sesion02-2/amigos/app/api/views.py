from flask import request, abort, jsonify
from .. import db
from . import api
from ..models import Amigo

@api.route("/amigo/<int:id>", methods=["GET"])
def get_amigo(id):
    amigo = Amigo.query.get_or_404(id)
    amigodict = {
        'id': amigo.id,
        'name': amigo.name,
        'lati': amigo.lati,
        'longi': amigo.longi,
        'device': amigo.device
    }
    return jsonify(amigodict)

@api.route("/amigo/byName/<name>", methods=["GET"])
def get_amigo_by_name(name):
    amigo = Amigo.query.filter_by(name=name).first()
    if not amigo:
        abort(404, "No se encuentra ningún amigo con ese nombre")
    amigodict = {
        'id': amigo.id,
        'name': amigo.name,
        'lati': amigo.lati,
        'longi': amigo.longi,
        'device': amigo.device
    }
    return jsonify(amigodict)

@api.route("/amigos", methods=["GET"])
def list_amigos():
    amigos = Amigo.query.all()
    amigos_list = [
        {
            'id': a.id,
            'name': a.name,
            'lati': a.lati,
            'longi': a.longi,
            'device': a.device
        }
        for a in amigos
    ]
    return jsonify(amigos_list)

@api.route("/devices", methods=["GET"])
def list_devices():
    """
    Suministra la lista de todos los device no nulos ni cadenas vacías.
    """
    amigos = Amigo.query.filter(Amigo.device.isnot(None), Amigo.device != "").all()
    devices = [a.device for a in amigos]
    return jsonify(devices)

@api.route("/amigo/<int:id>", methods=["PUT"])
def edit_amigo(id):
    amigo = Amigo.query.get_or_404(id)
    if not request.json:
        abort(422, "No se ha enviado JSON")
    name = request.json.get("name")
    lati = request.json.get("lati")
    longi = request.json.get("longi")

    if name:
        amigo.name = name
    if lati:
        amigo.lati = lati
    if longi:
        amigo.longi = longi
    if "device" in request.json:
        amigo.device = request.json.get("device")

    if name or lati or longi or ("device" in request.json):
        db.session.commit()

    amigodict = {
        "id": amigo.id,
        "name": amigo.name,
        "longi": amigo.longi,
        "lati": amigo.lati,
        "device": amigo.device
    }
    return jsonify(amigodict)

@api.route("/amigo/<int:id>", methods=["DELETE"])
def delete_amigo(id):
    amigo = Amigo.query.get_or_404(id)
    db.session.delete(amigo)
    db.session.commit()
    return ('', 204)

@api.route("/amigos", methods=["POST"])
def new_amigo():
    if not request.json:
        abort(422, "No se ha enviado JSON")
    name = request.json.get("name")
    if not name:
        abort(422, "El JSON no incluye el campo 'name'")
    amigo = Amigo.query.filter_by(name=name).first()
    if amigo:
        abort(422, "Ya existe un amigo con ese nombre")

    lati = request.json.get("lati", "0")
    longi = request.json.get("longi", "0")
    device = request.json.get("device", "")

    amigo = Amigo(name=name, lati=lati, longi=longi, device=device)
    db.session.add(amigo)
    db.session.commit()

    amigodict = {
        "id": amigo.id,
        "name": amigo.name,
        "longi": amigo.longi,
        "lati": amigo.lati,
        "device": amigo.device
    }
    return jsonify(amigodict)
