# Sources the bashrc config at ssh login
# https://stackoverflow.com/questions/820517/bashrc-at-ssh-login
if [ -f ~/.bashrc ]; then
  . ~/.bashrc
fi