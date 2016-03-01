[Unit]
Description=Runs an Xvfb virtual display buffer to allow headless execution of browsers

[Service]
Type=simple
User=root
ExecStart=/usr/bin/Xvfb {{ xvfb_display }} -screen 0 {{xvfb_resolution}}
Restart=on-abort

[Install]
WantedBy=multi-user.target
