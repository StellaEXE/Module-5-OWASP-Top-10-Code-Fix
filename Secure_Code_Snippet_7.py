import secrets
from datetime import datetime, timedelta

@app.route('/request-reset', methods=['POST'])
def request_reset():
    email = request.form['email']
    user = User.query.filter_by(email=email).first()
    
    if user:
        # Generate a secure, random one-time token
        token = secrets.token_urlsafe(32)
        user.reset_token = token
        user.token_expiry = datetime.utcnow() + timedelta(hours=1)
        db.session.commit()
        
        send_reset_email(user.email, token) # Send link to the user's email
    
    return 'If an account exists, a reset link has been sent.'
