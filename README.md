# Python Hacking - flask

Projekt tworzony podczas spotkań hs3city *Python Hacking* w [Hacker:Space](http://hs3.pl/) trójmiasto.

## Przygotowanie środowiska:

### Linux / MacOS
_(ToDo: dla Windows)_

```bash
python3 -m venv ~/projekty/venv/pythonhacking-flask
```

Ewentualnie z kopiowaniem całego interpretera:
```bash
python3 -m venv --copies ~/projekty/venv/pythonhacking-flask
```

Aktywowanie środowiska:
```bash
source ~/projekty/venv/pythonhacking-flask/bin/activate
```

## Pobranie i uruchomienie projektu

Pobranie źródeł:
```bash
cd ~/projekty/
git clone git@github.com:hs3city/flask_hs.git
```

### Instalacja zależności
Pamiętaj, aby środowisko było aktywne:
```bash
cd ~/projekty/flask_hs/
pip install --upgrade -r requirements.txt
```

Uruchomienie aplikacji

```bash
python main.py
```
