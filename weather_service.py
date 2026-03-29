from dataclasses import dataclass
from typing import Dict, Any

import requests


@dataclass
class WeatherData:
    city: str
    temperature: float
    feels_like: float
    humidity: int
    description: str
    wind_speed: float
    pressure: int
    temp_min: float
    temp_max: float
    local_time: str


class WeatherService:
    """
    Helper around OpenWeatherMap.
    Falls back to demo data if API key is not configured.
    """

    def __init__(self, api_key: str, timeout: int = 10) -> None:
        self.api_key = api_key.strip()
        self.timeout = timeout
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    @property
    def demo_mode(self) -> bool:
        placeholder_values = {
            "",
            "YOUR_API_KEY",
            "YOUR_REAL_API_KEY",
            "PASTE_YOUR_API_KEY_HERE",
        }
        return self.api_key in placeholder_values

    def get_weather(self, city: str) -> WeatherData:
        if not city.strip():
            raise ValueError("Please enter a city name.")

        if self.demo_mode:
            return self._demo_weather(city)

        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",
        }

        try:
            resp = requests.get(self.base_url, params=params, timeout=self.timeout)
        except requests.exceptions.RequestException as exc:
            raise RuntimeError(f"Network error: {exc}") from exc

        if resp.status_code == 401:
            raise RuntimeError(
                "Unauthorized (401). Your API key may be missing, invalid, or not yet activated."
            )
        if resp.status_code == 404:
            raise RuntimeError(
                "City not found (404). Please check the spelling or try a nearby major city."
            )

        if not resp.ok:
            raise RuntimeError(f"Unexpected error from API: {resp.status_code}")

        data: Dict[str, Any] = resp.json()
        try:
            main = data["main"]
            weather_list = data.get("weather", [])
            description = weather_list[0]["description"] if weather_list else "N/A"
            name = data.get("name") or city
            wind = data.get("wind", {})
            wind_speed = float(wind.get("speed", 0.0))
            pressure = int(main.get("pressure", 0))
            temp_min = float(main.get("temp_min", main["temp"]))
            temp_max = float(main.get("temp_max", main["temp"]))

            # Compute local time string from timestamp + timezone offset (both in seconds)
            from datetime import datetime, timezone, timedelta

            dt_value = data.get("dt")
            tz_offset = data.get("timezone", 0)
            if isinstance(dt_value, (int, float)):
                tz = timezone(timedelta(seconds=tz_offset))
                local_dt = datetime.fromtimestamp(dt_value, tz=tz)
                local_time = local_dt.strftime("%Y-%m-%d %H:%M")
            else:
                local_time = "N/A"
        except (KeyError, IndexError, TypeError, ValueError) as exc:
            raise RuntimeError("Unexpected response format from API.") from exc

        return WeatherData(
            city=name,
            temperature=float(main["temp"]),
            feels_like=float(main["feels_like"]),
            humidity=int(main["humidity"]),
            description=description.title(),
            wind_speed=wind_speed,
            pressure=pressure,
            temp_min=temp_min,
            temp_max=temp_max,
            local_time=local_time,
        )

    def _demo_weather(self, city: str) -> WeatherData:
        # Simple deterministic demo data so the UI is always testable
        normalized = city.strip() or "Hyderabad"
        base_temp = 30.0
        offset = (len(normalized) % 6) - 3  # -3 .. +2
        temp = base_temp + offset
        humidity = 55 + (len(normalized) % 20)
        return WeatherData(
            city=normalized.title(),
            temperature=temp,
            feels_like=temp + 1.5,
            humidity=humidity,
            description="Clear (demo mode)",
            wind_speed=5.0 + (len(normalized) % 5),
            pressure=1010 + (len(normalized) % 8),
            temp_min=temp - 2.0,
            temp_max=temp + 3.0,
            local_time="Demo time",
        )

