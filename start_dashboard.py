#!/usr/bin/env python3
"""
Simple HTTP Server for AI Implementation Dashboard
Run this script to view the dashboard in your browser
"""

import http.server
import socketserver
import webbrowser
import os
from pathlib import Path

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Expires', '0')
        super().end_headers()

def start_server():
    # Change to the dashboard directory
    dashboard_dir = Path(__file__).parent
    os.chdir(dashboard_dir)
    
    Handler = MyHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("=" * 60)
        print("🚀 AI Implementation Dashboard Server Started!")
        print("=" * 60)
        print(f"\n📊 Dashboard URL: http://localhost:{PORT}/dashboard.html")
        print(f"\n📁 Serving from: {dashboard_dir}")
        print("\n💡 Instructions:")
        print("   1. The dashboard will open automatically in your browser")
        print("   2. Edit 'data/projects_data.csv' to update the data")
        print("   3. Refresh the browser to see changes")
        print("   4. Press Ctrl+C to stop the server")
        print("\n" + "=" * 60 + "\n")
        
        # Open browser automatically
        webbrowser.open(f'http://localhost:{PORT}/dashboard.html')
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n✅ Server stopped. Thank you!")

if __name__ == "__main__":
    start_server()

# Made with Bob
