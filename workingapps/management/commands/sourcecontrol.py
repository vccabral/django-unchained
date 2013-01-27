from django.core.management.base import BaseCommand, CommandError
from workingapps.models import GitRepo
from pygithub3 import Github
from pygithub3.services.repos import Repo
from workingapps.management.commands import slugify

class Command(BaseCommand):
    args = 'create to create all the repos pending'
    help = 'creates all pending git repos'

    def handle(self, *args, **options):
        if len(args) > 0:
            if args[0] == "create":
                for pending_repo in GitRepo.objects.filter(is_active=False):
                    repo_name = slugify(pending_repo.project_set.all()[0])
                    repo_service = Repo(login='vccabral', password='C@brales10')
                    for o in repo_service.list():
                        print(o)
                    #fix me - us pygithub3 api to create a new repo
            else:
                print("There were no valid arguments")
        else:
            print("There were no valid arguments")
            ##add error handling  