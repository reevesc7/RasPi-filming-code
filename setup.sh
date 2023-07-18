#!/bin/bash

#Make ~/recordings
if ! [ -d ~/recordings ] ; then
    echo "Creating recordings directory..."
    mkdir ~/recordings
    chmod o+w ~/recordings
fi

#Modify ~/.bashrc to enable auto record on ssh connection
if sudo grep -q "SSH_CONNECTION" ~/.bashrc ; then
    :
else
    echo "Adding auto record on SSH connection to .bashrc..."
    sudo echo "" >> ~/.bashrc
    sudo echo "#ADDED BY RASPI-FILMING-CODE SETUP: auto record on SSH connection" >> ~/.bashrc
    sudo echo "if [[ -n SSH_CONNECTION ]] ; then" >> ~/.bashrc
    sudo echo "    :" >> ~/.bashrc
    sudo echo "fi" >> ~/.bashrc
fi

#Make a new record command
sh ~/RasPi-filming-code/addcommand.sh
