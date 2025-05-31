import base64
from flask import Flask, render_template, request, redirect, url_for
from .utils import auth_required
from .photos import photo, unvisited_photos_count

msg = None
img_path = photo()

selection_root_dir = "C:/Projects/Photo-Selector/photo_selector/selection_files"
wedding_root_dir = "C:/Users/Parde/Downloads/Wedding"


def create_app():
    app = Flask(__name__)

    app.config.from_prefixed_env()

    @app.route("/photos", methods=['GET', 'POST'])
    # @auth_required
    def photos():
        global msg, img_path

        if request.method == 'POST':
            if request.form['button'] == 'accept':
                with open(selection_root_dir+"/accepted.txt", 'a') as file:
                    file.writelines(img_path+"\n")
                msg = "Photo Accepted"
            elif request.form['button'] == 'reject':
                with open(selection_root_dir+"/rejected.txt", 'a') as file:
                    file.writelines(img_path+"\n")
                msg = "Photo Rejected"
            elif request.form['button'] == 'not_sure':
                with open(selection_root_dir+"/not_sure.txt", 'a') as file:
                    file.writelines(img_path+"\n")
                msg = "Photos marked as not sure"
            img_path = photo()
            return redirect(url_for('photos'))  # Redirect after POST

        with open(wedding_root_dir+img_path, "rb") as image_file:
            image_data = image_file.read()
            encoded_string = base64.b64encode(image_data).decode('utf-8')

        return render_template(
            'index.html',
            img_data=encoded_string,
            remaining_count=unvisited_photos_count(),
            msg=msg
        )

    return app
