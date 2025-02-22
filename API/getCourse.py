from flask import Blueprint, request, jsonify
from APIDataBase import APIDataBase

getCourse_blp = Blueprint('getCourse', __name__)
db = APIDataBase('localhost', 3306, 'root', 'fcu')

@getCourse_blp.route('/getCourse', methods=['GET'])
def getCourse():
    year = request.args.get('year')
    sms = request.args.get('sms')
    # degree = request.args.get('degree')
    # dept = request.args.get('dept')
    # unit = request.args.get('unit')
    cls_id = request.args.get('cls_id')
    print(year, sms, cls_id)
    if year == None or sms == None or cls_id == None:
        return jsonify({'error': '參數錯誤'})
    data = db.execSelect('SELECT * FROM `' + year + sms + '_course`' + ' WHERE `cls_id` = ' + '\'' + cls_id + '\'')
    if data == []:
        return jsonify({'error': '查無資料'})
    return jsonify(data)