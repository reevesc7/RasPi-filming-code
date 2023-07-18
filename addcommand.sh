#!/bin/bash

echo "Setting up custom command..."
echo "Existing commands:"
sudo ls /usr/local/bin
read -p "  Enter name of command: " command_name

#Conditionally make the new command file in /usr/local/bin
if test -f "/usr/local/bin/${command_name}" ; then
    read -p "  The $command_name command already exists. Overwrite it? (Y/n): " response
    case "$response" in
        [nN][oO]|[nN])
            :
            ;;
        *)
            read -p "  Enter duration of recording: " record_duration
            echo "python ~/RasPi-filming-code/record.py -t ${record_duration}" | sudo tee /usr/local/bin/$command_name
            sudo chmod +x /usr/local/bin/$command_name
            ;;
    esac
else
    read -p "  Enter duration of recording: " record_duration
    echo "python ~/RasPi-filming-code/record.py -t ${record_duration}" | sudo tee /usr/local/bin/$command_name
    sudo chmod +x /usr/local/bin/$command_name
fi

#Conditionally set up auto run on SSH connection
read -p "  Auto record using this command on SSH connection? (y/N/clear) " response
case "$response" in
    [yY][eE][sS]|[yY])
        sudo sed -i -e "/.*SSH_CONNECTION.*/ {" -e "n; s/.*/    $command_name/" -e "}" ~/.bashrc
        ;;
    [nN][oO]|[nN])
        :
        ;;
    [cC][lL][eE][aA][rR]|[cC])
        sudo sed -i -e "/.*SSH_CONNECTION.*/ {" -e "n; s/.*/    :/" -e "}" ~/.bashrc
        ;;
esac
