SSSH=/etc/ssh/sshd_config 


  
if grep -q "PasswordAuthentication no" "$SSSH";
then
  echo "Overwriding previous obs_venv"
  grep -v "PasswordAuthentication" $SSSH > temp && mv temp $SSSH
  grep -v "ChallengeResponseAuthentication" $SSSH > temp && mv temp $SSSH
  echo "ChallengeResponseAuthentication yes" >> $SSSH 
  echo "PasswordAuthentication yes" >> $SSSH 
  sudo systemctl restart ssh  
else
   echo "Pass auth is good"
    fi
