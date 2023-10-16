from flask import Flask, render_template, request, redirect, url_for
import replicate
import os

app = Flask(__name__)
token = os.getenv("REPLICATE_TOKEN")

@app.route('/', methods=['GET', 'POST'])
def upload_photo():
    if request.method == 'POST':
        # return FileStorage Object
        uploaded_photo = request.files['photo']
        if uploaded_photo:
            uploaded_photo.save('pics/uploaded_file.jpg')
            return redirect(url_for('show'))
        
    return render_template('upload_photo.html')

@app.route('/altText', methods=['GET', 'POST'])
def show():
    output = generate_alt_text('pics/uploaded_file.jpg')
    
    return render_template('output.html', output=output)


def generate_alt_text(photo):
    print(token)
    output = replicate.run(
        "salesforce/blip:2e1dddc8621f72155f24cf2e0adbde548458d3cab9f00c0139eea840d0ac4746",
        input={"image": open(photo, "rb")},
        api_key=token
    )
    print(output)
    return output

if __name__ == '__main__':
    app.run()