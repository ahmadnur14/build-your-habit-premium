"""
Chart Engine Module
Generates charts and visualizations for habit data
"""

from collections import defaultdict
from datetime import datetime, timedelta


class ChartEngine:
    """Generate charts and visualizations"""
    
    def __init__(self):
        """Initialize chart engine"""
        self.charts = {}
        self.data_processors = {}
    
    def create_line_chart(self, chart_id, title, entries, date_range=None):
        """
        Create a line chart
        
        Args:
            chart_id: Chart identifier
            title: Chart title
            entries: List of tracking entries
            date_range: Optional (start_date, end_date) tuple
        
        Returns:
            dict: Chart data configuration
        """
        filtered_entries = self._filter_by_date_range(entries, date_range)
        
        chart_data = {
            'id': chart_id,
            'type': 'line',
            'title': title,
            'labels': [],
            'datasets': [{
                'label': title,
                'data': [],
                'borderColor': '#3498db',
                'fill': False,
                'tension': 0.1
            }],
            'options': {
                'responsive': True,
                'plugins': {
                    'legend': {'display': True},
                    'title': {'display': True, 'text': title}
                }
            }
        }
        
        sorted_entries = sorted(filtered_entries, key=lambda x: x['timestamp'])
        for entry in sorted_entries:
            chart_data['labels'].append(entry['timestamp'].strftime('%Y-%m-%d'))
            chart_data['datasets'][0]['data'].append(entry['value'])
        
        self.charts[chart_id] = chart_data
        return chart_data
    
    def create_bar_chart(self, chart_id, title, category_data):
        """
        Create a bar chart
        
        Args:
            chart_id: Chart identifier
            title: Chart title
            category_data: Dict with {category: value}
        
        Returns:
            dict: Chart data configuration
        """
        chart_data = {
            'id': chart_id,
            'type': 'bar',
            'title': title,
            'labels': list(category_data.keys()),
            'datasets': [{
                'label': title,
                'data': list(category_data.values()),
                'backgroundColor': [
                    '#3498db', '#2ecc71', '#e74c3c', '#f39c12', '#9b59b6'
                ][:len(category_data)],
                'borderColor': '#2c3e50',
                'borderWidth': 1
            }],
            'options': {
                'responsive': True,
                'indexAxis': 'x',
                'plugins': {
                    'legend': {'display': True},
                    'title': {'display': True, 'text': title}
                }
            }
        }
        self.charts[chart_id] = chart_data
        return chart_data
    
    def create_pie_chart(self, chart_id, title, data_items):
        """
        Create a pie chart
        
        Args:
            chart_id: Chart identifier
            title: Chart title
            data_items: List of {label, value} dicts
        
        Returns:
            dict: Chart data configuration
        """
        labels = [item['label'] for item in data_items]
        values = [item['value'] for item in data_items]
        colors = ['#3498db', '#2ecc71', '#e74c3c', '#f39c12', '#9b59b6', '#1abc9c']
        
        chart_data = {
            'id': chart_id,
            'type': 'pie',
            'title': title,
            'labels': labels,
            'datasets': [{
                'data': values,
                'backgroundColor': colors[:len(data_items)],
                'borderColor': '#ecf0f1',
                'borderWidth': 2
            }],
            'options': {
                'responsive': True,
                'plugins': {
                    'legend': {'position': 'bottom'},
                    'title': {'display': True, 'text': title}
                }
            }
        }
        self.charts[chart_id] = chart_data
        return chart_data
    
    def create_heatmap(self, chart_id, title, entries, interval='day'):
        """
        Create a heatmap visualization
        
        Args:
            chart_id: Chart identifier
            title: Chart title
            entries: List of tracking entries
            interval: Time interval (day, week, month)
        
        Returns:
            dict: Heatmap data configuration
        """
        heatmap_data = defaultdict(int)
        
        for entry in entries:
            if interval == 'day':
                key = entry['timestamp'].strftime('%Y-%m-%d')
            elif interval == 'week':
                key = entry['timestamp'].strftime('%Y-W%V')
            elif interval == 'month':
                key = entry['timestamp'].strftime('%Y-%m')
            else:
                key = str(entry['timestamp'])
            
            heatmap_data[key] += 1
        
        chart = {
            'id': chart_id,
            'type': 'heatmap',
            'title': title,
            'interval': interval,
            'data': dict(heatmap_data),
            'color_scale': 'YlGn'
        }
        self.charts[chart_id] = chart
        return chart
    
    def create_comparison_chart(self, chart_id, title, datasets_list):
        """
        Create a comparison chart with multiple datasets
        
        Args:
            chart_id: Chart identifier
            title: Chart title
            datasets_list: List of {name, data, entries} dicts
        
        Returns:
            dict: Comparison chart data
        """
        colors = ['#3498db', '#2ecc71', '#e74c3c', '#f39c12', '#9b59b6']
        
        labels = set()
        for dataset in datasets_list:
            for entry in dataset.get('entries', []):
                labels.add(entry['timestamp'].strftime('%Y-%m-%d'))
        
        labels = sorted(list(labels))
        
        datasets = []
        for idx, dataset in enumerate(datasets_list):
            data_dict = {e['timestamp'].strftime('%Y-%m-%d'): e['value'] for e in dataset.get('entries', [])}
            datasets.append({
                'label': dataset['name'],
                'data': [data_dict.get(label, 0) for label in labels],
                'borderColor': colors[idx % len(colors)],
                'backgroundColor': colors[idx % len(colors)] + '20',
                'tension': 0.1
            })
        
        chart = {
            'id': chart_id,
            'type': 'comparison',
            'title': title,
            'labels': labels,
            'datasets': datasets,
            'options': {
                'responsive': True,
                'plugins': {
                    'legend': {'display': True},
                    'title': {'display': True, 'text': title}
                }
            }
        }
        self.charts[chart_id] = chart
        return chart
    
    def get_chart(self, chart_id):
        """Get chart data"""
        return self.charts.get(chart_id)
    
    def _filter_by_date_range(self, entries, date_range):
        """Filter entries by date range"""
        if not date_range:
            return entries
        
        start_date, end_date = date_range
        return [e for e in entries if start_date <= e['timestamp'] <= end_date]
