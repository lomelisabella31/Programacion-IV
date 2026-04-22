import requests

BASE = "http://127.0.0.1:5002"

def test_get_all():
    r = requests.get(BASE + "/vacunas")
    assert r.status_code == 200

def test_get_year():
    r = requests.get(BASE + "/vacunas/2001")
    assert r.status_code == 200
