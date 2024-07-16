[Setup]
AppName=GeradorDeRelatorioImpressorasHP
AppVersion=1.3
DefaultDirName={pf}\GeradorDeRelatorioImpressorasHP
DefaultGroupName=GeradorDeRelatorioImpressorasHP

[Files]
Source: "build\exe.win32-3.8\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs

[Icons]
Name: "{group}\icon2"; Filename: "{app}\GeradorDeRelatorioImpressorasHP.exe"; IconFilename: "{app}\icon2.ico"