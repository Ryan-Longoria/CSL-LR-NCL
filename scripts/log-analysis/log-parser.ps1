$filepath = Read-Host -Prompt "Input your log's filepath"
Write-Output "You entered filepath: $filepath`n"
$filedata = Get-Content $filepath

while(1){
	Write-Output "---------------------------------------------------------------------------------------"
	Write-Output "Log-Analysis options: "
	Write-Output "1. Output the first line               2. Output the last line"
	Write-Output "3. Find a specific line                4. Find lines containing specific word(s)"
	Write-Output "5. Find most occurred words            6. Find the occurrences of a specific word/line"
	Write-Output "7. Find line(s) with Regex pattern     8. Count number of lines"
	Write-Output "9. Quit`n"
	$option = Read-Host -Prompt "Enter option"

	if($option -eq 1) {
		$first = $filedata[0]
		Write-Output "$first"
	}

	if ($option -eq 8) {
		$length = $filedata.length
		Write-Output "$length"
	}
	if($option -eq 9) {
		Exit
	}
}
