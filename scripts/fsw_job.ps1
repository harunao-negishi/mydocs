# fsw_job.ps1
# Background FileSystemWatcher that appends events to a log file.
param(
    [string] $WatchPath = "$PSScriptRoot\..\docs",
    [string] $LogPath = "$PSScriptRoot\..\mkdocs_watcher_events.log",
    [int] $RunSeconds = 180
)
# Normalize paths
$WatchPath = (Resolve-Path $WatchPath).ProviderPath
$LogPath = (Resolve-Path $LogPath -ErrorAction SilentlyContinue).ProviderPath
if (-not $LogPath) { $LogPath = Join-Path (Resolve-Path $PSScriptRoot\..).ProviderPath 'mkdocs_watcher_events.log' }
if (Test-Path $LogPath) { Remove-Item $LogPath -Force }
Add-Content -Path $LogPath -Value "Starting background FileSystemWatcher on $WatchPath at $(Get-Date -Format o)"
$fsw = New-Object System.IO.FileSystemWatcher $WatchPath -Property @{IncludeSubdirectories=$true; Filter='*.md'; NotifyFilter=[System.IO.NotifyFilters]'FileName,LastWrite,Size,Attributes'}
Register-ObjectEvent -InputObject $fsw -EventName Changed -SourceIdentifier 'FSW_Changed' -Action { param($s,$e) [System.IO.File]::AppendAllText('$LogPath', "$(Get-Date -Format o) [Event] $($e.ChangeType) $($e.FullPath)`n") }
Register-ObjectEvent -InputObject $fsw -EventName Created -SourceIdentifier 'FSW_Created' -Action { param($s,$e) [System.IO.File]::AppendAllText('$LogPath', "$(Get-Date -Format o) [Event] $($e.ChangeType) $($e.FullPath)`n") }
Register-ObjectEvent -InputObject $fsw -EventName Deleted -SourceIdentifier 'FSW_Deleted' -Action { param($s,$e) [System.IO.File]::AppendAllText('$LogPath', "$(Get-Date -Format o) [Event] $($e.ChangeType) $($e.FullPath)`n") }
Register-ObjectEvent -InputObject $fsw -EventName Renamed -SourceIdentifier 'FSW_Renamed' -Action { param($s,$e) [System.IO.File]::AppendAllText('$LogPath', "$(Get-Date -Format o) [Renamed] $($e.OldFullPath) -> $($e.FullPath)`n") }
$fsw.EnableRaisingEvents = $true
Start-Sleep -Seconds $RunSeconds
Unregister-Event -SourceIdentifier 'FSW_Changed','FSW_Created','FSW_Deleted','FSW_Renamed' -ErrorAction SilentlyContinue
$fsw.Dispose()
Add-Content -Path $LogPath -Value "Stopped watcher at $(Get-Date -Format o)"
