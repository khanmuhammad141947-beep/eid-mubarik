from flask import request, render_template, jsonify
from . import main_bp
from utilities.save_data import save_data, get_data


@main_bp.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@main_bp.route('/eid_card', methods=['GET'])
def eid_card():
    toname = request.args.get('toname', 'Banta Tech')
    fromname = request.args.get('fromname', 'Khan Muhammad')
    card_no = request.args.get('card_no', 2)
    if card_no not in ['1', '2', '3']:
        card_no = '1'  # Default to card 2 if invalid number is provided
    return render_template(f'eid_card_{card_no}.html', toname=toname, fromname=fromname)

@main_bp.route("/save_eid_card", methods=["POST"])
def save_eid_card():

    data = request.get_json()

    save_data(data)

    return jsonify({"status":"success"})

@main_bp.route("/admin", methods=["GET"])
def admin():
    data = get_data()
    return render_template("admin.html", data=data)