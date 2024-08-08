def get_basic_health(level: int) -> dict:
    if level == 1:
        return {"status": "ok"}
    return {"status": "ok", "services": "ok"}