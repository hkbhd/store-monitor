from core.service import ReportService
from flask import Flask, jsonify
import asyncio
import threading

app = Flask(__name__)

class ReportManager:

    report_tasks = {}

    @staticmethod
    def generate_report():
        report_id = ReportService.generate_report_id()

        thread = threading.Thread(target=ReportManager._generate_report_async, args=(report_id,))
        thread.start()

        ReportManager.report_tasks[report_id] = "Processing"

        return jsonify({"Message": "Report creation initiated, the report id is : " + report_id})

    @staticmethod
    def _generate_report_async(report_id):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        async def generate_report_async():
            await ReportService.generate_report(report_id)
            ReportManager.report_tasks[report_id] = "Completed"

        loop.run_until_complete(generate_report_async())
        loop.close()

    @staticmethod
    def get_report_status(report_id):
        if report_id in ReportManager.report_tasks:
            return jsonify({"Status": ReportManager.report_tasks[report_id]})
        else:
            return jsonify({"Status": "Not Found"})
