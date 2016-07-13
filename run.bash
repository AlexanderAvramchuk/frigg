#!/bin/bash
 
NAME="frigg"                                  # Name of the application
DJANGODIR=/projects/frigg/frigg/            # Django project directory
SOCKFILE=/projects/frigg/socket/frigg.sock
USER=avrama                                       # the user to run as
                                    # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=frigg.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=frigg.wsgi                     # WSGI module name
 
echo "Starting $NAME as `whoami`"
 
# Activate the virtual environment
cd $DJANGODIR
source /projects/frigg/asgard/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /projects/frigg/asgard/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER \
  --bind=unix:$SOCKFILE \
  --log-level=error \
  --log-file=-
  --timeout=90
  --graceful-timeout=10
