from flask import abort, session
from .models import User, db

@app.route('/account/<int:user_id>')
def get_account(user_id):
    # 1. Check if user is logged in
    current_user_id = session.get('user_id')
    if not current_user_id:
        abort(401) # Unauthorized

    # 2. Check if the requested ID matches the session ID (or is an Admin)
    if current_user_id != user_id:
        abort(403) # Forbidden

    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())
