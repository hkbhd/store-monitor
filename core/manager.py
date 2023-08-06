from core.service import ReportService


class ReportManager:
    @staticmethod
    def generate_report():
        print("The flow has reached the manager")
        ReportService.generate_report()

    @staticmethod
    def get_report_status(report_id):
        pass
