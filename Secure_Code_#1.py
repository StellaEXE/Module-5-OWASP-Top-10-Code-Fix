from flask import abort
from flask_login import current_user, login_required

@app.route('/account/<user_id>')
@login_required
def get_account(user_id):
    # Ensure the logged-in user is only accessing their own data
    if str(current_user.id) != str(user_id):
        abort(403) # Forbidden
        
    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        abort(404)
        
    return jsonify(user.to_dict())
