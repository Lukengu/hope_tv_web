from src.views.home import home_page as  home_page_blueprint


class Route(object):
    @staticmethod
    def init_route(app):
        app.register_blueprint(home_page_blueprint, url_prefix='/')
