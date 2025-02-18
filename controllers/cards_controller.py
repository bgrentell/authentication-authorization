from flask import Blueprint, jsonify, request
from main import db
from models.cards import Card

cards = Blueprint('cards', __name__, url_prefix="/cards")

# The GET routes endpoint
@cards.route("/", methods=["GET"])
def get_cards():
    # get all the cards from the database table
    cards_list = Card.query.all()
    # Convert the cards from the database into a JSON format and store them in result
    #result = cards_schema.dump(cards_list)
    # return the data in JSON format
    #return jsonify(result)
    return "List of cards retrieved"

# The POST route endpoint
@cards.route("/", methods=["POST"])
def create_card():
    # # Create a new card
    # card_fields = card_schema.load(request.json)
    
    # new_card = Card()
    # new_card.title = card_fields["title"]
    # new_card.description = card_fields["description"]
    # new_card.status = card_fields["status"]
    # new_card.priority = card_fields["priority"]
    # # not taken from the request, generated by the server
    # new_card.date = date.today()
    # # add to the database and commit
    # db.session.add(new_card)
    # db.session.commit()
    # # return the card in the response
    # return jsonify(card_schema.dump(new_card))
    return "Card created"

# Finally, we round out our CRUD resource with a DELEYE method
@cards.route("/<int:id>/", methods=["DELETE"])
def delete_card(id):
    # # Get the user id invoking get_jwt_identity
    # user_id = get_jwt_identity()
    # # Find it in the db
    # user = User.query.get(user_id)
    # # Make sure it is in the database
    # if not user:
    #     return abort(401, description="Invalid user")
    # # Stop the request if the user is not an admin
    # if not user.admin:
    #     return abort(401, description="Unauthorised user")
    # # find the card
    # card = Card.query.filter_by(id=id).first()
    # # return an error if the card doesn't exist
    # if not Card:
    #     return abort(400, description="Card doesn't exist")
    # # Delete the card from the database and commit
    # db.session.delete(card)
    # db.session.commit()
    # # Return the card in the response
    # return jsonify(card_schema.dump(card))
    return "Card Deleted"

