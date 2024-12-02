from flask import Flask

from app.blueprints import index

app=Flask(__name__)
app.register_blueprint(index.bp)

if(__name__=="__main__"):
    app.run(debug=True)