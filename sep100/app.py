from flask import Flask, request, render_template
from jinja2 import Template

app = Flask(__name__)

def valid_ref(form):
    return True

@app.route('/addref', methods=['POST', 'GET'])
def addref():
    error = None
    if request.method == 'POST':
        if valid_ref(request.form):
            pass
            #return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid reference'
    print repr(request.form)
    return render_template('addref.html', error=error, doi=request.form['doi'] if 'doi' in request.form else None)


def main():
    # fill in template
    import conf
    with open('templates/sep100.css', 'r') as f:
        css_template = Template(f.read())
    with open('static/sep100.css', 'w') as f:
        f.write(css_template.render(conf.theme))

    app.run(debug=True)

if __name__ == '__main__':
    main()
