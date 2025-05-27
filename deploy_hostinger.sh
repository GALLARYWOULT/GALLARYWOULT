#!/bin/bash

echo "🚀 Starting GALLARYWOULT Setup on Hostinger VPS..."

# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install python3 python3-pip python3-venv nginx git -y

# Clone project (if not already cloned)
PROJECT_DIR="/var/www/gallarywoult"
sudo rm -rf $PROJECT_DIR
sudo git clone https://github.com/GALLARYWOULT/GALLARYWOULT.git $PROJECT_DIR

# Create virtual environment
cd $PROJECT_DIR
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Start app using Gunicorn
echo "🔧 Running Gunicorn..."
gunicorn --bind 0.0.0.0:5000 app:app --daemon

# Setup NGINX
echo "⚙️ Setting up NGINX..."
sudo tee /etc/nginx/sites-available/gallarywoult > /dev/null <<EOF
server {
    listen 80;
    server_name YOUR_DOMAIN.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}
EOF

sudo ln -s /etc/nginx/sites-available/gallarywoult /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl restart nginx

echo "✅ GALLARYWOULT Deployed Successfully!"
