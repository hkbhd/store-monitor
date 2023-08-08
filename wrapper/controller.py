from flask import Flask, Blueprint, request, jsonify
from core.manager import ReportManager
controller_bp = Blueprint("controller", __name__)


@controller_bp.route("/trigger_report", methods=["GET"])
def trigger_report():
    return ReportManager.generate_report()


@controller_bp.route("/get_report", methods=["GET"])
def get_report():
    report_id=request.args.get("report_id")
    return ReportManager.get_report_status(report_id)
