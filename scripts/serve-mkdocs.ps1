# scripts\serve-mkdocs.ps1
param(
  [string] $Address = "127.0.0.1:8000",
  [switch] $VerboseMode
)

# 1) Activate venv (adjust path if your venv is elsewhere)
$venvActivate = Join-Path -Path $PSScriptRoot -ChildPath "..\.venv\Scripts\Activate.ps1"
if (-not (Test-Path $venvActivate)) {
  Write-Error ".venv Activate script not found at $venvActivate"
  exit 1
}
. $venvActivate

# 2) Ensure polling
$Env:MKDOCS_WATCH_FORCE_POLLING = "true"

# 3) Run mkdocs (omit -v by default)
$mkdocsCmd = "mkdocs serve --dev-addr $Address"
if ($VerboseMode) { $mkdocsCmd += " -v" }

Write-Output "Starting: $mkdocsCmd (MKDOCS_WATCH_FORCE_POLLING=$Env:MKDOCS_WATCH_FORCE_POLLING)"
Invoke-Expression $mkdocsCmd