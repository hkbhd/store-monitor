from core.repository import ReportRepository
import time
import secrets


class ReportService:
    @staticmethod
    def generate_report_id():
        current_timestamp = str(int(time.time()))
        random_string = secrets.token_urlsafe(8)
        return f"{current_timestamp}_{random_string}"

    @staticmethod
    def extract_creation_time(report_id):
        timestamp_part = report_id.split("_")[0]
        creation_time = int(timestamp_part)
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(creation_time))

    @staticmethod
    async def generate_report(report_id):
        report_creation_time=ReportService.extract_creation_time(report_id)
        ReportRepository.find_store_status_by_store_id(5955337179846162144)

