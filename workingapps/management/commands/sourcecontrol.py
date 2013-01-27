from django.core.management.base import BaseCommand, CommandError
from workingapps.models import GitRepo
from pygithub3 import Github

class Command(BaseCommand):
    args = ''
    help = 'creats all pending git repos'

    def handle(self, *args, **options):
        if args[0] == "create":
            pending_repos = GitRepo.objects.filter(is_active=False)
            for pending_repo in pending_repos:
                print("create repo %" % str(pending_repo))
                #fix me - us pygithub3 api to create a new repo
        else:
            pass
            ##add error handling  