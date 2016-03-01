[Unit]
Description=Selenium Node
After=syslog.target

[Service]
Type=simple
User=root
Environment=DISPLAY={{ xvfb_display }}
ExecStart=/usr/bin/java -jar /usr/local/lib/selenium-server.jar -port {{ selenium_port }} -log {{ selenium_log }}
Restart=on-abort

[Install]
WantedBy=multi-user.target
