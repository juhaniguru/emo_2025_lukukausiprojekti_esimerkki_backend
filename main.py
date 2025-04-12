from fastapi import FastAPI

app = FastAPI()

@app.get("/api/measurements/{date_str}")
async def get_measurements(date_str: str):
    return [
        {"date_str": "00:00", "value": 5},
        {"date_str": "01:00", "value": 4},
        {"date_str": "02:00", "value": 5},
        {"date_str": "03:00", "value": 1},
        {"date_str": "04:00", "value": 3},
        {"date_str": "05:00", "value": 3},
        {"date_str": "06:00", "value": 6},
        {"date_str": "07:00", "value": 7},
        {"date_str": "08:00", "value": 10},
        {"date_str": "09:00", "value": 10},
        {"date_str": "10:00", "value": 10},
        {"date_str": "11:00", "value": 14},
        {"date_str": "12:00", "value": 14},
        {"date_str": "13:00", "value": 13},
        {"date_str": "14:00", "value": 16},
        {"date_str": "15:00", "value": 16},
        {"date_str": "16:00", "value": 20},
        {"date_str": "17:00", "value": 19},
        {"date_str": "18:00", "value": 20},
        {"date_str": "19:00", "value": 21},
        {"date_str": "20:00", "value": 18},
        {"date_str": "21:00", "value": 11},
        {"date_str": "22:00", "value": 22},
        {"date_str": "23:00", "value": 13},
    ]