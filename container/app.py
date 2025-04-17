from flask import Flask, jsonify, request
import os
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(
    host=os.environ['REDSHIFT_HOST'],
    dbname='dev',
    user=os.environ['REDSHIFT_USER'],
    password=os.environ['REDSHIFT_PASSWORD']
)

@app.route('/attribution/campaign/<campaign>')
def attribution(campaign):
    model = request.args.get('model', 'bayesian_mmm')
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM sp_attribution(campaign_name := %s, model := %s)",
        (campaign, model)
    )
    cols = [d[0] for d in cur.description]
    rows = cur.fetchall()
    return jsonify([dict(zip(cols,row)) for row in rows])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
