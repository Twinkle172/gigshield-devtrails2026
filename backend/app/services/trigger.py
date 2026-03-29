# app/services/trigger.py

def check_rain_trigger(rainfall):
    if rainfall > 50:
        return {
            "triggered": True,
            "payout": 500
        }
    return {
        "triggered": False
    }


def check_no_orders(hours):
    if hours >= 3:
        return {
            "triggered": True,
            "payout": 300
        }
    return {
        "triggered": False
    }