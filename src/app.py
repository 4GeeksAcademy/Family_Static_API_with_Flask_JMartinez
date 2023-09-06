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

    # if members is None:
    #     return jsonify(response_body), 400
    # else:
    return jsonify(members), 200
"""-------------------------------------</Get_all>----------------------------------------- """


"""-------------------------------------<Get_one>----------------------------------------- """

@app.route('/member/<int:miembro_id>', methods=['GET'])
def obetener_miembro(miembro_id):

    # this is how you can use the Family datastructure by calling its methods
    members_one = jackson_family.get_member(miembro_id)
    # del members_one['id']
    # print(members_one)
    return jsonify(members_one), 200


              
"""-------------------------------------</Get_one>----------------------------------------- """

"""-------------------------------------<POST_Member>----------------------------------------- """

@app.route('/member', methods=['POST'])
def add_miembro():

    # this is how you can use the Family datastructure by calling its methods
    try:

        new_member = json.loads(request.data)
        moro = {
             
            "id": jackson_family._generateId(),
            "first_name": new_member["first_name"],
            "last_name":jackson_family.last_name,
            "age": new_member["age"],
            "lucky_numbers": new_member["lucky_numbers"]
        
        }
        jackson_family.add_member(new_member)
        return jsonify(new_member), 200


    except:

            return jsonify(), 200
    

"""-------------------------------------</POST_Member>----------------------------------------- """

"""-------------------------------------</POST_Elminar>----------------------------------------- """


@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    # elimina un miembro de la familia Jackson por su ID
    member = jackson_family.delete_member(member_id)
    # devuelve una respuesta JSON  con la clave "done": true.
    return jsonify({"done": True}), 200





         
"""-------------------------------------</POST_Elminar>----------------------------------------- """           

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
