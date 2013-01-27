from django.core.management.base import BaseCommand, CommandError
from boto.ec2.connection import EC2Connection
from workingapps.models import JenkinsServer

class Command(BaseCommand):
    args = 'create to create all of the build servers pending'
    help = 'creats all pending CI build servers'

    def handle(self, *args, **options):
        if len(args) > 0: 
            if args[0] == "create":
                for pending_ci_server in JenkinsServer.objects.filter(is_active=False):
                    print("create ci box %" % str(pending_ci_server))
                #fix me - use boto to create a new CI box
            else:
                print("There were no valid arguments")
        else:
            print("There were no valid arguments")
            #fix me add error checking