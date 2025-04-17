name: Deploy to VPS

on:
  push:
    branches:
      - main  # Jab tum main branch pe koi changes push karoge

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Deploy to VPS
      env:
        SSH_PRIVATE_KEY: ${{ secrets.SSH_PRIVATE_KEY }}  # Secret ke liye apni SSH key set karni hai
      run: |
        ssh -o StrictHostKeyChecking=no -i $SSH_PRIVATE_KEY root@your-vps-ip "cd /path/to/your/project && git pull && python3 main.py"
