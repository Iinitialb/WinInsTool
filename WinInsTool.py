import subprocess
from tqdm import tqdm
import time

subprocess.run("cls", shell=True)
winget_pkgs = [
    "Microsoft.Edge", "Google.Chrome", "Mozilla.Firefox", "Opera.Opera", "Brave.Brave", "VivaldiTechnologies.Vivaldi",
    "Git.Git", "Python.Python.3", "Nodejs.Nodejs", "OpenJS.NodeJS", "Microsoft.VisualStudioCode",
    "Microsoft.VisualStudio.2022.Community", "JetBrains.IntelliJIDEA.Community", "JetBrains.PyCharm.Community",
    "JetBrains.WebStorm", "EclipseAdoptium.Temurin.17.JDK", "Oracle.JavaRuntimeEnvironment", "Amazon.Corretto.17",
    "Docker.DockerDesktop", "PostgreSQL.PostgreSQL", "MySQL.MySQLServer", "MongoDB.Compass", "SQLite.SQLite",
    "Notepad++.Notepad++", "SublimeText.SublimeText", "VSCodium.VSCodium", "Microsoft.WindowsTerminal",
    "Microsoft.PowerToys", "7zip.7zip", "RARLab.WinRAR", "WinSCP.WinSCP", "FileZilla.FileZilla", "PuTTY.PuTTY",
    "Greenshot.Greenshot", "GIMP.GIMP", "Inkscape.Inkscape", "BlenderFoundation.Blender", "OBSProject.OBSStudio",
    "Audacity.Audacity", "VideoLAN.VLC", "Spotify.Spotify", "Discord.Discord", "SlackTechnologies.Slack",
    "Zoom.Zoom", "Microsoft.Teams", "Telegram.TelegramDesktop", "WhatsApp.WhatsApp", "Valve.Steam",
    "EpicGames.EpicGamesLauncher", "RiotGames.Valorant", "CPUID.CPU-Z", "CrystalDewWorld.CrystalDiskInfo",
    "Microsoft.PowerBI", "Microsoft.AzureCLI", "Microsoft.AzureDataStudio", "Microsoft.SQLServerManagementStudio",
    "Oracle.VirtualBox", "VMware.WorkstationPlayer", "Adobe.Acrobat.Reader.64-bit", "Microsoft.Office",
    "Microsoft.OneDrive", "Microsoft.Outlook", "Microsoft.Word", "Microsoft.Excel", "Microsoft.PowerPoint",
    "Microsoft.Access", "Microsoft.Visio", "Microsoft.Project", "Microsoft.Defender", "Microsoft.Paint",
    "Microsoft.MSPaint", "Microsoft.Calculator", "Microsoft.MicrosoftToDo", "Microsoft.StickyNotes",
    "Microsoft.MicrosoftStore", "Microsoft.XboxApp", "Microsoft.XboxGameBar", "Microsoft.XboxGamingOverlay",
    "Microsoft.XboxIdentityProvider", "Microsoft.XboxSpeechToTextOverlay", "Microsoft.Xbox.TCUI",
    "Microsoft.XboxLive", "Microsoft.XboxLiveGames", "Microsoft.XboxLiveStorage", "Microsoft.XboxLiveVoiceChat",
    "Microsoft.XboxLiveMultiplayer", "Microsoft.XboxLiveMultiplayerManager", "Microsoft.XboxLiveMultiplayerSession",
    "Microsoft.XboxLiveMultiplayerSessionManager", "Microsoft.XboxLiveMultiplayerSessionMonitor",
    "Microsoft.XboxLiveMultiplayerSessionTracker", "Microsoft.XboxLiveMultiplayerSessionTrackerManager",
    "Microsoft.XboxLiveMultiplayerSessionTrackerMonitor", "Microsoft.XboxLiveMultiplayerSessionTrackerMonitorManager",
    "Microsoft.XboxLiveMultiplayerSessionTrackerMonitorManagerService", "Microsoft.XboxLiveMultiplayerSessionTrackerMonitorManagerServiceHost",
    "Microsoft.XboxLiveMultiplayerSessionTrackerMonitorManagerServiceHostManager", "Microsoft.XboxLiveMultiplayerSessionTrackerMonitorManagerServiceHostManagerMonitor",
    "Microsoft.XboxLiveMultiplayerSessionTrackerMonitorManagerServiceHostManagerMonitorService"
]
choco_pkgs = [
    "googlechrome", "firefox", "brave", "opera", "microsoft-edge",
    "notepadplusplus", "vscode", "sublimetext3", "atom", "winscp",
    "filezilla", "putty", "git", "python", "nodejs", "openjdk", "jdk8",
    "dotnet", "dotnetfx", "dotnetcore-sdk", "visualstudio2019community", "visualstudio2022community",
    "mysql", "postgresql", "mongodb", "sqlite", "docker-desktop", "virtualbox", "vmwareworkstationplayer",
    "powershell-core", "windows-terminal", "powertoys", "chocolateygui", "7zip", "winrar", "bandizip",
    "gimp", "inkscape", "paint.net", "irfanview", "greenshot", "sharex", "snagit", "obs-studio",
    "audacity", "vlc", "spotify", "foobar2000", "mpc-hc", "ffmpeg", "handbrake", "kodi",
    "discord", "zoom", "teams", "skype", "slack", "telegram", "whatsapp", "signal",
    "steam", "epicgameslauncher", "origin", "battle.net", "riotgames", "cpuz", "gpu-z",
    "crystaldiskinfo", "crystaldiskmark", "hwmonitor", "speccy", "rufus", "windirstat", "everything",
    "teamviewer", "anydesk", "tightvnc", "ultravnc", "keepass", "bitwarden", "lastpass", "veracrypt",
    "sumatrapdf", "adobereader", "foxitreader", "calibre", "libreoffice-fresh", "openoffice", "microsoft-office-deployment",
    "curl", "wget", "nmap", "wireshark", "postman", "insomnia-rest-api-client", "fiddler", "httpie",
    "cmder", "conemu", "terminal-icons", "oh-my-posh", "oh-my-zsh", "zoxide", "bat", "ripgrep",
    "neovim", "emacs", "jupyter", "anaconda", "miniconda", "r", "rstudio", "latex"
]
choices = [
    "1. Show list of packages (sh)",
    "2. Help (hp)",
    "3. Exit (ex)",
    "4. Install packages (in)"
]

packages = winget_pkgs + choco_pkgs
for i in range(0, len(packages), 5):
    row = packages[i:i+5]
    print("  ".join(f"{pkg:<25}" for pkg in row))

selected = set()
selepack = []

def show_packages():
    subprocess.run("cls", shell=True)
    print("############################################")
    print("###         Selecting Packages           ###")
    print("############################################")
    for idx, pkg in enumerate(packages, start=1):
        mark = "[*]" if idx in selected else "[]"
        print(f"{idx:2}. {mark} {pkg}")

def welcome_message():
    subprocess.run("cls", shell=True)
    print("############################################")
    print("###      Welcome to the WinInsTool      ###")
    print("############################################")
    for choicex in choices:
        print(choicex)
welcome_message()

while True:
        user_choice = input("\nSelect an option (1-4): ").lower()
        if user_choice in ["1", "sh"]:
            show_packages()
            while True:
                selection = input("\nEnter package number to toggle selection or 'b' to go back: ").lower()
                if selection == "b":
                    welcome_message()
                    if len(selepack) == 0:
                        print("No packages selected.")
                    else:
                        winget_set = set(pkg.lower() for pkg in winget_pkgs)
                        choco_set = set(pkg.lower() for pkg in choco_pkgs)
                        winget_comp = [pkg for pkg in selepack if pkg.lower() in winget_set]
                        choco_comp = [pkg for pkg in selepack if pkg.lower() in choco_set]
                        if len(winget_comp) == 0:
                            print("No packages selected for winget.")
                        if len(choco_comp) == 0:
                            print("No packages selected for chocolatey.")
                        if len(winget_comp) > 0:
                            print("Selected packages with winget: " + ", ".join(winget_comp))
                        if len(choco_comp) > 0:
                            print("Selected packages with chocolatey: " + ", ".join(choco_comp))
                        break
                elif selection.isdigit():
                    num = int(selection)
                    subprocess.run("cls", shell=True)
                    if num > len(packages):
                        show_packages()
                        print("This package is unavailable.")
                    elif 1 <= num <= len(packages):
                        pkg_name = packages[num - 1]
                        if num in selected:
                            selected.remove(num)
                            selepack.remove(pkg_name)
                            show_packages()
                            print(f"Deselected: {pkg_name}")
                        else:
                            selected.add(num)
                            selepack.append(pkg_name)
                            show_packages()
                            print(f"Selected: {pkg_name}")
                    else:
                        show_packages()
                        print("Invalid number. Try again.")
                else:
                    subprocess.run("cls", shell=True)
                    show_packages()
                    print("Invalid input. Please enter a number or 'b'.")
        elif user_choice in ["4", "in"]:
            if len(selepack) == 0:
                print("No packages selected for installation.")
                input("Press Enter to return to the main menu...")
                welcome_message()
            else:
                print("Installing selected packages: " + ", ".join(selepack))
                subprocess.run("cls", shell=True)
                print("Checking for chocolatey and winget availability...")
                winget_set = set(pkg.lower() for pkg in winget_pkgs)
                choco_set = set(pkg.lower() for pkg in choco_pkgs)
                winget_comp = [pkg for pkg in selepack if pkg.lower() in winget_set]
                choco_comp = [pkg for pkg in selepack if pkg.lower() in choco_set]
                if winget_comp:
                    try:
                        subprocess.run("winget --version", shell=True, check=True, stdout=subprocess.DEVNULL)
                        winget_av = True
                        print("winget is available.")
                        print("Installing packages with winget...")
                    except (subprocess.CalledProcessError, FileNotFoundError):
                        choic = input("winget is not available.do you want to install it?(y/n): ").lower()
                        if choic == "y":
                            try:
                                subprocess.run(["powershell", "-Command", "Invoke-WebRequest -Uri https://aka.ms/getwinget -OutFile winget.msixbundle; Add-AppxPackage winget.msixbundle"], check=True)
                                winget_av = True
                                print("winget installed successfully. Please restart the tool.")
                                input("press any key to continue...")
                                break
                            except subprocess.CalledProcessError:
                                winget_av = False
                                print("Failed to install winget. Please install it manually and try again.")
                                input("press any key to continue...")
                                break
                        elif choic == "n":
                            print("winget installation skipped.")
                            winget_av = False
                else:
                    winget_av = False
                    print("No packages selected for winget installation.")
                    input("press any key to continue...")
                if choco_comp:
                    print("Checking for choco availability....")
                    try:
                        subprocess.run("choco --version", shell=True, check=True, stdout=subprocess.DEVNULL)
                        choco_av = True
                        print("chocolatey is available.")
                        input("Press any key to start chocolatey installation...")
                    except (subprocess.CalledProcessError, FileNotFoundError):
                        print("chocolatey is not available. Installing chocolatey...")
                        chs = input("Do you want to install chocolatey now? (y/n): ").lower()
                        if chs == "y":
                            try:
                                subprocess.run(["powershell", "-Command", "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"], check=True)
                                choco_av = True
                                print("chocolatey installed successfully. Please restart the tool.")
                                input("press any key to continue...")
                                break
                            except subprocess.CalledProcessError:
                                print("Failed to install chocolatey. Please install it manually and try again.")
                                input("press any key to continue...")
                                choco_av = False
                                break
                        elif chs == "n":
                            print("chocolatey installation skipped.")
                            choco_av = False
                else:
                    choco_av = False
                    print("No packages selected for chocolatey installation.")
                    input("press any key to continue...")
                if winget_av:
                    input("press any key to start winget installation...")
                    print("Starting winget packages installation...")
                    print("Installing: " + ", ".join(winget_comp))
                    for pkg in tqdm(winget_comp, desc="Installing with winget", unit="pkg"):
                        try:
                            subprocess.run(f'winget install --id "{pkg}" -e --silent', shell=True, check=True)
                            time.sleep(1)
                            subprocess.run("cls", shell=True)
                            print("Winget package installed: " + pkg)
                        except (subprocess.CalledProcessError, FileNotFoundError):
                            subprocess.run("cls", shell=True)
                            print(f"Failed to install {pkg} with winget.")
                else:
                    print("Skipping winget packages installation: no package to install.")
                if choco_av:
                    input("press any key to start chocolatey installation...")
                    print("Starting chocolatey packages installation...")
                    print("Installing: " + ", ".join(choco_comp))
                    for pkg1 in tqdm(choco_comp, desc="Installing with chocolatey", unit="pkg"):
                        try:
                            subprocess.run(f'choco install "{pkg1}" -y', shell=True, check=True)
                            time.sleep(1)
                            subprocess.run("cls", shell=True)
                            print("Choco package installed: " + pkg1)
                        except (subprocess.CalledProcessError, FileNotFoundError):
                            subprocess.run("cls", shell=True)
                            print(f"Failed to install {pkg1} with chocolatey.")

        elif user_choice in ["2", "hp"]:
            print("\nHelp:\n1.Select '1' or 'sh' to view and toggle or disable packages.\n3.Exit the tool\n4.Start installing selected packages.")
        elif user_choice in ["3", "ex"]:
            print("\nExiting the tool.")
            break
        else:
            print("Invalid option. Try again.")
