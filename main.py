from typing import Union

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/getcode")
async def meteo(cp: str = Form(...)):
    geo_url = 'https://geocoding-api.open-meteo.com/v1/search'
    params = {'name': cp, 'count': 1, 'language': 'fr', 'format': 'json'}
    res = requests.get(geo_url, params=params).json()
    if not res.get('results'):
        raise ValueError(f"Code postal {cp} introuvable")
    loc = res['results'][0]

    lat, lon = loc['latitude'], loc['longitude']
    meteo_url = 'https://api.open-meteo.com/v1/forecast'
    m = requests.get(meteo_url, params={
        'latitude': lat,
        'longitude': lon,
        'current_weather': True,
        'timezone': 'Europe/Paris'
    }).json().get('current_weather', {})

    return {
        'ville': loc['name'],
        'pays': loc['country'],
        'latitude': lat,
        'longitude': lon,
        'temperature_C': m.get('temperature'),
        'vent_kmh': m.get('windspeed'),
        'heure': m.get('time')
    }