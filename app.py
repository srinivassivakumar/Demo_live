"""app.py"""

__author__="rajesh"
__copyright__ ="xyz"
__created_date__= "30-04-2022"

from flask import Flask
from flask_cors import CORS, cross_origin
import config as cfg

app = Flask(__name__)
cors = CORS(app)

# GET === whenever you have to fetch something from DB
# POST/PATCH === Insert the new item in DB
# Delete === if we have to remove the data
# put === to update something


@app.route("/",methods=["GET","POST"])
@cross_origin(origins="*")
def listofnumbers():




if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True,port=cfg.port)