from flask import Flask, request

app = Flask(__name__)

STYLE = """
<style>
    body { font-family: Arial, sans-serif; background: #0f1115; color: #e0e0e0; 
           display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
    .card { background: #1a1d24; padding: 40px; border-radius: 10px; 
            box-shadow: 0 4px 20px rgba(0,0,0,0.5); max-width: 500px; }
    h2 { color: #4fc3f7; margin-top: 0; }
    a { color: #4fc3f7; }
    .flag { color: #66bb6a; font-weight: bold; }
    .error { color: #ef5350; }
</style>
"""

@app.route('/')
def home():
    return f"""{STYLE}
    <div class="card">
        <h2>NEXORA Customer Portal</h2>
        <p>Welcome. Visit <a href="/profile?id=1">/profile?id=1</a> to view your profile.</p>
    </div>"""

@app.route('/profile')
def profile():
    user_id = request.args.get('id', '1')
    if user_id == '1':
        body = "<p>Welcome, User1. This is your normal profile page.</p>"
    elif user_id == 'admin':
        body = "<p class='flag'>ADMIN PANEL - FLAG: NEXORA{brok3n_4cc3ss_c0ntr0l}</p>"
    else:
        body = f"<p class='error'>User '{user_id}' not found.</p>"
    return f"""{STYLE}
    <div class="card">
        <h2>NEXORA Customer Portal</h2>
        {body}
    </div>"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
