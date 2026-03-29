from flask import Flask, render_template, request, redirect, url_for

from weather_service import WeatherService


def create_app() -> Flask:
    app = Flask(__name__)

    # TODO: Replace this with your real OpenWeatherMap API key for live data.
    api_key = "YOUR_API_KEY"
    service = WeatherService(api_key=api_key)

    @app.route("/", methods=["GET", "POST"])
    def index():
        error = None
        weather = None
        demo = service.demo_mode

        if request.method == "POST":
            city = (request.form.get("city") or "").strip()
            # Redirect after POST so browser refresh doesn't show resubmit dialog (PRG pattern)
            return redirect(url_for("index", city=city))

        city = (request.args.get("city") or "").strip()
        if city:
            try:
                weather = service.get_weather(city)
            except Exception as exc:  # noqa: BLE001
                error = str(exc)

        return render_template(
            "index.html",
            city=city,
            weather=weather,
            error=error,
            demo=demo,
        )

    return app


app = create_app()


if __name__ == "__main__":
    # Run the development server
    app.run(debug=True)

