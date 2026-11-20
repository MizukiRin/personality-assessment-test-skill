# Sync personality-assessment source repo to global Antigravity plugin directory
$ErrorActionPreference = "Stop"
$srcRoot = "E:\personality assessment test\personality-accessement-test"
$subSkill = Join-Path $srcRoot "skills\personality-assessment-test"
$globalPlugin = "C:\Users\Rin\.gemini\config\plugins\personality-assessment"

function Sync-NewerFile($pathA, $pathB) {
    $existsA = Test-Path $pathA
    $existsB = Test-Path $pathB
    if ($existsA -and -not $existsB) {
        New-Item -ItemType Directory -Path (Split-Path $pathB) -Force | Out-Null
        Copy-Item $pathA $pathB -Force
    } elseif ($existsB -and -not $existsA) {
        New-Item -ItemType Directory -Path (Split-Path $pathA) -Force | Out-Null
        Copy-Item $pathB $pathA -Force
    } elseif ($existsA -and $existsB) {
        $timeA = (Get-Item $pathA).LastWriteTimeUtc
        $timeB = (Get-Item $pathB).LastWriteTimeUtc
        if ($timeA -gt $timeB) {
            Copy-Item $pathA $pathB -Force
        } elseif ($timeB -gt $timeA) {
            Copy-Item $pathB $pathA -Force
        }
    }
}

# Keep root SKILL.md and skills/personality-assessment-test/SKILL.md in sync (newest wins)
Sync-NewerFile (Join-Path $srcRoot "SKILL.md") (Join-Path $subSkill "SKILL.md")

foreach ($folder in @("references", "resources", "scripts")) {
    $rootDir = Join-Path $srcRoot $folder
    $subDir = Join-Path $subSkill $folder
    if (Test-Path $rootDir) {
        Get-ChildItem -Path $rootDir -File -Recurse | Where-Object { $_.FullName -notmatch "__pycache__|sync_plugin\.ps1" } | ForEach-Object {
            $rel = $_.FullName.Substring($rootDir.Length).TrimStart('\')
            Sync-NewerFile $_.FullName (Join-Path $subDir $rel)
        }
    }
    if (Test-Path $subDir) {
        Get-ChildItem -Path $subDir -File -Recurse | Where-Object { $_.FullName -notmatch "__pycache__|sync_plugin\.ps1" } | ForEach-Object {
            $rel = $_.FullName.Substring($subDir.Length).TrimStart('\')
            Sync-NewerFile (Join-Path $rootDir $rel) $_.FullName
        }
    }
}

# Mirror plugin bundle to global Antigravity plugins directory (real files, no junctions)
New-Item -ItemType Directory -Path $globalPlugin -Force | Out-Null
Copy-Item -Path (Join-Path $srcRoot "plugin.json") -Destination $globalPlugin -Force
Copy-Item -Path (Join-Path $srcRoot "README.md") -Destination $globalPlugin -Force

foreach ($dir in @("assets", "skills", "rules")) {
    $srcDir = Join-Path $srcRoot $dir
    $dstDir = Join-Path $globalPlugin $dir
    if (Test-Path $srcDir) {
        New-Item -ItemType Directory -Path $dstDir -Force | Out-Null
        Copy-Item -Path (Join-Path $srcDir "*") -Destination $dstDir -Recurse -Force
    }
}

Write-Host "Synced personality-assessment plugin to $globalPlugin"