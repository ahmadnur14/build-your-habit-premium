"""
Tracker Builder Module
Handles creation and management of habit trackers
"""

class TrackerBuilder:
    """Build and configure habit trackers"""
    
    def __init__(self):
        """Initialize tracker builder"""
        self.trackers = {}
        self.tracker_config = {}
    
    def create_tracker(self, tracker_id, habit_name, target_frequency, unit):
        """
        Create a new habit tracker
        
        Args:
            tracker_id: Unique identifier for the tracker
            habit_name: Name of the habit to track
            target_frequency: Target frequency (daily, weekly, monthly)
            unit: Unit of measurement (count, minutes, pages, etc.)
        
        Returns:
            dict: Tracker configuration
        """
        tracker = {
            'id': tracker_id,
            'habit_name': habit_name,
            'target_frequency': target_frequency,
            'unit': unit,
            'created_at': None,
            'entries': [],
            'status': 'active'
        }
        self.trackers[tracker_id] = tracker
        return tracker
    
    def add_entry(self, tracker_id, value, timestamp):
        """
        Add a tracking entry to a habit tracker
        
        Args:
            tracker_id: Tracker identifier
            value: Value to record
            timestamp: When the entry was recorded
        
        Returns:
            bool: Success status
        """
        if tracker_id not in self.trackers:
            return False
        
        entry = {
            'value': value,
            'timestamp': timestamp
        }
        self.trackers[tracker_id]['entries'].append(entry)
        return True
    
    def get_tracker(self, tracker_id):
        """Get tracker details"""
        return self.trackers.get(tracker_id)
    
    def list_trackers(self):
        """List all active trackers"""
        return [t for t in self.trackers.values() if t['status'] == 'active']
    
    def update_tracker_config(self, tracker_id, config):
        """Update tracker configuration"""
        if tracker_id in self.trackers:
            self.tracker_config[tracker_id] = config
            return True
        return False
    
    def delete_tracker(self, tracker_id):
        """Mark tracker as inactive"""
        if tracker_id in self.trackers:
            self.trackers[tracker_id]['status'] = 'inactive'
            return True
        return False
