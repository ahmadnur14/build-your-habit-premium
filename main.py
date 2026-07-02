"""
Main Application Entry Point
Integrated habit tracking system with Excel export
"""

from excel_file_generator import ExcelFileGenerator
from tracker_builder import TrackerBuilder
from analytics_engine import AnalyticsEngine
from dashboard_builder import DashboardBuilder
from chart_engine import ChartEngine
from report_engine import ReportEngine
from datetime import datetime, timedelta


class HabitTrackingApp:
    """Main application for habit tracking with Excel export"""
    
    def __init__(self):
        """Initialize the application"""
        self.tracker_builder = TrackerBuilder()
        self.analytics_engine = AnalyticsEngine()
        self.dashboard_builder = DashboardBuilder()
        self.chart_engine = ChartEngine()
        self.report_engine = ReportEngine()
        self.excel_generator = ExcelFileGenerator(output_dir='downloads')
    
    # ===== TRACKER OPERATIONS =====
    def create_new_habit(self, habit_name, frequency='daily', unit='count'):
        """Create a new habit tracker"""
        tracker_id = f"habit_{datetime.now().timestamp()}"
        tracker = self.tracker_builder.create_tracker(
            tracker_id=tracker_id,
            habit_name=habit_name,
            target_frequency=frequency,
            unit=unit
        )
        return tracker_id, tracker
    
    def log_habit(self, tracker_id, value, notes=''):
        """Log an entry for a habit"""
        entry = {
            'value': value,
            'timestamp': datetime.now(),
            'notes': notes
        }
        self.tracker_builder.add_entry(tracker_id, entry['value'], entry['timestamp'])
        return entry
    
    def get_all_trackers(self):
        """Get all active trackers"""
        return self.tracker_builder.list_trackers()
    
    # ===== ANALYTICS OPERATIONS =====
    def get_completion_rate(self, tracker_id):
        """Get completion rate for a tracker"""
        tracker = self.tracker_builder.get_tracker(tracker_id)
        if not tracker:
            return None
        
        rate = self.analytics_engine.calculate_completion_rate(
            tracker_id,
            tracker['entries'],
            tracker['target_frequency']
        )
        return rate
    
    def get_streak(self, tracker_id):
        """Get current streak for a tracker"""
        tracker = self.tracker_builder.get_tracker(tracker_id)
        if not tracker:
            return None
        
        streak = self.analytics_engine.get_streak(
            tracker['entries'],
            tracker['target_frequency']
        )
        return streak
    
    def get_trend_analysis(self, tracker_id, period_days=7):
        """Get trend analysis for a tracker"""
        tracker = self.tracker_builder.get_tracker(tracker_id)
        if not tracker:
            return None
        
        trend = self.analytics_engine.get_trend(tracker['entries'], period_days)
        return trend
    
    def get_statistics(self, tracker_id):
        """Get statistics for a tracker"""
        tracker = self.tracker_builder.get_tracker(tracker_id)
        if not tracker:
            return None
        
        stats = self.analytics_engine.get_statistics(tracker['entries'])
        return stats
    
    # ===== DASHBOARD OPERATIONS =====
    def create_dashboard(self, dashboard_title):
        """Create a dashboard"""
        dashboard_id = f"dashboard_{datetime.now().timestamp()}"
        dashboard = self.dashboard_builder.create_dashboard(dashboard_id, dashboard_title)
        return dashboard_id, dashboard
    
    def add_metric_to_dashboard(self, dashboard_id, metric_name, value, target=None):
        """Add a metric card to dashboard"""
        card_id = f"card_{datetime.now().timestamp()}"
        card = self.dashboard_builder.create_metric_card(
            card_id, metric_name, metric_name, value
        )
        self.dashboard_builder.add_component(dashboard_id, card_id, 'metric_card', (0, 0), (1, 1))
        return card
    
    def add_progress_bar(self, dashboard_id, label, current, max_val):
        """Add progress bar to dashboard"""
        progress_id = f"progress_{datetime.now().timestamp()}"
        progress = self.dashboard_builder.create_progress_bar(
            progress_id, label, current, max_val
        )
        self.dashboard_builder.add_component(dashboard_id, progress_id, 'progress_bar', (0, 0), (1, 1))
        return progress
    
    # ===== CHART OPERATIONS =====
    def create_line_chart(self, tracker_id, chart_title):
        """Create a line chart for a tracker"""
        tracker = self.tracker_builder.get_tracker(tracker_id)
        if not tracker:
            return None
        
        chart_id = f"chart_{datetime.now().timestamp()}"
        chart = self.chart_engine.create_line_chart(
            chart_id, chart_title, tracker['entries']
        )
        return chart
    
    def create_performance_chart(self, trackers_data):
        """Create a performance comparison chart"""
        chart_id = f"chart_{datetime.now().timestamp()}"
        chart = self.chart_engine.create_bar_chart(
            chart_id, 'Performance Overview', trackers_data
        )
        return chart
    
    # ===== REPORT OPERATIONS =====
    def generate_daily_report(self):
        """Generate daily report"""
        trackers = self.get_all_trackers()
        trackers_summary = []
        
        for tracker in trackers:
            trackers_summary.append({
                'name': tracker['habit_name'],
                'completed': len(tracker['entries']) > 0,
                'value': tracker['entries'][-1]['value'] if tracker['entries'] else 0
            })
        
        report_id = f"report_{datetime.now().timestamp()}"
        report = self.report_engine.create_daily_report(
            report_id, datetime.now().date(), trackers_summary
        )
        return report
    
    def generate_weekly_report(self):
        """Generate weekly report"""
        report_id = f"report_{datetime.now().timestamp()}"
        week_start = datetime.now().date()
        
        trackers = self.get_all_trackers()
        trackers_data = {t['id']: t for t in trackers}
        
        report = self.report_engine.create_weekly_report(
            report_id, week_start, trackers_data
        )
        return report
    
    def generate_monthly_report(self):
        """Generate monthly report"""
        report_id = f"report_{datetime.now().timestamp()}"
        month = datetime.now().strftime('%Y-%m')
        
        trackers = self.get_all_trackers()
        trackers_data = {t['id']: t for t in trackers}
        
        report = self.report_engine.create_monthly_report(
            report_id, month, trackers_data
        )
        return report
    
    # ===== EXCEL EXPORT OPERATIONS =====
    def export_tracker_template(self):
        """Export habit tracker template as Excel"""
        filepath = self.excel_generator.generate_habit_tracker_template(
            filename='Habit_Tracker_Template.xlsx'
        )
        return filepath
    
    def export_habit_data(self):
        """Export all habit data as Excel"""
        trackers = self.get_all_trackers()
        tracker_data = {t['id']: t for t in trackers}
        
        filepath = self.excel_generator.generate_habit_data_export(
            tracker_data,
            filename='Habit_Data_Export.xlsx'
        )
        return filepath
    
    def export_weekly_report_excel(self):
        """Export weekly report as Excel"""
        filepath = self.excel_generator.generate_weekly_report(
            filename='Weekly_Report.xlsx'
        )
        return filepath
    
    def export_monthly_report_excel(self):
        """Export monthly report as Excel"""
        filepath = self.excel_generator.generate_monthly_report(
            filename='Monthly_Report.xlsx'
        )
        return filepath
    
    def get_available_downloads(self):
        """Get list of available Excel files for download"""
        return self.excel_generator.list_generated_files()


# ===== USAGE EXAMPLES =====
if __name__ == '__main__':
    # Inisialisasi aplikasi
    app = HabitTrackingApp()
    
    print("=" * 60)
    print("HABIT TRACKING APPLICATION - USAGE EXAMPLES")
    print("=" * 60)
    
    # 1. Create habits
    print("\n1. Creating new habits...")
    habit1_id, habit1 = app.create_new_habit('Morning Exercise', 'daily', 'minutes')
    habit2_id, habit2 = app.create_new_habit('Reading', 'daily', 'pages')
    habit3_id, habit3 = app.create_new_habit('Meditation', 'daily', 'minutes')
    print(f"✓ Created {len(app.get_all_trackers())} habits")
    
    # 2. Log entries
    print("\n2. Logging habit entries...")
    app.log_habit(habit1_id, 30, 'Morning run in park')
    app.log_habit(habit2_id, 20, 'Read development book')
    app.log_habit(habit3_id, 15, 'Morning meditation')
    print("✓ Logged 3 habit entries")
    
    # 3. Get analytics
    print("\n3. Analyzing data...")
    completion = app.get_completion_rate(habit1_id)
    streak = app.get_streak(habit1_id)
    stats = app.get_statistics(habit1_id)
    print(f"✓ Completion Rate: {completion:.1f}%")
    print(f"✓ Current Streak: {streak} days")
    print(f"✓ Total Entries: {stats['total_entries']}")
    
    # 4. Generate reports
    print("\n4. Generating reports...")
    daily_report = app.generate_daily_report()
    print(f"✓ Daily Report Generated: {daily_report['type']}")
    
    weekly_report = app.generate_weekly_report()
    print(f"✓ Weekly Report Generated: {weekly_report['type']}")
    
    monthly_report = app.generate_monthly_report()
    print(f"✓ Monthly Report Generated: {monthly_report['type']}")
    
    # 5. Export to Excel
    print("\n5. Exporting to Excel...")
    template_path = app.export_tracker_template()
    print(f"✓ Template exported: {template_path}")
    
    data_path = app.export_habit_data()
    print(f"✓ Data exported: {data_path}")
    
    weekly_path = app.export_weekly_report_excel()
    print(f"✓ Weekly report exported: {weekly_path}")
    
    monthly_path = app.export_monthly_report_excel()
    print(f"✓ Monthly report exported: {monthly_path}")
    
    # 6. List available downloads
    print("\n6. Available files for download:")
    files = app.get_available_downloads()
    for file in files:
        print(f"   - {file['name']} ({file['size']} bytes)")
        print(f"     URL: {file['url']}")
    
    print("\n" + "=" * 60)
    print("All files ready in 'downloads' folder!")
    print("=" * 60)
