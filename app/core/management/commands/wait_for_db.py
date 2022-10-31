'''
django command to wait for the database is to be available
'''
from sqlite3 import OperationalError
import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.core.management.base import BaseCommand


from django.core.management.base import BaseCommand
class Command(BaseCommand):
    '''django command to wait for database'''
    def handle(self,*args,**options):
        pass
        '''Entrypoint for command'''
        self.stdout.write('waiting for databases...')
        db_up=False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up=True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('database unavailable waiting for 1 sec.....')
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS("Database available"))


