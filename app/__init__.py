from flask import Flask
import secrets

from app.blueprints import index
from app.blueprints import session

app=Flask(__name__)
# app.secret_key="assdsffgghjhhiiuygrdtdt"
app.secret_key=secrets.token_hex(16)
app.register_blueprint(index.bp)
app.register_blueprint(session.bp)


if(__name__=="__main__"):
    app.run(debug=True)