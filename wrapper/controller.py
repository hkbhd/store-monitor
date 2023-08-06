from flask import Flask, Blueprint, request, jsonify
from core.manager import ReportManager

app = Flask(__name__)
controller_bp = Blueprint("controller", __name__)


@controller_bp.route("/trigger_report", methods=["GET"])
def trigger_report():
    print("The flow has reached the controller")
    ReportManager.generate_report()
    return jsonify({"Message":"Message"})


@controller_bp.route("/get_report", methods=["GET"])
def get_report():
    pass
