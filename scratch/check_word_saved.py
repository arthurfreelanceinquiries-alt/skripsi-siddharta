import subprocess

cmd = """
$word = [Runtime.InteropServices.Marshal]::GetActiveObject('Word.Application')
foreach ($doc in $word.Documents) {
    Write-Output "Name: $($doc.Name) | Saved: $($doc.Saved) | ReadOnly: $($doc.ReadOnly)"
}
"""
res = subprocess.run(["powershell", "-NoProfile", "-Command", cmd], capture_output=True, text=True)
print("STDOUT:", res.stdout)
print("STDERR:", res.stderr)
