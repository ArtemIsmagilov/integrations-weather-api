def city_not_found(city_name: str):
    return f"City with name '{city_name}' not found!"


def status_code_not_200(url: str, status_code: int):
    return f"Request on '{url}' return status code {status_code}"
