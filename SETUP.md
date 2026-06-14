# GYM PRO - Django Backend Setup Guide

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

## Installation Steps

1. **Activate your virtual environment** (if using one):
   ```bash
   # Windows
   env\Scripts\activate
   
   # Linux/Mac
   source env/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Copy images to static folder**:
   ```bash
   # Windows
   copy images\*.* static\images\
   
   # Linux/Mac
   cp images/* static/images/
   ```

4. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (for admin panel access):
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin account.

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   - Home page: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/
   - Login: http://127.0.0.1:8000/login/
   - Register: http://127.0.0.1:8000/register/
   - Profile: http://127.0.0.1:8000/profile/ (requires login)

## Features

### User Registration & Login
- Users can register with username, email, mobile number, and password
- All user data is stored in Django admin panel
- Users can login and access their profile

### Profile Page
- Displays user information:
  - Username
  - Email
  - Mobile Number
  - Account Status
  - Last Login
  - Date Joined

### Contact Form
- Contact form submissions are stored in Django admin panel
- All contact details (name, email, message) are saved

### Admin Panel
- Access at `/admin/` with superuser credentials
- View and manage:
  - Users (with extended profile information)
  - Contact form submissions
  - All data is searchable and filterable

## Database Models

1. **UserProfile**: Extended user profile with mobile number
2. **Contact**: Contact form submissions

## URLs

- `/` - Home page with contact form
- `/register/` - User registration
- `/login/` - User login
- `/logout/` - User logout
- `/profile/` - User profile (requires login)
- `/admin/` - Django admin panel


