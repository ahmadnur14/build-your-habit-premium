"""
Dashboard Builder Module
Creates dashboard layouts and components for visualization
"""


class DashboardBuilder:
    """Build and manage dashboard components"""
    
    def __init__(self):
        """Initialize dashboard builder"""
        self.components = {}
        self.layouts = {}
        self.widgets = {}
    
    def create_dashboard(self, dashboard_id, title, layout_type='grid'):
        """
        Create a new dashboard
        
        Args:
            dashboard_id: Unique identifier
            title: Dashboard title
            layout_type: Layout type (grid, flex, column, row)
        
        Returns:
            dict: Dashboard configuration
        """
        dashboard = {
            'id': dashboard_id,
            'title': title,
            'layout_type': layout_type,
            'components': [],
            'created_at': None,
            'updated_at': None,
            'active': True
        }
        self.layouts[dashboard_id] = dashboard
        return dashboard
    
    def add_component(self, dashboard_id, component_id, component_type, position, size):
        """
        Add a component to dashboard
        
        Args:
            dashboard_id: Dashboard identifier
            component_id: Component identifier
            component_type: Type of component (card, chart, metric, etc.)
            position: Position (x, y) tuple
            size: Size (width, height) tuple
        
        Returns:
            bool: Success status
        """
        if dashboard_id not in self.layouts:
            return False
        
        component = {
            'id': component_id,
            'type': component_type,
            'position': position,
            'size': size,
            'config': {},
            'visible': True
        }
        
        self.components[component_id] = component
        self.layouts[dashboard_id]['components'].append(component_id)
        return True
    
    def create_metric_card(self, card_id, title, metric_name, value, unit=''):
        """
        Create a metric card component
        
        Args:
            card_id: Card identifier
            title: Card title
            metric_name: Name of the metric
            value: Metric value
            unit: Unit of measurement
        
        Returns:
            dict: Metric card configuration
        """
        card = {
            'id': card_id,
            'type': 'metric_card',
            'title': title,
            'metric_name': metric_name,
            'value': value,
            'unit': unit,
            'color': '#3498db',
            'icon': None
        }
        self.widgets[card_id] = card
        return card
    
    def create_progress_bar(self, progress_id, label, current_value, max_value, target_value=None):
        """
        Create a progress bar component
        
        Args:
            progress_id: Progress bar identifier
            label: Label text
            current_value: Current value
            max_value: Maximum value
            target_value: Target value (optional)
        
        Returns:
            dict: Progress bar configuration
        """
        progress_percent = (current_value / max_value * 100) if max_value > 0 else 0
        
        progress = {
            'id': progress_id,
            'type': 'progress_bar',
            'label': label,
            'current_value': current_value,
            'max_value': max_value,
            'target_value': target_value,
            'percent': progress_percent,
            'color': '#2ecc71' if progress_percent >= 80 else '#f39c12' if progress_percent >= 50 else '#e74c3c'
        }
        self.widgets[progress_id] = progress
        return progress
    
    def create_summary_widget(self, widget_id, title, data_items):
        """
        Create a summary widget
        
        Args:
            widget_id: Widget identifier
            title: Widget title
            data_items: List of {label, value} items
        
        Returns:
            dict: Summary widget configuration
        """
        widget = {
            'id': widget_id,
            'type': 'summary_widget',
            'title': title,
            'items': data_items,
            'layout': 'list'
        }
        self.widgets[widget_id] = widget
        return widget
    
    def update_component_config(self, component_id, config):
        """Update component configuration"""
        if component_id in self.components:
            self.components[component_id]['config'].update(config)
            return True
        return False
    
    def get_dashboard_layout(self, dashboard_id):
        """Get complete dashboard layout"""
        if dashboard_id not in self.layouts:
            return None
        
        dashboard = self.layouts[dashboard_id]
        components_data = [self.components[cid] for cid in dashboard['components'] if cid in self.components]
        
        return {
            **dashboard,
            'components_data': components_data
        }
    
    def remove_component(self, dashboard_id, component_id):
        """Remove component from dashboard"""
        if dashboard_id in self.layouts and component_id in self.layouts[dashboard_id]['components']:
            self.layouts[dashboard_id]['components'].remove(component_id)
            return True
        return False
