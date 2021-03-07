## Questions

### Whats the version and year of the windows machine?
```powershell
Get-ComputerInfo
```

### Which user logged in last?
```powershell
(Get-LocalUser | Sort-Object -Property LastLogon)[-1].Name
```

### When did John log onto the system last?
```powershell
(Get-LocalUser -Name John).LastLogon
```

### What IP does the system connect to when it first starts?
Logout and login in back to see cmd with connection.

### What two accounts had administrative privileges (other than the Administrator user)?
```powershell
Get-LocalGroupMember -Group "Administrators"
```

### Whats the name of the scheduled task that is malicous.
```powershell
Get-ScheduledTask -TaskPath \
```

### What file was the task trying to run daily?
```powershell
(Get-ScheduledTask -TaskName "Clean file system").Actions
```

### What port did this file listen locally for?
```powershell
(Get-ScheduledTask -TaskName "Clean file system").Actions
```

### When did Jenny last logon?
```powershell
(Get-LocalUser -Name Jenny).LastLogon
```

### At what date did the compromise take place?
```powershell
(Get-ScheduledTask -TaskName "Clean file system").Date
```

### At what time did Windows first assign special privileges to a new logon?
03/02/2019 4:04:49 PM

### What tool was used to get Windows passwords?
Check the folder C:\TMP.

### What was the attackers external control and command servers IP?
```powershell
Get-Content C:\Windows\System32\drivers\etc\hosts
```

### What was the extension name of the shell uploaded via the servers website?
Check the folder: C:\inetpub\wwwroot

### What was the last port the attacker opened?
```powershell
(Get-NetFirewallRule)[0]
```


### Check for DNS poisoning, what site was targeted?
```powershell
Get-Content C:\Windows\System32\drivers\etc\hosts
```