SSSH=/etc/ssh/sshd_config 

  
if grep -q "PasswordAuthentication no" "$SSSH";
then
  echo "Overwriding previous SSH permissions"
  grep -v "PasswordAuthentication" $SSSH > temp && mv temp $SSSH
  grep -v "ChallengeResponseAuthentication" $SSSH > temp && mv temp $SSSH
  echo "ChallengeResponseAuthentication yes" >> $SSSH 
  echo "PasswordAuthentication yes" >> $SSSH 
  sudo systemctl restart ssh  
else
   echo "SSH is already set"
    fi
