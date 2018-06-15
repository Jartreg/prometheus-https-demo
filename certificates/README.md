# Zertifikate
In den Ordnern `site` und `attacker` befinden sich die Zertifikate und Schlüssel für die Website und den Angreifer. Aus beiden Ordnern muss das Zertifikat mit dem Ende `-authority.cert.pem` im Testbrowser installiert werden.

## Zertifikate erstellen
Die Konfiguration der Zertifikate kann in `config.sh` geändert werden. Anschließend müssen die Zertifikate im Terminal mit `./generate.sh` neu generiert werden.

### Vorraussetzungen
* macOS oder Linux, um die Skripte auszuführen
* OpenSSL muss installiert sein (bei Linux standardmäßig der Fall)