#==========================================
# Desktop
source activate myenv   # (in linux)
activate myenv          # (in windows - note that you should be in your c:\anaconda2 directory)

for home pc is: source activate qsforex_env

To check the current environment has been changed:

conda info -e

And now to run Spyder with Python 3.4 just type:

spyder

run spyder from inside the virtualenv

#==========================================
# Pi

Login
Login: ssh pi@192.168.0.14
Password: raspberry
Copy file using ssh
scp /home/deckard/Documents/git_repos/qsforex/settings.py pi@192.168.0.14:~/git_repos/qsforex

Activate virtualenv
source ~/venv/qsforex/bin/activate

screen # will create a new screen

trading/trading.py #from the qsforex folder

ctl + a + d # to detach
ctl + a + k # to kill

screen -ls ~ list screens
screen -r <session id/name> # reconnect
screen -S <session name> # start with user defined name

