#!/bin/sh
### BEGIN INIT INFO
# Provides:          {{ project_name }}-fcgi
# Required-Start:    $local_fs $remote_fs $network
# Required-Stop:     $local_fs $remote_fs $network
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: {{ project_name|title }} as FastCGI Django
# Description:       Start and stop {{ project_name|title }} Django project as a
#                    standalone FastCGI server instance using start-stop-daemon.
### END INIT INFO
# file: /etc/init.d/{{ project_name }}-fcgi

# Do NOT "set -e"

PATH=/sbin:/usr/sbin:/bin:/usr/bin
DESC="{{ project_name|title }} as FastCGI Django"
NAME={{ project_name }}-fcgi
ENV_ROOT={{ project_directory }}  # eg. /srv/abcproject.domain.com
PROJECT_ROOT=$ENV_ROOT
PIDFILE=/var/run/$NAME.pid
SCRIPTNAME=/etc/init.d/$NAME

DAEMON=$ENV_ROOT/bin/python
DAEMON_CHDIR=$PROJECT_ROOT
DAEMON_USER=$NAME
DAEMON_GROUP=$DAEMON_USER
FCGI_HOST=127.0.0.1
FCGI_PORT=$((8000 + $(id -u $DAEMON_USER 2> /dev/null || echo 0)))

# Variables in START*_OPTS and DAEMON_ARGS will be expanded later with eval
STARTSTOP_OPTS='--quiet --exec $DAEMON --chdir $DAEMON_CHDIR \
 --chuid $DAEMON_USER --user $DAEMON_USER --group $DAEMON_GROUP'
#START_OPTS='--background --make-pidfile'
DAEMON_ARGS='manage.py runfcgi \
 --settings=main.settings --pythonpath=$PROJECT_ROOT \
 pidfile=$PIDFILE \
 protocol=fcgi \
 minspare=1 maxspare=4 maxrequests=1000 \
 host=$FCGI_HOST port=$FCGI_PORT'
#export PYTHONPATH="$ENV_ROOT/lib/python2.6${PYTHONPATH:+:$PYTHONPATH}"

# Exit if the package is not installed
[ -x "$DAEMON" ] || exit 0

# Read configuration variable file if it is present
[ -r /etc/default/$NAME ] && . /etc/default/$NAME

# Load the VERBOSE setting and other rcS variables
. /lib/init/vars.sh

# Define LSB log_* functions.
# Depend on lsb-base (>= 3.2-14) to ensure that this file is present
# and status_of_proc is working.
. /lib/lsb/init-functions

# Expand variables
STARTSTOP_OPTS=$(eval echo "$STARTSTOP_OPTS")
START_OPTS=$(eval echo "$START_OPTS")
DAEMON_ARGS=$(eval echo "$DAEMON_ARGS")

#
# Function that starts the daemon/service
#
do_start()
{
	# Return
	#   0 if daemon has been started
	#   1 if daemon was already running
	#   2 if daemon could not be started
	start-stop-daemon --start --pidfile "$PIDFILE" $START_OPTS $STARTSTOP_OPTS \
		--test > /dev/null || return 1
	
	case "$START_OPTS" in
		*--make-pidfile*)
			;;
		*)
			# Daemon needs write access to PID file
			[ ! -e "$PIDFILE" -o -f "$PIDFILE" -a ! -L "$PIDFILE" ] && \
				touch "$PIDFILE" && chmod 600 "$PIDFILE" && \
				chown $DAEMON_USER:$DAEMON_GROUP "$PIDFILE" || return 2
			;;
	esac
	start-stop-daemon --start --pidfile "$PIDFILE" $START_OPTS $STARTSTOP_OPTS \
	   	-- $DAEMON_ARGS || return 2
	# Add code here, if necessary, that waits for the process to be ready
	# to handle requests from services started subsequently which depend
	# on this one.  As a last resort, sleep for some time.
}

#
# Function that stops the daemon/service
#
do_stop()
{
	# Return
	#   0 if daemon has been stopped
	#   1 if daemon was already stopped
	#   2 if daemon could not be stopped
	#   other if a failure occurred
	start-stop-daemon --stop --retry=TERM/30/KILL/5 --pidfile "$PIDFILE" \
		$STARTSTOP_OPTS
	RETVAL="$?"
	[ "$RETVAL" = 2 ] && return 2
	# Wait for children to finish too if this is a daemon that forks
	# and if the daemon is only ever run from this initscript.
	# If the above conditions are not satisfied then add some other code
	# that waits for the process to drop all resources that could be
	# needed by services started subsequently.  A last resort is to
	# sleep for some time.
	[ -n "$DAEMON_USER" ] && PS_SELECT="--user $DAEMON_USER"
	[ -n "$DAEMON_GROUP" ] && PS_SELECT="$PS_SELECT --group $DAEMON_GROUP"
	if [ -n "$PS_SELECT" ] && ps $PS_SELECT -o pid=,cmd= | grep -q "$DAEMON $DAEMON_ARGS"; then
		start-stop-daemon --stop --oknodo --retry=0/30/KILL/5 $STARTSTOP_OPTS
		[ "$?" = 2 ] && return 2
	fi
	# Many daemons don't delete their pidfiles when they exit.
	rm -f "$PIDFILE"
	return "$RETVAL"
}

case "$1" in
	start)
		[ "$VERBOSE" != no ] && log_daemon_msg "Starting $DESC" "$NAME"
		do_start
		case "$?" in
			0|1) [ "$VERBOSE" != no ] && log_end_msg 0 ;;
			*) [ "$VERBOSE" != no ] && log_end_msg 1 ;;
		esac
		;;
	stop)
		[ "$VERBOSE" != no ] && log_daemon_msg "Stopping $DESC" "$NAME"
		do_stop
		case "$?" in
			0|1) [ "$VERBOSE" != no ] && log_end_msg 0 ;;
			*) [ "$VERBOSE" != no ] && log_end_msg 1 ;;
		esac
		;;
	status)
		status_of_proc -p "$PIDFILE" "$DAEMON" "$NAME" && exit 0 || exit $?
		;;
	restart|force-reload)
		#
		# If the "reload" option is implemented then remove the
		# 'force-reload' alias
		#
		log_daemon_msg "Restarting $DESC" "$NAME"
		do_stop
		case "$?" in
			0|1)
				do_start
				case "$?" in
					0) log_end_msg 0 ;;
					1) log_end_msg 1 ;; # Old process is still running
					*) log_end_msg 1 ;; # Failed to start
				esac
				;;
			*)
				# Failed to stop
				log_end_msg 1
				;;
		esac
		;;
	*)
		echo "Usage: $SCRIPTNAME {start|stop|force-reload|restart|status}" >&2
		exit 3
		;;
esac

:
