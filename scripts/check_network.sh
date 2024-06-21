#!/bin/sh

# Check if server connected to LAN
ping -c5 10.0.0.1

if [ $? -eq 0 ]; then
    echo "LAN ok"
else
    # reboot
    sudo /sbin/shutdown -r now
fi

# Check if port 80 is open
port=$(sudo lsof -i:80)

if test -z "$port"
then
      # reboot
      sudo /sbin/shutdown -r now
      echo "Port 80 not ok"
else
      echo "Port 80 ok"
fi

# Check if port 5000 is open
port2=$(sudo lsof -i:5000)

if test -z "$port2"
then
      # reboot
      sudo /sbin/shutdown -r now
      echo "Port 5000 not ok"
else
      echo "Port 5000 ok"
fi

status_code=$(curl -o /dev/null -s -w "%{http_code}\n" http://user:password@localhost/api/v1/heater/ping)
if [ $status_code -eq 200 ]; then
      echo "WebApi ok"
else
      # reboot
      sudo /sbin/shutdown -r now
      echo "WebApi not ok"      
fi

now=$(date)
echo "$now - Lan, api and ports checked." > internet.log
