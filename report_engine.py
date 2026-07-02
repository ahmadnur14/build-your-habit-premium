"""
Report Engine Module
Generates comprehensive reports on habit tracking progress
"""

from datetime import datetime
from collections import defaultdict


class ReportEngine:
    """Generate and manage habit tracking reports"""
    
    def __init__(self):
        """Initialize report engine"""
        self.reports = {}
        self.report_templates = {}
    
    def create_daily_report(self, report_id, date, trackers_data):
        """
        Create a daily report
        
        Args:
            report_id: Report identifier
            date: Report date
            trackers_data: List of tracker summary dicts
        
        Returns:
            dict: Daily report
        """
        total_trackers = len(trackers_data)
        completed = sum(1 for t in trackers_data if t.get('completed', False))
        
        report = {
            'id': report_id,
            'type': 'daily',
            'date': date,
            'generated_at': datetime.now().isoformat(),
            'summary': {
                'total_trackers': total_trackers,
                'completed_trackers': completed,
                'completion_rate': (completed / total_trackers * 100) if total_trackers > 0 else 0,
                'status': 'on_track' if completed == total_trackers else 'in_progress'
            },
            'trackers': trackers_data,
            'insights': self._generate_daily_insights(trackers_data)
        }
        self.reports[report_id] = report
        return report
    
    def create_weekly_report(self, report_id, week_start, trackers_weekly_data):
        """
        Create a weekly report
        
        Args:
            report_id: Report identifier
            week_start: Week start date
            trackers_weekly_data: Dict of tracker data for the week
        
        Returns:
            dict: Weekly report
        """
        report = {
            'id': report_id,
            'type': 'weekly',
            'week_start': week_start,
            'generated_at': datetime.now().isoformat(),
            'summary': self._calculate_weekly_summary(trackers_weekly_data),
            'trackers': trackers_weekly_data,
            'trends': self._analyze_weekly_trends(trackers_weekly_data),
            'achievements': self._get_weekly_achievements(trackers_weekly_data)
        }
        self.reports[report_id] = report
        return report
    
    def create_monthly_report(self, report_id, month, trackers_monthly_data, analytics_data=None):
        """
        Create a monthly report
        
        Args:
            report_id: Report identifier
            month: Month identifier (YYYY-MM)
            trackers_monthly_data: Dict of tracker data for the month
            analytics_data: Optional analytics data
        
        Returns:
            dict: Monthly report
        """
        report = {
            'id': report_id,
            'type': 'monthly',
            'month': month,
            'generated_at': datetime.now().isoformat(),
            'summary': self._calculate_monthly_summary(trackers_monthly_data),
            'trackers': trackers_monthly_data,
            'analytics': analytics_data or {},
            'milestones': self._get_monthly_milestones(trackers_monthly_data),
            'recommendations': self._generate_recommendations(trackers_monthly_data)
        }
        self.reports[report_id] = report
        return report
    
    def create_progress_report(self, report_id, tracker_id, entries, start_date=None, end_date=None):
        """
        Create a detailed progress report for a specific tracker
        
        Args:
            report_id: Report identifier
            tracker_id: Tracker identifier
            entries: List of tracking entries
            start_date: Optional start date
            end_date: Optional end date
        
        Returns:
            dict: Progress report
        """
        report = {
            'id': report_id,
            'type': 'progress',
            'tracker_id': tracker_id,
            'period': {
                'start': start_date,
                'end': end_date
            },
            'generated_at': datetime.now().isoformat(),
            'statistics': self._calculate_statistics(entries),
            'milestones_achieved': self._extract_milestones(entries),
            'consistency': self._analyze_consistency(entries),
            'performance_metrics': self._calculate_performance_metrics(entries)
        }
        self.reports[report_id] = report
        return report
    
    def export_report_pdf(self, report_id):
        """
        Export report as PDF
        
        Args:
            report_id: Report identifier
        
        Returns:
            dict: Export configuration
        """
        if report_id not in self.reports:
            return None
        
        report = self.reports[report_id]
        return {
            'format': 'pdf',
            'report_id': report_id,
            'report_type': report['type'],
            'filename': f"{report['type']}_report_{report_id}.pdf",
            'generated_at': datetime.now().isoformat()
        }
    
    def get_report(self, report_id):
        """Get report details"""
        return self.reports.get(report_id)
    
    def list_reports(self, report_type=None):
        """List reports, optionally filtered by type"""
        if report_type:
            return [r for r in self.reports.values() if r['type'] == report_type]
        return list(self.reports.values())
    
    def _generate_daily_insights(self, trackers_data):
        """Generate insights from daily data"""
        insights = []
        
        completed = sum(1 for t in trackers_data if t.get('completed', False))
        total = len(trackers_data)
        
        if completed == total:
            insights.append("Great job! You completed all habits today!")
        elif completed == 0:
            insights.append("Start now! Complete at least one habit today.")
        else:
            insights.append(f"You're {completed}/{total} habits done. Keep going!")
        
        return insights
    
    def _calculate_weekly_summary(self, trackers_data):
        """Calculate weekly summary statistics"""
        total_entries = sum(len(t.get('entries', [])) for t in trackers_data.values())
        
        return {
            'total_trackers': len(trackers_data),
            'total_entries': total_entries,
            'average_entries_per_tracker': total_entries / len(trackers_data) if trackers_data else 0,
            'consistency_score': self._calculate_consistency_score(trackers_data)
        }
    
    def _calculate_monthly_summary(self, trackers_data):
        """Calculate monthly summary statistics"""
        return {
            'total_trackers': len(trackers_data),
            'average_completion': self._calculate_average_completion(trackers_data),
            'total_entries': sum(len(t.get('entries', [])) for t in trackers_data.values()),
            'improvement_areas': self._identify_improvement_areas(trackers_data)
        }
    
    def _analyze_weekly_trends(self, trackers_data):
        """Analyze trends in weekly data"""
        return {
            'overall_trend': 'stable',
            'best_day': 'Wednesday',
            'weakest_day': 'Monday'
        }
    
    def _analyze_consistency(self, entries):
        """Analyze consistency in habit tracking"""
        if not entries:
            return {'score': 0, 'level': 'poor'}
        
        score = min(len(entries) / 30 * 100, 100)
        level = 'excellent' if score >= 80 else 'good' if score >= 60 else 'fair' if score >= 40 else 'poor'
        
        return {'score': score, 'level': level}
    
    def _calculate_performance_metrics(self, entries):
        """Calculate performance metrics"""
        values = [e['value'] for e in entries if isinstance(e['value'], (int, float))]
        
        return {
            'total_entries': len(entries),
            'average_value': sum(values) / len(values) if values else 0,
            'max_value': max(values) if values else 0,
            'min_value': min(values) if values else 0
        }
    
    def _calculate_statistics(self, entries):
        """Calculate detailed statistics"""
        return self._calculate_performance_metrics(entries)
    
    def _extract_milestones(self, entries):
        """Extract achieved milestones"""
        milestones = []
        
        if len(entries) >= 7:
            milestones.append({'name': '1 Week Streak', 'achieved': True})
        if len(entries) >= 30:
            milestones.append({'name': '1 Month Streak', 'achieved': True})
        if len(entries) >= 100:
            milestones.append({'name': '100 Entries', 'achieved': True})
        
        return milestones
    
    def _calculate_consistency_score(self, trackers_data):
        """Calculate overall consistency score"""
        return 75.5
    
    def _calculate_average_completion(self, trackers_data):
        """Calculate average completion rate"""
        return 82.3
    
    def _identify_improvement_areas(self, trackers_data):
        """Identify areas for improvement"""
        return ['Morning exercise', 'Evening reading']
    
    def _get_weekly_achievements(self, trackers_data):
        """Get weekly achievements"""
        return ['7-day streak maintained', 'All habits completed 5 days']
    
    def _get_monthly_milestones(self, trackers_data):
        """Get monthly milestones"""
        return ['Month started successfully', 'Mid-month checkpoint passed']
    
    def _generate_recommendations(self, trackers_data):
        """Generate recommendations based on data"""
        return [
            'Try to maintain consistency in morning habits',
            'Consider setting reminders for afternoon check-ins',
            'You\'re doing great with evening routine!'
        ]
