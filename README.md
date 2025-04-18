Predict API

Aplikacja Flask z regułą decyzyjną, skonteneryzowana w Dockerze.

Zadanie

Endpoint `/api/v1.0/predict` przyjmuje dwie liczby (`num1`, `num2`), sumuje je i:

- Jeśli suma > 5.8 → `prediction: 1`
- W przeciwnym razie → `prediction: 0`

Jeśli liczby nie zostaną podane, domyślnie przyjmowane są jako `0`.

---

Przykład zapytania (POST)

```json
{
  "num1": 2,
  "num2": 4
}



-Odpowiedź

```json
{
  "prediction": 1,
  "features": {
    "num1": 2,
    "num2": 4,
    "total": 6
  }
}

-Uruchomienie lokalne
pip install flask
python run.py

-Uruchomienie w Dockerze
docker build -t predict-api .
docker run -p 5000:5000 predict-api



