from core.repository import ReportRepository


class ReportService:
    @staticmethod
    def generate_report():
        print("The flow has reached the service")
        ReportRepository.generate_report()

    @staticmethod
    def get_report_status(report_id):
        pass
