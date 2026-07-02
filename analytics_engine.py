"""
Analytics Engine Module
Provides data analysis and insights on habit tracking data
"""

from collections import defaultdict
from datetime import datetime, timedelta


class AnalyticsEngine:
    """Analyze habit tracking data and generate insights"""
    
    def __init__(self):
        """Initialize analytics engine"""
        self.data_cache = {}
        self.metrics = {}
    
    def calculate_completion_rate(self, tracker_id, entries, target_frequency):
        """
        Calculate habit completion rate
        
        Args:
            tracker_id: Tracker identifier
            entries: List of tracking entries
            target_frequency: Target frequency (daily, weekly, monthly)
        
        Returns:
            float: Completion rate percentage (0-100)
        """
        if not entries:
            return 0.0
        
        total_periods = self._get_periods_count(entries, target_frequency)
        completed_periods = len(entries)
        
        if total_periods == 0:
            return 0.0
        
        rate = (completed_periods / total_periods) * 100
        return min(rate, 100.0)
    
    def get_streak(self, entries, target_frequency):
        """
        Calculate current streak
        
        Args:
            entries: List of tracking entries
            target_frequency: Target frequency (daily, weekly, monthly)
        
        Returns:
            int: Current streak count
        """
        if not entries:
            return 0
        
        sorted_entries = sorted(entries, key=lambda x: x['timestamp'])
        streak = 1
        
        for i in range(len(sorted_entries) - 1, 0, -1):
            current = sorted_entries[i]['timestamp']
            previous = sorted_entries[i-1]['timestamp']
            
            if self._is_consecutive(current, previous, target_frequency):
                streak += 1
            else:
                break
        
        return streak
    
    def get_trend(self, entries, period_days=7):
        """
        Analyze trend over a period
        
        Args:
            entries: List of tracking entries
            period_days: Number of days to analyze
        
        Returns:
            dict: Trend analysis results
        """
        if not entries:
            return {'trend': 'no_data', 'change_percent': 0}
        
        now = datetime.now()
        week_ago = now - timedelta(days=period_days)
        
        recent_entries = [e for e in entries if e['timestamp'] >= week_ago]
        older_entries = [e for e in entries if week_ago > e['timestamp'] >= week_ago - timedelta(days=period_days)]
        
        recent_count = len(recent_entries)
        older_count = len(older_entries)
        
        if older_count == 0:
            change_percent = 100 if recent_count > 0 else 0
        else:
            change_percent = ((recent_count - older_count) / older_count) * 100
        
        trend = 'improving' if change_percent > 0 else 'declining' if change_percent < 0 else 'stable'
        
        return {
            'trend': trend,
            'change_percent': round(change_percent, 2),
            'recent_count': recent_count,
            'older_count': older_count
        }
    
    def get_statistics(self, entries):
        """
        Generate comprehensive statistics
        
        Args:
            entries: List of tracking entries
        
        Returns:
            dict: Statistics summary
        """
        if not entries:
            return {
                'total_entries': 0,
                'average_value': 0,
                'max_value': 0,
                'min_value': 0
            }
        
        values = [e['value'] for e in entries if isinstance(e['value'], (int, float))]
        
        return {
            'total_entries': len(entries),
            'average_value': sum(values) / len(values) if values else 0,
            'max_value': max(values) if values else 0,
            'min_value': min(values) if values else 0
        }
    
    def _is_consecutive(self, current_date, previous_date, frequency):
        """Check if two dates are consecutive based on frequency"""
        diff = (current_date - previous_date).days
        
        if frequency == 'daily':
            return diff == 1
        elif frequency == 'weekly':
            return diff <= 7
        elif frequency == 'monthly':
            return diff <= 30
        
        return False
    
    def _get_periods_count(self, entries, frequency):
        """Calculate number of periods for completion rate"""
        if not entries:
            return 0
        
        sorted_entries = sorted(entries, key=lambda x: x['timestamp'])
        first_date = sorted_entries[0]['timestamp']
        last_date = sorted_entries[-1]['timestamp']
        
        diff_days = (last_date - first_date).days
        
        if frequency == 'daily':
            return diff_days + 1
        elif frequency == 'weekly':
            return diff_days // 7 + 1
        elif frequency == 'monthly':
            return diff_days // 30 + 1
        
        return 1
