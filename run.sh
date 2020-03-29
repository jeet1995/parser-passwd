#!/usr/bin/env bash

PYTHON_VERSION=$(python --version 2>&1)
PYTHON_REQUIRED_VERSION="3.7"

if [[ ${PYTHON_VERSION} == *"$PYTHON_REQUIRED_VERSION"* ]]
then

    echo "Please enter the absolute path to the etc/passwd file"
    read PASSWD_FILE_PATH

    echo "Please enter the absolute path to the etc/group file"
    read GROUP_FILE_PATH

    python runner.py --path_etc_passwd ${PASSWD_FILE_PATH} --path_etc_group ${GROUP_FILE_PATH}

  while true
  do
    read -r -p 'Do you wish to continue (yes/no)?' choice
    case "$choice" in
      [Nn]* ) echo 'Exiting.'; exit;;
      [Yy]* ) echo ''; break;;
      * ) echo 'Response not valid, try again.';;
    esac
  done
else
    echo "The runner.py script can only be run with Python 3.7"
fi