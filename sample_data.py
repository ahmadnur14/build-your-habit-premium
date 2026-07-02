"""
Sample Data Generator
Creates sample habit data for Excel export demonstration
"""

from datetime import datetime, timedelta
import random


def generate_sample_tracker_data():
    """Generate sample tracker data"""
    sample_data = {}
    
    # Habit 1: Morning Exercise
    habit1_id = "habit_1"
    sample_data[habit1_id] = {
        'id': habit1_id,
        'habit_name': 'Morning Exercise',
        'target_frequency': 'daily',
        'unit': 'minutes',
        'status': 'active',
        'entries': [
            {'value': 30, 'timestamp': datetime.now() - timedelta(days=6)},
            {'value': 45, 'timestamp': datetime.now() - timedelta(days=5)},
            {'value': 30, 'timestamp': datetime.now() - timedelta(days=4)},
            {'value': 60, 'timestamp': datetime.now() - timedelta(days=3)},
            {'value': 35, 'timestamp': datetime.now() - timedelta(days=2)},
            {'value': 40, 'timestamp': datetime.now() - timedelta(days=1)},
            {'value': 50, 'timestamp': datetime.now()},
        ]
    }
    
    # Habit 2: Reading
    habit2_id = "habit_2"
    sample_data[habit2_id] = {
        'id': habit2_id,
        'habit_name': 'Reading',
        'target_frequency': 'daily',
        'unit': 'pages',
        'status': 'active',
        'entries': [
            {'value': 25, 'timestamp': datetime.now() - timedelta(days=6)},
            {'value': 30, 'timestamp': datetime.now() - timedelta(days=5)},
            {'value': 20, 'timestamp': datetime.now() - timedelta(days=4)},
            {'value': 35, 'timestamp': datetime.now() - timedelta(days=3)},
            {'value': 28, 'timestamp': datetime.now() - timedelta(days=2)},
            {'value': 32, 'timestamp': datetime.now() - timedelta(days=1)},
            {'value': 40, 'timestamp': datetime.now()},
        ]
    }
    
    # Habit 3: Meditation
    habit3_id = "habit_3"
    sample_data[habit3_id] = {
        'id': habit3_id,
        'habit_name': 'Meditation',
        'target_frequency': 'daily',
        'unit': 'minutes',
        'status': 'active',
        'entries': [
            {'value': 10, 'timestamp': datetime.now() - timedelta(days=6)},
            {'value': 15, 'timestamp': datetime.now() - timedelta(days=5)},
            {'value': 12, 'timestamp': datetime.now() - timedelta(days=4)},
            {'value': 20, 'timestamp': datetime.now() - timedelta(days=3)},
            {'value': 15, 'timestamp': datetime.now() - timedelta(days=2)},
            {'value': 18, 'timestamp': datetime.now() - timedelta(days=1)},
            {'value': 25, 'timestamp': datetime.now()},
        ]
    }
    
    # Habit 4: Drinking Water
    habit4_id = "habit_4"
    sample_data[habit4_id] = {
        'id': habit4_id,
        'habit_name': 'Drink 8 Glasses Water',
        'target_frequency': 'daily',
        'unit': 'glasses',
        'status': 'active',
        'entries': [
            {'value': 8, 'timestamp': datetime.now() - timedelta(days=6)},
            {'value': 7, 'timestamp': datetime.now() - timedelta(days=5)},
            {'value': 8, 'timestamp': datetime.now() - timedelta(days=4)},
            {'value': 9, 'timestamp': datetime.now() - timedelta(days=3)},
            {'value': 8, 'timestamp': datetime.now() - timedelta(days=2)},
            {'value': 8, 'timestamp': datetime.now() - timedelta(days=1)},
            {'value': 8, 'timestamp': datetime.now()},
        ]
    }
    
    # Habit 5: Sleep 8 Hours
    habit5_id = "habit_5"
    sample_data[habit5_id] = {
        'id': habit5_id,
        'habit_name': 'Sleep 8 Hours',
        'target_frequency': 'daily',
        'unit': 'hours',
        'status': 'active',
        'entries': [
            {'value': 7.5, 'timestamp': datetime.now() - timedelta(days=6)},
            {'value': 8, 'timestamp': datetime.now() - timedelta(days=5)},
            {'value': 7, 'timestamp': datetime.now() - timedelta(days=4)},
            {'value': 8.5, 'timestamp': datetime.now() - timedelta(days=3)},
            {'value': 8, 'timestamp': datetime.now() - timedelta(days=2)},
            {'value': 8, 'timestamp': datetime.now() - timedelta(days=1)},
            {'value': 9, 'timestamp': datetime.now()},
        ]
    }
    
    return sample_data
