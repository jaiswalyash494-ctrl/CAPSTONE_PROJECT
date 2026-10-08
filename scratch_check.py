import subprocess
import sys

# Test Word COM
try:
    ps_cmd = '$w = New-Object -ComObject Word.Application; Write-Host "WORD:" $w.Version; $w.Quit()'
    res = subprocess.run(["powershell", "-NoProfile", "-Command", ps_cmd], capture_output=True, text=True)
    print("PS Output:", res.stdout.strip())
    print("PS Error:", res.stderr.strip())
except Exception as e:
    print("Word check error:", e)

# Test pip packages we can install or have
print("Python:", sys.version)
