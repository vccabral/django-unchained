from django.core.management.base import BaseCommand, CommandError
from boto.ec2.connection import EC2Connection
from workingapps.models import JenkinsServer
from cibox.settings import AWS_SECRET_ACCESS_KEY, AWS_ID
import time

class Command(BaseCommand):
    args = 'create to create all of the build servers pending'
    help = 'creats all pending CI build servers'

    def handle(self, *args, **options):
        if len(args) > 0: 
            if args[0] == "create":
                conn = EC2Connection(AWS_ID, AWS_SECRET_ACCESS_KEY)
                for pending_ci_server in JenkinsServer.objects.filter(is_active=False):
                    cur_git_repo = pending_ci_server.project_set.all()[0].git_repo
                    if cur_git_repo.is_active:
                        reservation = conn.run_instances(image_id='ami-03c1736a',
                                           key_name='ciboxbuild',
                                           instance_type='m1.small',
                                           security_groups=['default'])
                        found_instance = False
                        while not found_instance:
                            time.sleep(30)
                            for r in conn.get_all_instances():
                                found_instance = (r.id == reservation.id and r.instances[0].public_dns_name!="")
                        pending_ci_server.url = r.instances[0].public_dns_name
                        pending_ci_server.is_active = True
                        pending_ci_server.save()
            else:
                print("There were no valid arguments")
        else:
            print("There were no valid arguments")
            #fix me add error checking