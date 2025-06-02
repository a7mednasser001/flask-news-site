
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

df = pd.read_excel("reports_data.xlsx")
df.fillna('', inplace=True)

@app.route('/')
def index():
    reports = df.to_dict(orient='records')
    return render_template('index.html', reports=reports)

@app.route('/report/<slug>')
def report(slug):
    report_row = df[df['slug'] == slug]
    if report_row.empty:
        return "التقرير غير موجود", 404
    report = report_row.to_dict(orient='records')[0]
    return render_template('report.html', report=report)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
