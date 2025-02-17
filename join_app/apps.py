from django.apps import AppConfig
from django.db.models.signals import post_migrate

def load_initial_data(sender, **kwargs):
    """
    Load initial data from fixtures after migrations.
    """
    from django.core.management import call_command

    # List of fixture files to load
    fixtures = [
        'contacts.json',  # Fixture for Contact
        'tasks.json',  # Fixture for Task
        'subtasks.json',  # Fixture for SubTask
    ]

    # Load each fixture
    for fixture in fixtures:
        try:
            call_command('loaddata', fixture)
            print(f"Successfully loaded {fixture}")
        except Exception as e:
            print(f"Error loading {fixture}: {e}")

class JoinAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'join_app'

    def ready(self):
        post_migrate.connect(load_initial_data, sender=self)