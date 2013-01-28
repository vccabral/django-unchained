from django.core.management.base import BaseCommand, CommandError
from workingapps.models import GitRepo
from pygithub3 import Github
from pygithub3.services.repos import Repo
from workingapps.management.commands import slugify
from cibox.settings import GIT_LOGIN, GIT_PASSWORD

class Command(BaseCommand):
    args = 'create to create all the repos pending'
    help = 'creates all pending git repos'

    def handle(self, *args, **options):
        if len(args) > 0:
            if args[0] == "create":
                for pending_repo in GitRepo.objects.filter(is_active=False):
                    repo_name = slugify(pending_repo.project_set.all()[0])
                    repo_service = Repo(login=GIT_LOGIN, password=GIT_PASSWORD)
                    repo_service.create(dict(name=repo_name, description='desc'))
                    repo = repo_service.get(user="vccabral",repo=repo_name)
                    pending_repo.url = repo.clone_url
                    pending_repo.is_active = True
                    pending_repo.save()
            else:
                print("There were no valid arguments")
        else:
            print("There were no valid arguments")
            ##add error handling  