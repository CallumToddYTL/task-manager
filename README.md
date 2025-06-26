## Features
- Secure Registering with strong password recommendation
- Login
- Role-based access (Admin/User)
- Task CRUD (Admin: Full, User: CRU)

## Running Instance
Instance is ran on AWS, using EC2.
http://13.51.150.160:5000

## Local Setup
```bash
git clone [<repo>](https://github.com/CallumToddYTL/task-manager.git)
cd clickup_clone
python -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
source venv/bin/activate  # or .\venv\Scripts\activate
pip install -r requirements.txt
flask run
