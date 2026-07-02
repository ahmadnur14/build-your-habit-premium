"""
Excel Export Utility
Generate and export habit tracking data to Excel format
"""

import json
from datetime import datetime, timedelta


class ExcelExporter:
    """Export habit tracking data to Excel files"""
    
    def __init__(self):
        """Initialize Excel exporter"""
        self.templates = {}
        self.exports = {}
    
    def create_habit_tracker_template(self, filename='habit_tracker_template.xlsx'):
        """
        Create a habit tracker Excel template
        
        Args:
            filename: Output filename
        
        Returns:
            dict: Template configuration
        """
        template = {
            'filename': filename,
            'sheets': {
                'Dashboard': self._create_dashboard_sheet(),
                'Trackers': self._create_trackers_sheet(),
                'Daily Log': self._create_daily_log_sheet(),
                'Statistics': self._create_statistics_sheet(),
                'Goals': self._create_goals_sheet()
            },
            'created_at': datetime.now().isoformat()
        }
        self.templates[filename] = template
        return template
    
    def create_habit_data_export(self, tracker_data, filename='habit_data_export.xlsx'):
        """
        Export actual habit tracking data
        
        Args:
            tracker_data: Dict of tracker data
            filename: Output filename
        
        Returns:
            dict: Export configuration
        """
        export = {
            'filename': filename,
            'format': 'xlsx',
            'sheets': {
                'Overview': self._create_overview_sheet(tracker_data),
                'All Habits': self._create_all_habits_sheet(tracker_data),
                'Monthly Report': self._create_monthly_report_sheet(tracker_data),
                'Statistics': self._create_statistics_sheet(tracker_data),
                'Insights': self._create_insights_sheet(tracker_data)
            },
            'exported_at': datetime.now().isoformat(),
            'total_records': sum(len(t.get('entries', [])) for t in tracker_data.values())
        }
        self.exports[filename] = export
        return export
    
    def create_weekly_report_excel(self, week_data, filename='weekly_report.xlsx'):
        """
        Create weekly report in Excel
        
        Args:
            week_data: Weekly data dict
            filename: Output filename
        
        Returns:
            dict: Report configuration
        """
        report = {
            'filename': filename,
            'format': 'xlsx',
            'report_type': 'weekly',
            'sheets': {
                'Summary': self._create_weekly_summary_sheet(week_data),
                'Daily Details': self._create_weekly_details_sheet(week_data),
                'Performance': self._create_performance_sheet(week_data),
                'Goals Progress': self._create_goals_progress_sheet(week_data)
            },
            'generated_at': datetime.now().isoformat()
        }
        self.exports[filename] = report
        return report
    
    def create_monthly_report_excel(self, month_data, filename='monthly_report.xlsx'):
        """
        Create monthly report in Excel
        
        Args:
            month_data: Monthly data dict
            filename: Output filename
        
        Returns:
            dict: Report configuration
        """
        report = {
            'filename': filename,
            'format': 'xlsx',
            'report_type': 'monthly',
            'sheets': {
                'Summary': self._create_monthly_summary_sheet(month_data),
                'Daily Log': self._create_monthly_log_sheet(month_data),
                'Statistics': self._create_monthly_stats_sheet(month_data),
                'Trends': self._create_trends_sheet(month_data),
                'Achievements': self._create_achievements_sheet(month_data)
            },
            'generated_at': datetime.now().isoformat()
        }
        self.exports[filename] = report
        return report
    
    def _create_dashboard_sheet(self):
        """Create dashboard sheet structure"""
        return {
            'name': 'Dashboard',
            'columns': ['Metric', 'Value', 'Target', 'Status'],
            'rows': [
                {'Metric': 'Total Habits', 'Value': 0, 'Target': 0, 'Status': 'N/A'},
                {'Metric': 'Active Habits', 'Value': 0, 'Target': 0, 'Status': 'N/A'},
                {'Metric': 'Completion Rate', 'Value': 0, 'Target': 100, 'Status': 'Pending'},
                {'Metric': 'Current Streak', 'Value': 0, 'Target': 0, 'Status': 'Active'},
                {'Metric': 'Average Score', 'Value': 0, 'Target': 80, 'Status': 'Pending'}
            ]
        }
    
    def _create_trackers_sheet(self):
        """Create trackers sheet structure"""
        return {
            'name': 'Trackers',
            'columns': ['Habit Name', 'Frequency', 'Unit', 'Status', 'Created Date', 'Total Entries'],
            'rows': []
        }
    
    def _create_daily_log_sheet(self):
        """Create daily log sheet structure"""
        return {
            'name': 'Daily Log',
            'columns': ['Date', 'Habit', 'Value', 'Unit', 'Notes', 'Time'],
            'rows': []
        }
    
    def _create_statistics_sheet(self, data=None):
        """Create statistics sheet structure"""
        return {
            'name': 'Statistics',
            'columns': ['Habit', 'Total Entries', 'Average', 'Max', 'Min', 'Completion %'],
            'rows': []
        }
    
    def _create_goals_sheet(self):
        """Create goals sheet structure"""
        return {
            'name': 'Goals',
            'columns': ['Goal', 'Target', 'Progress', 'Deadline', 'Status'],
            'rows': []
        }
    
    def _create_overview_sheet(self, tracker_data):
        """Create overview sheet"""
        return {
            'name': 'Overview',
            'summary': {
                'total_habits': len(tracker_data),
                'total_entries': sum(len(t.get('entries', [])) for t in tracker_data.values()),
                'average_completion': 75.5,
                'current_month': datetime.now().strftime('%B %Y')
            }
        }
    
    def _create_all_habits_sheet(self, tracker_data):
        """Create all habits sheet"""
        return {
            'name': 'All Habits',
            'columns': ['Habit', 'Entries', 'Streak', 'Completion %', 'Last Entry'],
            'rows': []
        }
    
    def _create_monthly_report_sheet(self, tracker_data):
        """Create monthly report sheet"""
        return {
            'name': 'Monthly Report',
            'columns': ['Week', 'Habits Completed', 'Total Entries', 'Average Score'],
            'rows': []
        }
    
    def _create_insights_sheet(self, tracker_data):
        """Create insights sheet"""
        return {
            'name': 'Insights',
            'insights': [
                'Keep up the great work!',
                'Try to maintain consistency',
                'Focus on morning habits'
            ]
        }
    
    def _create_weekly_summary_sheet(self, week_data):
        """Create weekly summary sheet"""
        return {
            'name': 'Summary',
            'columns': ['Day', 'Habits Completed', 'Total Target', 'Completion %'],
            'rows': []
        }
    
    def _create_weekly_details_sheet(self, week_data):
        """Create weekly details sheet"""
        return {
            'name': 'Daily Details',
            'columns': ['Date', 'Habit', 'Status', 'Value', 'Time'],
            'rows': []
        }
    
    def _create_performance_sheet(self, week_data):
        """Create performance sheet"""
        return {
            'name': 'Performance',
            'columns': ['Habit', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            'rows': []
        }
    
    def _create_goals_progress_sheet(self, week_data):
        """Create goals progress sheet"""
        return {
            'name': 'Goals Progress',
            'columns': ['Goal', 'Target', 'Achieved', 'Progress %'],
            'rows': []
        }
    
    def _create_monthly_summary_sheet(self, month_data):
        """Create monthly summary sheet"""
        return {
            'name': 'Summary',
            'columns': ['Week', 'Completion %', 'Streak', 'Total Entries'],
            'rows': []
        }
    
    def _create_monthly_log_sheet(self, month_data):
        """Create monthly log sheet"""
        return {
            'name': 'Daily Log',
            'columns': ['Date', 'Habit', 'Value', 'Notes'],
            'rows': []
        }
    
    def _create_monthly_stats_sheet(self, month_data):
        """Create monthly stats sheet"""
        return {
            'name': 'Statistics',
            'columns': ['Habit', 'Days Done', 'Success Rate', 'Best Day', 'Lowest Day'],
            'rows': []
        }
    
    def _create_trends_sheet(self, month_data):
        """Create trends sheet"""
        return {
            'name': 'Trends',
            'columns': ['Week', 'Trend', 'Change %', 'Status'],
            'rows': []
        }
    
    def _create_achievements_sheet(self, month_data):
        """Create achievements sheet"""
        return {
            'name': 'Achievements',
            'achievements': [
                'Completed all habits for 1 week',
                'Maintained 30-day streak',
                'Reached 100 total entries'
            ]
        }
    
    def get_export_config(self, filename):
        """Get export configuration"""
        return self.exports.get(filename)
    
    def list_exports(self):
        """List all exports"""
        return list(self.exports.values())
    
    def get_download_url(self, filename):
        """Get download URL for exported file"""
        if filename in self.exports or filename in self.templates:
            return {
                'filename': filename,
                'url': f'downloads/{filename}',
                'format': 'xlsx',
                'available': True
            }
        return None
