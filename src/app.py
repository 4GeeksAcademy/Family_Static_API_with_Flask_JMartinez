"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
import json 
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)



"""-------------------------------------<Get_all>----------------------------------------- """
@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()

    if members is None:
        return jsonify(response_body), 400
    else:

        response_body = {
            "hello": "world",
            "family": members
        }


        return jsonify(response_body), 200
"""-------------------------------------</Get_all>----------------------------------------- """


"""-------------------------------------<Get_one>----------------------------------------- """

@app.route('/member/<int:member_id>', methods=['GET'])
def obetener_miembro(member_id):

    # this is how you can use the Family datastructure by calling its methods
    members_one = jackson_family.get_member(member_id)
   
    if members_one:
        if members_one is None:
            return jsonify("miembro no valido"), 400
        else:

            response_body = {
                "hello": "world",
                "family": members_one
            }


            return jsonify(response_body), 200
    else :
        
        return jsonify("¡el miembro no existe!"), 400
              
"""-------------------------------------</Get_one>----------------------------------------- """

"""-------------------------------------<POST_Member>----------------------------------------- """

@app.route('/member', methods=['POST'])
def add_miembro():

    # this is how you can use the Family datastructure by calling its methods
    try:

        new_member = json.loads(request.data)
        jackson_family.add_member(new_member)
        return jsonify(new_member), 200


    except:

            return jsonify(), 200

         
              
"""-------------------------------------</POST_Member>----------------------------------------- """

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
