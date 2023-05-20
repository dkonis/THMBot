# detects default nstalled browser and returns location - only chrome & firefox supported 

$browser = (Get-ItemProperty HKCU:\Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice -Name ProgId).ProgId
$b_location = (Get-ItemProperty HKLM:\SOFTWARE\Classes\$browser\DefaultIcon).'(default)'.Split(",")[0]
Write-Output $b_location