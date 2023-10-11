from django.apps import AppConfig


class ApiPortfolioConfig(AppConfig):
    name = "api_portfolio"

    def ready(self) -> None:
        import api_portfolio.signals
