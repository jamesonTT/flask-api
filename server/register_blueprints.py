from .blueprints.index import index

def register_blueprints(app):
    app.register_blueprint(index)
